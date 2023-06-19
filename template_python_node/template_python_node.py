#!/usr/bin/python3

import rclpy
from template_python_node.generated.parameters import ParameterizedNode

from std_msgs.msg import String


class LocalNode(ParameterizedNode):
    def __init__(self):
        super().__init__('template_python_node')



def main(args=None):
    rclpy.init(args=args)
    node = LocalNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()