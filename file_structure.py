 
import os

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the subdirectories
DATA_DIR = os.path.join(BASE_DIR, "data")
API_DIR = os.path.join(BASE_DIR, "api")

# Create the directories if they don't exist
for dir in [DATA_DIR, API_DIR]:
    if not os.path.exists(dir):
        os.makedirs(dir)

# Create the files in the data directory
with open(os.path.join(DATA_DIR, "raw_data.txt"), 'w') as f:
    pass

with open(os.path.join(DATA_DIR, "processed_data.txt"), 'w') as f:
    pass

# Create the files in the api directory
with open(os.path.join(API_DIR, "main.py"), 'w') as f:
    f.write('# FastAPI app code goes here')

with open(os.path.join(API_DIR, "requirements.txt"), 'w') as f:
    f.write('fastapi\n uvicorn\n')

print("Project structure created successfully.")
