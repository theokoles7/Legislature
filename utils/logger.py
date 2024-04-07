"""Logger utilities."""

import datetime, logging, os, sys

from utils.arguments import ARGS

# Intialize logger
LOGGER = logging.getLogger("legislature")

# Set general logger level
LOGGER.setLevel(logging.getLevelName(ARGS.logging_level.upper()))

# Define console handler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.getLevelName(ARGS.logging_level.upper()))
stdout_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s: %(message)s'))
LOGGER.addHandler(stdout_handler)

# Verify that logging path exists
os.makedirs(ARGS.logging_path, exist_ok=True)

# Define file handler
file_handler = logging.FileHandler(f"{ARGS.logging_path}/legislature.log")
file_handler.setLevel(logging.getLevelName(ARGS.logging_level.upper()))
file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s: %(message)s'))
LOGGER.addHandler(file_handler)