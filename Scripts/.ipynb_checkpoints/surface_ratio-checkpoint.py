import pymesh
import os

ratio_list = []
ply_list = []
path = 'output/all_feat_3l/pred_surfaces'
with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".ply") and entry.is_file():

          mesh = pymesh.load_mesh('entry')
          mesh.add_attribute('vertex_area')
          areas = mesh.get_attribute('vertex_area')

          mesh.add_attribute("vertex_iface")
          iareas = mesh.get_attribute("vertex_iface")
          iareas = mesh.get_attribute("vertex_iface")

          ratio = sum(iareas)/sum(areas)
          ratio_list.append(ratio)
          ply_list.append(entry)

complete_list = list(zip(ply_list, ratio_list))
with open('ply_patch_ratio.txt', 'w') as filehandle:
    for listitem in complete_list:
        filehandle.write('%s\n' % listitem)
