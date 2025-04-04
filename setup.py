from setuptools import setup

setup(
    name="calculadora-cientifica",
    version="3.0.0",
    author="Leonardo Medeiro - LeoMedeiros72",
    description="Uma calculadora científica avançada",
    long_description=open("README.md").read(),
    packages=["calculadora"],
    install_requires=["numpy", "matplotlib", "scipy"],
)
