# pincher_control/control_servo.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from dynamixel_sdk import PortHandler, PacketHandler
import time

# Direcciones de registro en el AX-12A
ADDR_TORQUE_ENABLE    = 24
ADDR_GOAL_POSITION    = 30
ADDR_MOVING_SPEED     = 32
ADDR_TORQUE_LIMIT     = 34
ADDR_PRESENT_POSITION = 36

class PincherController(Node):
    def __init__(self):
        super().__init__('pincher_controller')

        # Define dxl_ids desde el inicio
        self.declare_parameter('dxl_ids', [1, 2, 3, 4, 5])
        self.dxl_ids = self.get_parameter('dxl_ids').value

        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 1000000)
        self.declare_parameter('moving_speed', 100)
        self.declare_parameter('torque_limit', 600)
        self.declare_parameter('delay', 0.5)

        port_name     = self.get_parameter('port').value
        baudrate      = self.get_parameter('baudrate').value
        self.speed    = self.get_parameter('moving_speed').value
        self.torque   = self.get_parameter('torque_limit').value
        self.delay    = self.get_parameter('delay').value
        delay_seconds = 0.5
        self.port = None
        self.packet = None


        # Inicializar comunicación
        self.port = PortHandler(port_name)
        self.port.openPort()
        self.port.setBaudRate(baudrate)
        self.packet = PacketHandler(1.0)

        self.joint_pub = self.create_publisher(JointState, '/phantom/joint_states', 10)
        self.timer = self.create_timer(0.5, self.publish_joint_state)

        # 1) Configurar torque_limite, velocidad y enviar posición a cada servo
        for dxl_id in self.dxl_ids:
            # Limitar torque
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_TORQUE_LIMIT, self.torque)
            # Limitar velocidad
            self.packet.write2ByteTxRx(self.port, dxl_id, ADDR_MOVING_SPEED, self.speed)
            # Habilitar torque
            self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 1)
            # Enviar posición objetivo
            self.create_subscription(JointState, '/phantom/joint_target', self.joint_callback, 10)
            self.get_logger().info('Pincher listo para recibir comandos en /phantom/joint_target')

            self.get_logger().info(f'Esperando {delay_seconds}s para que el motor ID {dxl_id} complete su movimiento...')
            time.sleep(delay_seconds)

        # 2) (Opcional) Leer y mostrar posición actual
        for dxl_id in self.dxl_ids:
            pos, _, _ = self.packet.read2ByteTxRx(self.port, dxl_id, ADDR_PRESENT_POSITION)
            self.get_logger().info(f'[ID {dxl_id}] posición actual={pos}')

        # 3) Esperar a que todos los servos alcancen la posición
        self.get_logger().info(f'Esperando {delay_seconds}s para completar movimiento...')
        time.sleep(delay_seconds)

        # 4) Apagar torque en todos los servos
        for dxl_id in self.dxl_ids:
            self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 0)

    def joint_callback(self, msg):
        if not hasattr(self, 'dxl_ids'):
            self.get_logger().error('dxl_ids no está definido aún')
            return

        if len(msg.position) != len(self.dxl_ids):
            self.get_logger().warn('Cantidad de posiciones no coincide con cantidad de motores.')
            return

        for i, goal in enumerate(msg.position):
            dxl_id = self.dxl_ids[i]
            ticks = int(goal)
            self.packet.write2ByteTxRx(self.port, dxl_id, 30, ticks)
            self.get_logger().info(f'[ID {dxl_id}] → Posición objetivo: {ticks}')
            time.sleep(self.delay)

    def publish_joint_state(self):
        joint_msg = JointState()
        joint_msg.name = [f'joint_{i+1}' for i in range(len(self.dxl_ids))]
        joint_msg.position = []

        for dxl_id in self.dxl_ids:
            pos, _, _ = self.packet.read2ByteTxRx(self.port, dxl_id, ADDR_PRESENT_POSITION)
            if pos is not None:
                joint_msg.position.append(float(pos))
            else:
                joint_msg.position.append(0.0)  # valor por defecto si falla

        self.joint_pub.publish(joint_msg)

    def destroy_node(self):
        for dxl_id in self.dxl_ids:
            self.packet.write1ByteTxRx(self.port, dxl_id, ADDR_TORQUE_ENABLE, 0)
        self.port.closePort()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = PincherController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
