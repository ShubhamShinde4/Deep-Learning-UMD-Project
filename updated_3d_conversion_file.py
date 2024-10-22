import open3d as o3d
import numpy as np
import cv2

# Define function for resizing depth image to match color image dimensions
def resize_depth_image(depth_image, color_image_shape):
    return cv2.resize(depth_image, (color_image_shape[1], color_image_shape[0]), interpolation=cv2.INTER_NEAREST)

# Define function for creating point cloud from depth and color images
def create_point_cloud_from_images(color_image_path, depth_image_path, point_cloud_path, voxel_size=0.05):
    color_image = o3d.io.read_image(color_image_path)
    depth_image = cv2.imread(depth_image_path, -1)
    depth_image_resized = resize_depth_image(depth_image, np.asarray(color_image).shape)

    # Convert to Open3D Image
    depth_image_o3d = o3d.geometry.Image(depth_image_resized)

    # Create RGBD image
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_image, depth_image_o3d, depth_scale=1000.0, depth_trunc=3.0, convert_rgb_to_intensity=False
    )

    # Set the camera intrinsics
    intrinsic = o3d.camera.PinholeCameraIntrinsic(
        width=np.asarray(color_image).shape[1],
        height=np.asarray(color_image).shape[0],
        fx=525.0,  # Placeholder value
        fy=525.0,  # Placeholder value
        cx=np.asarray(color_image).shape[1] / 2,
        cy=np.asarray(color_image).shape[0] / 2
    )

    # Create point cloud
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)

    # OPTIONAL: Add random intensity to points
    n_points = np.asarray(pcd.points).shape[0]
    intensity = np.random.rand(n_points, 3)  # Random values for intensity
    pcd.colors = o3d.utility.Vector3dVector(intensity)

    # Downsample the point cloud
    pcd_downsampled = pcd.voxel_down_sample(voxel_size=voxel_size)
    print(f"Downsampled point cloud from {n_points} to {len(pcd_downsampled.points)} points.")

    # Save the downsampled point cloud
    o3d.io.write_point_cloud(point_cloud_path, pcd_downsampled)

    # Visualize the downsampled point cloud
    o3d.visualization.draw_geometries([pcd_downsampled])

    return pcd_downsampled

# Define your paths
color_image_path = 'generated_image.png'
depth_image_path = 'depth_map.png'
point_cloud_path = 'point_cloud.pcd'

# Create and visualize the point cloud with downsampling
create_point_cloud_from_images(color_image_path, depth_image_path, point_cloud_path, voxel_size=0.05)
