import os,sys
from pathlib import Path
import logging


while True:
    project_name=input("Enter your projrct name :") 
    if project_name !="":
        break
    
list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/Components/__init__.py",
    f"{project_name}/Config/__init__.py",
    f"{project_name}/Constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/Exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yml",
    "schema.yml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"]

for file_path in list_of_files: 
    file_path = Path(file_path)
    file_dir, filename= os.path.split(file_path)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        
    if not os.path.exists(file_path) or (os.path.getsize(file_path)==0):
        with open( file_path, "w") as f:
            pass
        
    else:
        logging.info(f"file is already present at : {file_path}")
    