# class that contains source code for node
import rclpy
from rclpy.node import Node
from pymodbus.client import ModbusTcpClient
from conveyor_interfaces.msg import ConveyorState
from conveyor_interfaces.srv import EnableConveyor, SetConveyorState

class ConveyorController(Node):
    def __init__(self):
        super().__init__('conveyor_controller')

        #create publisher
        self.pub_state = self.create_publisher(ConveyorState, "conveyor/state", 10) 
        self.publish_timer = self.create_timer(1, self.pub_state_cb)

        #create services
        self.enable_conveyor = self.create_service(EnableConveyor, "conveyor/enable", self.enable_conveyor_cb)
        self.set_conveyor = self.create_service(SetConveyorState, "conveyor/set_state", self.set_conveyor_state_cb)

        self.direction = ConveyorState.FORWARD
        self.speed = 0.0
        self.enabled = False 

        #connect to modbus
        # self.client = ModbusTcpClient('192.168.1.50', port='502')
        # self.client.connect()

    def pub_state_cb(self):
        state_msg = ConveyorState()
        state_msg.direction = self.direction
        state_msg.speed = self.speed
        state_msg.enabled = self.enabled

        self.pub_state.publish(state_msg)

    def enable_conveyor_cb(self, request: EnableConveyor.Request, response: EnableConveyor.Response):
        if request.enable:
            # Send signal over Modbus to enable conveyor
            pass 
    
        self.enabled = request.enable
        response.success = True
        response.message = "Conveyor On"
        return response

    def set_conveyor_state_cb(self, request: SetConveyorState.Request, response: SetConveyorState.Response):
        self.get_logger().info(f"Speed: {request.speed}, Direction: {request.direction}")

        response.success = True
        response.message = "All good"

        return response
        


def main(args=None):
    rclpy.init(args=args)
    node = ConveyorController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()