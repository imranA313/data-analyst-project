import os

# Project name
project_name = "data_analytics_project-01"

# Folder structure
folders = [
    f"{project_name}/data/raw",
    f"{project_name}/data/processed",
    f"{project_name}/data/external",
    f"{project_name}/src",
    f"{project_name}/pipelines",
    f"{project_name}/notebooks",
    f"{project_name}/outputs/charts",
    f"{project_name}/outputs/reports",
    f"{project_name}/config",
    f"{project_name}/logs",
    f"{project_name}/tests"
]

# Files to create
files = [
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/.gitignore",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/data_loader.py",
    f"{project_name}/src/data_cleaning.py",
    f"{project_name}/src/analysis.py",
    f"{project_name}/src/visualization.py",
    f"{project_name}/src/utils.py",
    f"{project_name}/pipelines/run_pipeline.py",
    f"{project_name}/config/config.yaml"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        f.write("")  # empty file

print(f"✅ Project '{project_name}' structure created successfully!")