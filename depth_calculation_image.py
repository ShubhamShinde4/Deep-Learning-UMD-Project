import cv2
import torch
import numpy as np


# Assuming 'generate_depth_map' function is implemented and working properly
def generate_depth_map(image_path, depth_map_path):
    # Placeholder for the depth map generation logic
    # Replace with actual depth map generation code
    depth_map = np.random.uniform(0, 1, (384, 384)).astype(np.float32)

    # Save depth map as 16-bit image
    depth_image_16bit = np.clip(depth_map * 1000, 0, 65535).astype(np.uint16)
    cv2.imwrite(depth_map_path, depth_image_16bit)
    print(f"Depth map saved to {depth_map_path}")


# Example usage
image_path = "generated_image.png"
depth_map_path = "depth_map.png"
generate_depth_map(image_path, depth_map_path)
