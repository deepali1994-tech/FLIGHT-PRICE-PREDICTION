from setuptools import find_packages, setup

from typing import List

HYPEN="-e."
def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path, "r") as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','')for req in requirements]
            
        
    if HYPEN in requirements:
        requirements.remove(HYPEN)


    return requirements

setup(
    name="flight",
    version="1.0", 
    author="Deepali",
    author_email="deepalikashyap748@gmail.com",
    packages=find_packages(),
    description="A package for predicting flight prices",
    install_requires=get_requirements("requirements.txt")
        
)