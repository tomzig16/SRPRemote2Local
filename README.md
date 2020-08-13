# SRPRemote2Local
SRPRemote 2 Local is a repository with a script that essentially updates Unity project packages manifest.json file contents (in effect replacing or adding) to include local SRP paths. This is usually needed in order to debug localally and change values inside the existing SRP scripts.

# Instalation
This application uses several pip requirements which are listed in `requirements.txt` file. Easiest way to install is to call pip install with -r argument as shown below.
```
pip install -r ./requirements.txt
```
I suggest adding path to this application to path global variable so it can be accessed from command line without navigating to this folder first.

# Usage

First you have to save path to SRP folder in SRPR2L by calling command below
```
srpr2l.py --setup Path/To/SRP
```
Once you setup it that way you can use the tool by simply calling `srpr2l.py [path/to/project]` as shown below
```
srpr2l.py path/to/unity/project
```
Optionally, you can give another SRP folder (in case you have several copies with different versions) or additional parameter `-pa` (`--print-actions`) parameter which will print more information on what application is doing.

# License

[MIT](LICENSE)
