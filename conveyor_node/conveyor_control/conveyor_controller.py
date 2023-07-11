# class that contains source code for node
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool, Float32, String
from rcl_interfaces.srv import SetParameters
from pymodbus.client import ModbusTcpClient

# class ConveyorController(Node):
    