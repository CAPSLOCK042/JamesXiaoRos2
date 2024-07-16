#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args = args)
    node = PoseSubscriber()
    rclpy.spin(node) #this node is kept alive until killed
    rclpy.shutdown()

if __name__ == "__main__":
    main()