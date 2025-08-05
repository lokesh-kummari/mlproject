from setuptools import setup, find_packages
HYPEN_E_DOT='-e .'

def get_req(file_name):
    """Reads a requirements file and returns a list of requirements."""
    with open(file_name, 'r') as file:
       req = file.read().splitlines()
       req = [i.replace('\n', '') for i in req if i and not i.startswith('#')]
    if HYPEN_E_DOT in req:
        req.remove(HYPEN_E_DOT)
    return req

setup(
    name='mlproject',
    version='0.1.0',
    author='Lokesh Kummari',
    author_email='klokesh5401@gmail.com',
    packages=find_packages(),
    install_requires=[
        get_req('requirements.txt'),
    ]
)