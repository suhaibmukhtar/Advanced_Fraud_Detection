from setuptools import find_packages,setup
from typing import List

def get_requirements(file:str)->List[str]:
    """
    This function will return the list of requirements i.e. libraries required
    """
    requirements=[]
    HYPHEN_DOT_E="-e ."
    with open(file,'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

#specifying parameters for setup
setup(
    name="Advanced_Credit_Card_Fraud_Detection",
    version="1.0",
    author="Suhaib Mukhtar",
    author_email="suhaibmukhtar2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)