from datetime import datetime
from typing import Dict
import bpy
import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from utils.consts import *

BLEND_FILE_NAME = os.path.basename(bpy.data.filepath)
GLTF_FILE_NAME = BLEND_FILE_NAME.replace(".blend", ".glb")
BLEND_FILE_CACHE_FILE_NAME = "update-time-cache-of-blend-files.json"
BLEND_FILE_CACHE_PATH = os.path.join(CACHE_DIR, BLEND_FILE_CACHE_FILE_NAME)

def load_cache() -> Dict[str, float]:
  if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)
  if not os.path.exists(BLEND_FILE_CACHE_PATH):
    return dict()
  with open(BLEND_FILE_CACHE_PATH, "r") as cache_handle:
    try:
      data = json.loads(cache_handle.read())
      if not isinstance(data, dict):
        sys.exit("Wrong format of a cache file: {}".format(BLEND_FILE_CACHE_PATH))
      return data
    except:
      sys.exit("Can't handle a cache file: {}".format(BLEND_FILE_CACHE_PATH))

def save_cache(data: Dict[str, float]) -> None:
  with open(BLEND_FILE_CACHE_PATH, "w+") as cache_handle:
    json.dump(data, cache_handle)

cache = load_cache()
blend_file_last_update = os.path.getmtime(bpy.data.filepath)
if not BLEND_FILE_NAME in cache or cache[BLEND_FILE_NAME] < blend_file_last_update:
  bpy.ops.export_scene.gltf(
    check_existing=False,
    export_apply=True,
    export_yup=False,
    filepath=os.path.join(MODELS_DIR, GLTF_FILE_NAME),
    use_visible=True,
  )
  cache[BLEND_FILE_NAME] = blend_file_last_update
  save_cache(cache)
  print("Updated {}".format(bpy.data.filepath))
else:
  print("Untouched: {}".format(bpy.data.filepath))
