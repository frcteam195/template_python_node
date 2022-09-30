## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['template_python_node'],  #packages=['template_python_node', 'template_python_node.subnode'],
    package_dir={'': 'src'})

setup(**setup_args)