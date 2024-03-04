import os;

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", ".."))
MODELS_DIR = os.path.join(ROOT_DIR, "models")
LEVELS_DIR = os.path.join(ROOT_DIR, "levels")
CACHE_DIR = os.path.join(ROOT_DIR, "cache")
