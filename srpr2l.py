import argparse
import src.HelpMessages as HelpMes
from src.LocalProjectManager import printActions, AddLocalSRPToProject
from src.LocalSRPManager import SetupLocalSRP 

if __name__ == "__main__":
    mainParser = argparse.ArgumentParser(description=HelpMes.appDescription)
    mainParser.add_argument("--setup", nargs=1, help=HelpMes.setSrpPath, default=None)
    mainParser.add_argument("project_path", nargs="?", help=HelpMes.projectPath)
    mainParser.add_argument("srp_path", nargs="?", help=HelpMes.srpPath)
    mainParser.add_argument("-pa", "--print-actions", action="store_true", help=HelpMes.printActions)
    args = mainParser.parse_args(["--setup", "E:\\work\\srp"])
    print(args)
    if args.setup != None:
        SetupLocalSRP(args.setup[0])
    else:
        printActions = args.print_actions
        AddLocalSRPToProject(args.project_path, args.srp_path)
