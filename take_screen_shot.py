#! /home/jing/Downloads/software/ParaView-5.8.0-RC2-MPI-Linux-Python3.7-64bit/bin/pvpython

import os
import sys
import argparse
import time
import re
# parser = argparse.ArgumentParser(description='take screen shot of model through paraview, only obj and vtk are supported.')

# parser.add_argument('-i','--input', help='input directory',type = str)
# parser.add_argument('-o','--output', help='output directory',type = str)

# args = parser.parse_args()

from paraview.simple import *
#### disable automatic camera reset on 'Show'
# paraview.simple._DisableFirstRenderCameraReset()


def file_comp(f1) :
    x = re.findall("\d+", f1)
    if len(x) == 0 :
        return 0
    return int(x[0])

path = sys.argv[1]
print(path)
path_list=os.listdir(path)
path_list.sort(key=file_comp) #sort
for files in path_list:
    f_model = files
    ext = os.path.splitext(f_model)[1]
    if ext == ".vtk":
        cubevtk = LegacyVTKReader(FileNames=os.path.abspath(f_model))
    elif ext == ".obj":
        cubevtk = WavefrontOBJReader(FileName=os.path.abspath(f_model))
    elif ext == ".stl":
        cubevtk = STLReader(FileNames=os.path.abspath(f_model))
    else :
        print("only obj, stl and vtk are supported")
        continue

            
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    renderView1.ViewSize = [1051, 755]

    # show data in view
    cubevtkDisplay = Show(cubevtk, renderView1)
    # reset view to fit data
    renderView1.ResetCamera()
        
    # get the material library
    materialLibrary1 = GetMaterialLibrary()
    # update the view to ensure updated data information
    renderView1.Update()
        
    # Hide orientation axes
    renderView1.OrientationAxesVisibility = 0
        
    # change representation type
    cubevtkDisplay.SetRepresentationType('Surface With Edges')

    # renderView1.ResetCamera()
    # RenderAllViews()
    # time.sleep(0.2)

    renderView1.CameraPosition = [34.337806363565186, 32.680307398326256, 57.27025020794612]
    renderView1.CameraFocalPoint = [-4.076712180910736e-15, 2.1551788703431267e-15, 9.99999982176814]
    renderView1.CameraViewUp = [-0.3459576989339217, 0.8703582394371489, -0.3504137634172106]
    renderView1.CameraParallelScale = 17.326507561118422
    renderView1.ResetCamera()
    RenderAllViews()
    # time.sleep(0.2)
    png_name = path + "/screen_shot/" + f_model + ".png"
    SaveScreenshot(png_name, renderView1, ImageResolution=[1051, 755], TransparentBackground=0)
    Delete(cubevtk)
    del cubevtk
