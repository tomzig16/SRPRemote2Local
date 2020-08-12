import os
import json

resourcesFolderName = "./res"
jsonDataFileName = "LocalSRPParams.json"
scriptPath = os.path.dirname(__file__)
resourcesFolderPath = os.path.join(scriptPath, resourcesFolderName)
resourcesFilePath = os.path.realpath(os.path.join(resourcesFolderPath, jsonDataFileName))

printActions = False
class ActionType:
    INFO = "INF"
    CHANGED = "UPD"
    DELETED = "DEL"
    NEW = "NEW"



def PrintAction(actionType, actionText):
    if printActions == True:
        print(f"[{actionType}] {actionText}")

def GetLocalSRPData():
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
        "srp_path": srpPath,
        "srp_related":{}
    }
    for file in os.listdir(srpPath):
        if "com.unity." not in file:
            continue
        data["srp_related"][file] = os.path.realpath(os.path.join(srpPath, file))
    return data


def GetProjectPackageManifestData(projectManifestPath):
    try:
        with open(projectManifestPath) as jsonFile:
            return json.load(jsonFile)
    except FileNotFoundError:
        return None


def UpdateProjectManifestJson(projectJson, localSRPData):
    for key, val in localSRPData.items():
        if key in projectJson["dependencies"]:
            PrintAction(ActionType.CHANGED, f"\"{key}\":\t{projectJson['dependencies'][key]} -> {val}")
        else:
            PrintAction(ActionType.NEW, f"\"{key}\" added with value {val}")
        projectJson["dependencies"][key] = val


def SaveNewProjectManifest(projectManifestPath, newManifest):
    with open(projectManifestPath, "w") as projMan:
        json.dump(newManifest, projMan)


def AddLocalSRPToProject(projectPath, srpPath):
    PrintAction(ActionType.INFO, "Action printing is enabled")
    localSRPData = None
    # First check if custom SRP path is given and valid
    # if it is given it is higher priority to be used than local saved SRP folder 
    # (this is in case we have 2 different branches at once etc.)
    if srpPath != None:
        PrintAction(ActionType.INFO, f"Trying to use custom srp path ({srpPath})")
        if os.path.exists(srpPath) == False:
            print("Given SRP path does not exist.\nCheck given SRP path and try again...")
            print("Or run without it to use default local SRP path")
            return
        localSrpPath = os.path.realpath(srpPath)
        localSRPData = GenerateSRPPackagesPaths(localSrpPath)
    else:
        PrintAction(ActionType.INFO, "Trying to use existing local SRP info")
        localSrpPath = GetLocalSRPData()
        if localSrpPath == None:
            print("Local SRP info is not saved and custom SRP path was not given. Please run command with --setup or give SRP path alongside project path.")
            return
    
    # Else - local srp path is set correctly
    manifestPath = "Packages/manifest.json" # Unity searches for manifest exactly there (inside project folder)
    fullManifestPath = os.path.realpath(os.path.join(projectPath, manifestPath))
    PrintAction(ActionType.INFO, f"Attempting to read project package manifest ({fullManifestPath})")
    projectManifest = GetProjectPackageManifestData(fullManifestPath)
    if projectManifest == None:
        print("Packages/manifest.json was not found. Make sure given project path (destination) is Unity project.")
        return
    PrintAction(ActionType.INFO, "Updating and saving new manifest...")
    UpdateProjectManifestJson(projectManifest, localSRPData["srp_related"])
    SaveNewProjectManifest(fullManifestPath, projectManifest)
    PrintAction(ActionType.INFO, "Finished.")

    print("Done")


            
