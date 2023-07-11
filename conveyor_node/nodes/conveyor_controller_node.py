# executable that runs node
import rclpy
from rclpy.node import Node


class ConveyorNode(Node):
    def __init__(self):
        super().__init__("conveyor_node")










def main(args=None):
    rclpy.init(arg=args)
    node = ConveyorNode()
    rclpy.spin(node)
    rclpy.shutdown()
    if __name__ == "__main__":
        main()