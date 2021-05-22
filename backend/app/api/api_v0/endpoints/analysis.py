import open3d as o3d
import numpy as np
from fastapi import APIRouter
from app.db.emulate_db import get_cameras_data_from_db
from app import schemas

router = APIRouter()


def in_doors(pcd_path: str):
    data_json = dict()
    data_json['figures'] = []
    pcd = o3d.io.read_point_cloud(pcd_path)
    # pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    # voxel_down = pcd.voxel_down_sample(voxel_size=0.02)
    voxel_crop = np.asarray(pcd.points)
    voxel_crop = voxel_crop[(voxel_crop[:, 1] < -0.2) * (-0.28 < voxel_crop[:, 1])]
    pcd_crop = o3d.geometry.PointCloud()
    pcd_crop.points = o3d.utility.Vector3dVector(voxel_crop)
    final_crop, ind = pcd_crop.remove_statistical_outlier(nb_neighbors=20, std_ratio=0.25)
    final_crop, ind = final_crop.remove_radius_outlier(nb_points=10, radius=0.05)
    if len(final_crop.points):
        bbox = final_crop.get_oriented_bounding_box()
        print(bbox.get_center())
        bbox.color = (1, 0, 0)
        # o3d.visualization.draw_geometries([pcd, bbox])
        data_json['figures'].append({
                    "object": 'human',
                    "geometry": {
                        "position": dict(zip(['x', 'y', 'z'], bbox.get_center())),
                        "rotation": {
                            "x": 0,
                            "y": 0,
                            "z": 0
                        },
                        "dimensions": dict(zip(['x', 'y', 'z'], bbox.get_center() / 2))
                    },
                    "door": 'open'
                })
    else:
        data_json['figures'].append({"door": "open"})
    return data_json



# def camera_analyse(cameras: list):
    

@router.post("/start-analysis")
def start_analysis() :
    """
    Запуск анализа с tof камер.
    """
    cameras = get_cameras_data_from_db()
        
    return [{}for camera in cameras()]



