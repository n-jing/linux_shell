#! /home/jing/Downloads/software/ParaView-5.8.0-MPI-Linux-Python3.7-64bit/bin/pvbatch

import os
import sys
import argparse
import time
# parser = argparse.ArgumentParser(description='take screen shot of model through paraview, only obj and vtk are supported.')

# parser.add_argument('-i','--input', help='input directory',type = str)
# parser.add_argument('-o','--output', help='output directory',type = str)

# args = parser.parse_args()

from paraview.simple import *
#### disable automatic camera reset on 'Show'
# paraview.simple._DisableFirstRenderCameraReset()


path = sys.argv[1]
print(path)
for root, dirs, files in os.walk(path):
    for file_ in files:
        f_model = os.path.join(root, file_)
        print(f_model)
        ext = os.path.splitext(f_model)[1]
        if ext == ".vtk":
            continue
        elif ext == ".obj":
            cubevtk = WavefrontOBJReader(FileName=os.path.abspath(f_model))
        elif ext == ".stl":
            cubevtk = STLReader(FileNames=os.path.abspath(f_model))
        else :
            print("only obj, stl and vtk are supported")
            continue

        vtk_path = os.path.splitext(f_model)[0] + ".vtk"
        print(vtk_path)
        SaveData(vtk_path, proxy=cubevtk, CellDataArrays=['GroupIds'],
                 FileType='Ascii')            

        Delete(cubevtk)

os._exit(0)        
