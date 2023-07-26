import open3d as o3d
import numpy as np
import os
import sys

sys.path.append('..')

#import open3d_tutorial as o3dtut
#o3dtut.interactive = not "CI" in os.envioren 

pcd = o3d.io.read_point_cloud("../../test_data/fragment.ply")
print(pcd)
print(np.array(pcd.points))
o3d.visualization.draw_geometries([pcd])
