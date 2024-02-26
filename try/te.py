import os
import requests
import zipfile
from distutils.dir_util import copy_tree


local_folder = os.path.abspath(os.path.dirname(__file__))
print(local_folder)