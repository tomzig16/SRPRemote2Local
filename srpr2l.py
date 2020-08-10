import argparse
import src.HelpMessages as HelpMes

def ReplaceManifestJson(projectPath, srpPath):
    print("Test func was hit!\n")
    print(srpPath)


if __name__ == "__main__":
    mainParser = argparse.ArgumentParser(description=HelpMes.appDescription)
    mainParser.add_argument("--setup", nargs=1, help=HelpMes.setSrpPath, default=None)
    mainParser.add_argument("project_path", nargs="?", help="project path should be here")
    mainParser.add_argument("srp_path", nargs="?", help="srp path should be here")
    args = mainParser.parse_args(["arg1"])
    print(args)
    if args.setup != None:
        print("Setup is not none")
    else:
        ReplaceManifestJson(args.project_path, args.srp_path)