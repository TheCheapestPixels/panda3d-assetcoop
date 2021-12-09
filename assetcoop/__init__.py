import sys
import os
from panda3d.core import get_model_path

path = os.path.join(os.path.dirname(__file__), 'bam')
get_model_path().prepend_directory(path)