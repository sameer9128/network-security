from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''this function will return list of requirements'''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## read line from file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    return requirement_lst
print(get_requirements())

setup(
    name="NetworkSecurity",
    version='0.0.1',
    author='ahmad',
    author_email='sameer.engi9128@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()

)