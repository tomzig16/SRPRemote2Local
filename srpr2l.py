import argparse
import src.HelpMessages as HelpMes

def TestFunc(args):
    print("Test func was hit!\n")
    print(args)


mainParser = argparse.ArgumentParser(description=HelpMes.appDescription)
commandGroups = mainParser.add_subparsers(title="commandGroups")

installationSubParser = commandGroups.add_parser("--setup", help=HelpMes.setSrpPath)
installationSubParser.set_defaults(func=TestFunc)
installationSubParser.add_argument("srp_path", nargs=1, help=HelpMes.setSrpPath)

executionSubParser = commandGroups.add_parser("-e", help="launch (optional)")
mainParser.add_argument("project_path", nargs="?", help="project path should be here")
mainParser.add_argument("srp_path", nargs="?", help="srp path should be here")


mainParser.print_help()


