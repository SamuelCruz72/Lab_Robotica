import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PhantomHMI(Node):
    def __init__(self):
        super().__init__('phantom_hmi_node')

        # Publicador de posiciones articulares
        self.joint_pub = self.create_publisher(JointState, '/phantom/joint_target', 10)
        self.joint_sub = self.create_subscription(JointState, '/phantom/joint_states', self.joint_callback, 10)


        # Pose de referencia (home), en ticks o radianes según tu sistema
        self.home_pose = [512, 512, 512, 512, 512]
        self.latest_joint_positions = [0.0] * 5
        self.gui = None  # Se asigna luego desde HMIWindow

    def send_relative_pose(self, delta):
        pose = [float(home + d) for home, d in zip(self.home_pose, delta)]

        joint_msg = JointState()
        joint_msg.name = [f'joint_{i+1}' for i in range(len(pose))]
        joint_msg.position = pose
        self.joint_pub.publish(joint_msg)

        self.get_logger().info(f'Enviando pose absoluta: {pose}')

    def joint_callback(self, msg):
        self.latest_joint_positions = list(msg.position)
        if self.gui:
            self.gui.update_joint_labels(self.latest_joint_positions)

    
class HMIWindow(QWidget):
    def __init__(self, ros_node):
        super().__init__()
        self.ros_node = ros_node
        self.ros_node.gui = self  # Permite que el nodo llame a update_joint_labels

        self.setWindowTitle('HMI – Phantom Pincher')
        layout = QVBoxLayout()

        # Título con nuestros nombres
        title = QLabel("HMI – Phantom Pincher\nSamuel Alejandro Cruz Saavedra")
        title.setFont(QFont('Arial', 16, QFont.Bold))
        title.setStyleSheet("margin-bottom: 15px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)


        # Botones de control
        btns = [
            ("Home", [0, 0, 0, 0, 0]),
            ("Pose 2", [25, 25, 20, -20, 0]),
            ("Pose 3", [-35, 35, -30, 30, 0]),
            ("Pose 4", [85, -20, 55, 25, 0]),
            ("Pose 5", [80, -35, 55, -45, 0]),
        ]

        for name, delta in btns:
            btn = QPushButton(name)
            btn.clicked.connect(lambda _, d=delta: self.ros_node.send_relative_pose(d))
            layout.addWidget(btn)

        # Etiquetas para mostrar los valores articulares actuales
        self.joint_labels = []
        for i in range(5):
            lbl = QLabel(f'Articulación {i+1}: ---')
            layout.addWidget(lbl)
            self.joint_labels.append(lbl)

        self.setLayout(layout)

    def update_joint_labels(self, positions):
        for i, pos in enumerate(positions):
            self.joint_labels[i].setText(f'Articulación {i+1}: {pos:.2f}')

def main(args=None):
    rclpy.init(args=args)
    app = QApplication(sys.argv)
    ros_node = PhantomHMI()
    gui = HMIWindow(ros_node)
    gui.show()

    # Mantener nodo vivo
    timer = ros_node.create_timer(0.1, lambda: None)

    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
    finally:
        ros_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
