#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.get_logger().info("Hello from ROS2")
        self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

#test node: executable (what you run in terminal)
#first_node: node name
#my_robot_controller: package name
#my_first_node: file name

#symlink helps you make edits without needing to build every time
def main(args=None):
    rclpy.init(args = args)
    node = MyNode()
    rclpy.spin(node) #this node is kept alive until killed
    rclpy.shutdown()
if __name__ == "__main__":
    main()
