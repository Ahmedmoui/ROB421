import os
import sys

import rclpy
from rclpy.node import Node
import pygame  


class EyesNode(Node):
    def __init__(self):
        super().__init__('eyes')
        pygame.init()
        self.get_logger().info('Pygame initialized!')
        # initilaize
        pygame.init()
        screen = pygame.display.set_mode((480, 800), pygame.NOFRAME)
        pygame.display.set_caption("Blinking Eyes - Portrait")
        clock = pygame.time.Clock()
        pygame.display.flip()
        

def main(args=None):
    rclpy.init(args=args)
    node = EyesNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
