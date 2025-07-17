import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/samuelcruz/Lab_Robotica/ros2_ws/phantom_ws/src/install/pincher_control'
