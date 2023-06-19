#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class LocalNode(Node):
    def __init__(self):
        super().__init__('tt_py_node')

def main(args=None):
    rclpy.init(args=args)
    node = LocalNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()