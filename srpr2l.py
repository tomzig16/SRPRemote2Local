import argparse
import src.HelpMessages as HelpMes
import src.LocalDataLoader as ldloader

if __name__ == "__main__":
    mainParser = argparse.ArgumentParser(description=HelpMes.appDescription)
    mainParser.add_argument("--setup", nargs=1, help=HelpMes.setSrpPath, default=None)
    mainParser.add_argument("project_path", nargs="?", help=HelpMes.projectPath)
    mainParser.add_argument("srp_path", nargs="?", help=HelpMes.srpPath)
    args = mainParser.parse_args(["arg1", "E:\\work\\srp"])
    print(args)
    if args.setup != None:
        print("Setup is not none")
    else:
        ldloader.ReplaceManifestJson(args.project_path, args.srp_path)
