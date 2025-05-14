# eyes/eyes_node.py
import rclpy
from rclpy.node import Node
import pygame

class EyesNode(Node):
    def __init__(self):
        super().__init__('eyes')
        pygame.init()
        self.get_logger().info('Eyes node initialized with pygame!')

def main(args=None):
    rclpy.init(args=args)
    node = EyesNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
