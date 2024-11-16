import json
import azure.functions as func  # type: ignore

import sys
import os
from pathlib import Path

# sys.path.append(os.path.join(os.path.dirname(__file__), '../../core_lib'))

# this code is required to import the utility class from the core.lib when running in azure
# sys.path.append(os.path.join(os.path.dirname(__file__), 'core_lib'))

# Import the Utility class
from core_lib.utility import Utility

def get_directory_structure(folder_path):
    """
    Recursively retrieves the directory structure as a nested dictionary.
    """
    dir_structure = {}
    for root, dirs, files in os.walk(folder_path):
        # Get the relative path for nested structure
        relative_path = os.path.relpath(root, folder_path)
        # Replace '.' with the root folder's name for readability
        if relative_path == ".":
            relative_path = os.path.basename(folder_path)
        
        # Add files and subdirectories to the structure
        dir_structure[relative_path] = {
            "folders": dirs,
            "files": files
        }
    return dir_structure

def main(req: func.HttpRequest) -> func.HttpResponse:
    utility = Utility()
    
    payload = {
        "current_directory_1": os.getcwd(),
        "directory_structure_1": get_directory_structure(os.getcwd()),
        "current_directory_2": os.path.dirname(__file__),
        "directory_structure_2": get_directory_structure(os.path.dirname(__file__)),
        "parent_directory_1": os.path.join(os.getcwd(),".."),
        "parent_structure_1": get_directory_structure(os.path.join(os.getcwd(),"..")),
        "parent_directory_2": os.path.join(os.path.dirname(__file__), ".."),
        "parent_structure_2": get_directory_structure(os.path.join(os.path.dirname(__file__), "..")),
        "parent_directory_3": os.path.join(Path(__file__).resolve().parent),
        "parent_structure_3": get_directory_structure(Path(__file__).resolve().parent),
        "sub_directory_2": os.path.join(os.path.dirname(__file__), "core_lib"),
        "sub_structure_2": get_directory_structure(os.path.join(os.path.dirname(__file__), "core_lib")),
    }

    return func.HttpResponse(json.dumps(payload), mimetype="application/json")