from rqt_gui_py.plugin import Plugin
from python_qt_binding import QtWidgets
from std_msgs.msg import String
import rclpy

QWidget = QtWidgets.QWidget
QVBoxLayout = QtWidgets.QVBoxLayout
QPushButton = QtWidgets.QPushButton
QLabel = QtWidgets.QLabel

class PhantomPlugin(Plugin):
    def __init__(self, context):
        super().__init__(context)
        self.setObjectName('PhantomPlugin')

        rclpy.init(args=None)
        self.node = rclpy.create_node('phantom_hmi_node')
        self.publisher = self.node.create_publisher(String, '/phantom/pose_command', 10)

        self._widget = QWidget()
        layout = QVBoxLayout()

        for i in range(1, 6):
            btn = QPushButton(f"Ir a Pose {i}")
            btn.clicked.connect(lambda _, n=i: self.send_pose(n))
            layout.addWidget(btn)

        self._widget.setLayout(layout)
        context.add_widget(self._widget)

    def send_pose(self, pose_id):
        msg = String()
        msg.data = f"pose_{pose_id}"
        self.publisher.publish(msg)
        self.node.get_logger().info(f'Pose {pose_id} enviada')
