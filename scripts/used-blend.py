#!/usr/bin/env python
import os
import sys

from utils.consts import *
from utils.file_names import *
from utils.print import print_list

entities_file_path = os.path.join(ROOT_DIR, "levels", "entities.json")
models_full_pathes = retrieve_models_full_pathes(entities_file_path)

blend_full_pathes = []
for model_full_path in models_full_pathes:
  filepath = model_full_path.replace(".glb", ".blend")
  filepath = filepath.replace("models", "src")
  if not os.path.exists(filepath):
    print("File not found: {}".format(filepath), file=sys.stderr)
    exit(1)
  blend_full_pathes.append(filepath)

print_list(blend_full_pathes)
