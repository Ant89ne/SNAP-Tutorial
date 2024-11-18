import os
import tqdm

cropDataFolder = '/home/bralet/Bureau/miniworkshopsnap/Data/croppedData/'
orthoGraph = '/home/bralet/Bureau/miniworkshopsnap/Correction/graphs/graph_orthorectification_param.xml' #myGraph'+site+'CalibParam.xml'
outputFolder = '/home/bralet/Bureau/miniworkshopsnap/Data/orthorectifiedData/'
snapExecutablePath = '/opt/snapSentinel/bin/gpt'

listFiles = [f for f in os.listdir(cropDataFolder) if os.path.isfile(os.path.join(cropDataFolder,f)) and f.endswith('.tif')]

if not os.path.isdir(outputFolder):
    os.mkdir(outputFolder)

params = {}

# Calibration, subset and DEM registration - SNAP
for f in tqdm.tqdm(listFiles) :
    params["inputFile"] = cropDataFolder + f
    params["outputFile"] = outputFolder + f

    paramLine = ""
    for k in params.keys():
        paramLine += f" -P{k}={params[k]}"
    
    os.system(f"{snapExecutablePath} {orthoGraph} {paramLine}")
