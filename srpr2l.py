import argparse
import src.HelpMessages as HelpMes
import src.LocalProjectManager as ldloader

if __name__ == "__main__":
    mainParser = argparse.ArgumentParser(description=HelpMes.appDescription)
    mainParser.add_argument("--setup", nargs=1, help=HelpMes.setSrpPath, default=None)
    mainParser.add_argument("project_path", nargs="?", help=HelpMes.projectPath)
    mainParser.add_argument("srp_path", nargs="?", help=HelpMes.srpPath)
    mainParser.add_argument("-pa", "--print-actions", action="store_true", help=HelpMes.printActions)
    args = mainParser.parse_args(["E:/work/unity_proj/emptyproj", "E:\\work\\srp", "-pa"])
    print(args)
    if args.setup != None:
        print("Setup is not none")
    else:
        ldloader.printActions = args.print_actions
        ldloader.AddLocalSRPToProject(args.project_path, args.srp_path)
