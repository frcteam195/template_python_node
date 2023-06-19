#!/usr/bin/python3
import rclpy
import rclpy.node
import rclpy.parameter
from dataclasses import dataclass

@dataclass
class parameters_t:
    log_path: rclpy.parameter.Parameter = None
    log_prefix: rclpy.parameter.Parameter = None
    disabled_log_restart_time: rclpy.parameter.Parameter = None
    

def load_parameters(node : rclpy.node.Node, Parameters : parameters_t):
    node.declare_parameter("log_path", rclpy.Parameter.Type.STRING)
    node.declare_parameter("log_prefix", rclpy.Parameter.Type.STRING)
    node.declare_parameter("disabled_log_restart_time", rclpy.Parameter.Type.INTEGER)
    
    Parameters.log_path = node.get_parameter("log_path")
    Parameters.log_prefix = node.get_parameter("log_prefix")
    Parameters.disabled_log_restart_time = node.get_parameter("disabled_log_restart_time")
    
class ParameterizedNode(rclpy.node.Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.Parameters = parameters_t()
        load_parameters(self, self.Parameters)

