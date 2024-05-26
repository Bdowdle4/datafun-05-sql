# datafun-05-sql
CC5.1: Start a new Project

+ Create a GitHub project repository with a default README.md.
+ Clone your repo down to your machine. 
+ Open your project folder in VS Code (if you haven't already).
+ Add a useful .gitignore with a line for .vsode/ and .venv/ and whatever else doesn't need to go in the repo. 

## How to Install and Run the Project

### Clone Your Repo

```shell
git clone "paste_your_repo_URL_here"
```

### Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell
py -m venv .venv
.venv\Scripts\Activate
pip list
py -m pip install --upgrade pip
deactivate
```

### Create files in root folder

```shell
# Example for managing project requirements
code .
ni "requirements.txt"
```

### Add all dependencies by installing packages seperately
```shell
#Example If you have a requirements.txt list each package in this file
py -m pip install -r requirements.txt
#Example If you don't
py -m pip install jupyterlab numpy pandas matplotlib seaborn scipy
```

### Freeze Your Dependencies
This will keep the package at the version it was installed as
```shell
py -m pip freeze > requirements.txt
```

### Git add and commit 

```shell
git add .
git commit -m "initial commit"
git push origin main
```