import os
import sys

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Print the system path
print("System Path:")
for path in sys.path:
    print(path)

# Add the current directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current Directory:", current_dir)
sys.path.append(current_dir)

# Attempt to import the ChemEnv module
try:
    from environment.ChemEnv import ChemEnv
    print("Import successful!")
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
