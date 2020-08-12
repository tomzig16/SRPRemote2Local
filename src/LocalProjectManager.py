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



def GetProjectPackageManifestData(projectPath):
    manifestPath = "Packages/manifest.json" # Unity searches for manifest exactly there (inside project folder)
    fullManifestPath = os.path.realpath(os.path.join(projectPath, manifestPath))
    try:
        with open(fullManifestPath) as jsonFile:
            return json.load(jsonFile)
    except FileNotFoundError:
        return None


def UpdateProjectManifestJson(projectJson, localSRPData):
    for key, val in localSRPData.items():
        projectJson["dependencies"][key] = val

def SaveNewProjectManifest(projectPath, newManifest):
    manifestPath = "Packages/manifest.json"
    fullManifestPath = os.path.realpath(os.path.join(projectPath, manifestPath))
    with open(fullManifestPath, "w") as projMan:
        json.dump(newManifest, projMan)

def AddLocalSRPToProject(projectPath, srpPath):
    localSRPData = None
    # First check if custom SRP path is given and valid
    # if it is given it is higher priority to be used than local saved SRP folder 
    # (this is in case we have 2 different branches at once etc.)
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
    
    # Else - local srp path is set correctly
    projectManifest = GetProjectPackageManifestData(projectPath)
    if projectManifest == None:
        print("Packages/manifest.json was not found. Make sure given project path (destination) is Unity project.")
        return
    
    UpdateProjectManifestJson(projectManifest, localSRPData)
    SaveNewProjectManifest(projectPath, projectManifest)

    print("Done")


            
