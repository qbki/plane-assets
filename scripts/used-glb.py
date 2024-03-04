#!/usr/bin/env python
import os

from utils.consts import *
from utils.file_names import *
from utils.print import print_list

entities_file_path = os.path.join(ROOT_DIR, "levels", "entities.json")
models_full_pathes = retrieve_models_full_pathes(entities_file_path)

print_list(models_full_pathes)
