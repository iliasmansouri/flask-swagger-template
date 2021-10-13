import os

SPECIFICATION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs")
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
GPU_MEMORY_LIMIT = int(os.environ.get("GPU_MEMORY_LIMIT", 2048))
