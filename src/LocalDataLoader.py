import os
import json

resourcesFolderName = "./res"
jsonDataFileName = "LocalSRPParams.json"
scriptPath = os.path.dirname(__file__)
resourcesFolderPath = os.path.join(scriptPath, resourcesFolderName)
resourcesFilePath = os.path.realpath(os.path.join(resourcesFolderPath, jsonDataFileName))


def GetLocalSRPPath():
    try:
        localSRPPath = None
        with open(resourcesFilePath) as jsonFile:
            localSRPData = json.load(jsonFile)
            localSRPPath = localSRPData["srp_path"]
        return localSRPPath
    except (FileNotFoundError, KeyError):
        return None

def GenerateSRPPackagesPaths(srpPath):
    data = {
        "srp_path": srpPath
    }
    for file in os.listdir(srpPath):
        if "com.unity." not in file:
            continue
        data[file] = os.path.realpath(os.path.join(srpPath, file))
    return data



def GetProjectPackageManifestData(srpPath):
    manifestPath = "Packages/manifest.json" # Unity searches for manifest exactly there (inside project folder)
    fullManifestPath =  os.path.realpath(os.path.join(srpPath, manifestPath))
    try:
        manifestData = None
        with open(fullManifestPath) as jsonFile:
            pass
    except:
        pass


def ReplaceManifestJson(projectPath, srpPath):
    localSRPData = None
    if srpPath != None:
        if os.path.exists(srpPath) == False:
            print("Given SRP path does not exist.\nCheck given SRP path and try again...")
            print("Or run without it to use default local SRP path")
            return
        localSrpPath = os.path.realpath(srpPath)
        localSRPData = GenerateSRPPackagesPaths(localSrpPath)
    else:
        localSrpPath = GetLocalSRPPath()
        if localSrpPath == None:
            if srpPath == None:
                print("No SRP path was given. Please run command with --setup or give SRP path alongside project path.")
                return
    
    # Else if local srp path is set correctly
    srpJson = GetProjectPackageManifestData(localSrpPath)

            
