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
python srpr2l -srp [path/to/srp]
```
Once it is added you can update any project by calling command and simply giving Unity project root folder
```
python srpr2l [path/to/unity/project]
```

# License

[MIT](LICENSE)
