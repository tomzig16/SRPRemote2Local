import os
import json

resourcesFolderName = "./res"
jsonDataFileName = "LocalSRPParams.json"
scriptPath = os.path.dirname(__file__)
resourcesFolderPath = os.path.join(scriptPath, resourcesFolderName)
resourcesFilePath = os.path.realpath(os.path.join(resourcesFolderPath, jsonDataFileName))

def GetLocalSRPData():
    try:
        with open(resourcesFilePath) as jsonFile: 
            return json.load(jsonFile)
    except FileNotFoundError:
        return None

def SaveLocalSRPData(srpData):
    with open(resourcesFilePath, "w") as localSrpDataFile:
        json.dump(srpData, localSrpDataFile)

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


def SetupLocalSRP(srpPath):
    if os.path.exists(srpPath) == False:
        print("Given SRP path does not exist.\nCheck SRP path and try again...")
        return
    srpData = GenerateSRPPackagesPaths(srpPath)
    SaveLocalSRPData(srpData)
    print("Local SRP data is set up and the tool is ready to be used.")
    