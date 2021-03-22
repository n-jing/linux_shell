#! /home/jing/Downloads/software/ParaView-5.8.0-MPI-Linux-Python3.7-64bit/bin/pvpython

import sys
import os

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


path = sys.argv[1]
ext = os.path.splitext(path)[1]
if ext == ".vtk":
    cubevtk = LegacyVTKReader(FileNames=os.path.abspath(path))
elif ext == ".obj":
    cubevtk = WavefrontOBJReader(FileName=os.path.abspath(path))
elif ext == ".stl":
    cubevtk = STLReader(FileNames=os.path.abspath(path))
else :
    print("only obj, stl and vtk are supported")
    sys.exit(1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2043, 820]

# get layout
layout1 = GetLayout()

# show data in view
cubevtkDisplay = Show(cubevtk, renderView1)
print(cubevtk.GetDataInformation().GetNumberOfCells())
