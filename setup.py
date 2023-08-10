from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='print-cores',
    version='0.0.1',
    license='MIT License',
    author='Jeferson Lopes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='jeferson.projectspy@gmail.com',
    keywords='print cores',
    description=u'Print Cores nao oficializado',
    packages=['print_cores'],
    install_requires=[])