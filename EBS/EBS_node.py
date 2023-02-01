#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan

class ebsNode(Node):
    def __init__(self):
        super().__init__("ebsNode")
        self.ebs_pub_ = self.create_publisher(Bool, "/trigger_ebs", 10)
        self.ebs_sub_ = self.create_subscription(LaserScan, "/lidar", self.on_msg, 10)
        self.get_logger().info("ebsNode Initialised")

    def on_msg(self, msg):
        #self.ebs_pub_.publish()
        self.get_logger().info("msg received")


def main(args=None):
    rclpy.init(args=args)

    node = ebsNode()
    rclpy.spin(node)

    rclpy.shutdown()