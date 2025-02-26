from setuptools import setup, find_packages
from typing import List

requirements_path= "requirements.txt"
Hyphen_e_dot= "-e ."

def get_requiremets()-> List[str]:
    with open(requirements_path, "r") as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hyphen_e_dot  in requirements:
            requirements.remove(Hyphen_e_dot)
            
        return requirements


project_name = "ML_Modular Project"
version = "1.0"
description = "Learning Modular Coding"

author = "Mohaiminul Islam"
author_email="imniloy11@gmail.com"

setup(name=project_name,
      version= version,
      description= description,
      author= author,
      author_email=author_email,
      packages= find_packages(),
      install_requires=get_requiremets(),
     )



