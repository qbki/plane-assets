import json
import os
from typing import Any, List

from utils.consts import ROOT_DIR

def retrieve_models_pathes(data: Any) -> List[str]:
  acc = []
  if isinstance(data, str) and data.endswith(".glb"):
    acc.append(data)
  if isinstance(data, dict):
    for value in data.values():
      acc += retrieve_models_pathes(value)
  return acc

def retrieve_models_full_pathes(filepath: str) -> List[str]:
  file_handle = open(filepath)
  json_root = json.load(file_handle)
  result = []
  for file_name in retrieve_models_pathes(json_root):
    full_path = os.path.normpath(os.path.join(ROOT_DIR, file_name))
    result.append(full_path)
  return result

def retrieve_files_in_directory(dirpath: str) -> List[str]:
  directory = os.listdir(dirpath)
  result = []
  for file_name in directory:
    full_path = os.path.join(dirpath, file_name)
    if os.path.isfile(full_path):
      result.append(full_path)
  return result
