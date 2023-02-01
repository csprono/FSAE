#!/usr/bin/env python3
import math

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
        payload = Bool()
        dist, tol = 1.0, 1e-5 
        
        payload.data = (not math.isclose(msg.range_min, dist, rel_tol=tol) 
                        and msg.range_min < dist)
        
        self.get_logger().info(f"range is {msg.range_min}m < 1m {payload.data}")
        self.ebs_pub_.publish(payload)

def main(args=None):
    rclpy.init(args=args)
    
    node = ebsNode()
    rclpy.spin(node)

    rclpy.shutdown()