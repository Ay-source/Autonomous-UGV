"""
Description:


Author: forby
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import torch
import torchvision
from torchvision.models.detection import fasterrcnn_mobilenet_v3_large_320_fpn as fasterrcnn


class ObjectDetectionNode(Node):
    """
    Description:

    Publishing topic:

    Subscribing topic:

    Message details:
    """
    def __init__(self, image):
        # Initialize the node
        super().__init__("object_detection_node")

        # Subcribe to the raw image node
        self.subscription = self.create_subscriber(Image, "image_raw", self.listener_callback, 10)
        # Publish the detected images to the detection_image node
        self.publisher = self.create_publisher(Image, "detection_image", 10)
        # Bridge ros2 image data type to cv data type
        self.bridge = CvBridge()
        self.model = torch

    def listener_callback(self):
        model = fasterrcnn(weights="DEFAULT")
        model.eval()
        prediction = model(image)
        return prediction

def main(args=None):
    # Initialize ros2
    rclpy.init(args=args)

    # Spin the node
    rclpy.spin(ObjectDetectionNode())

    # Destroy the node

    # Shutdown ros2
    rclpy.shutdown()

if __name__ == "__main__":
    main()
