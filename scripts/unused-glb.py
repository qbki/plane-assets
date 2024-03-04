#!/usr/bin/env python
from utils.consts import *
from utils.file_names import *
from utils.print import print_list

entities_file_path = os.path.join(LEVELS_DIR, "entities.json")
models_full_pathes = retrieve_models_full_pathes(entities_file_path)
files_in_directory = retrieve_files_in_directory(MODELS_DIR)

unsed_files = [x for x in files_in_directory if x not in models_full_pathes]
print_list(unsed_files)
