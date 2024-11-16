import azure.functions as func  # type: ignore

import sys
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), '../../core_lib'))

# this code is required to import the utility class from the core.lib when running in azure
# sys.path.append(os.path.join(os.path.dirname(__file__), 'core_lib'))

# Import the Utility class
from core_lib.utility import Utility

def main(req: func.HttpRequest) -> func.HttpResponse:
    utility = Utility()
    name = req.params.get("name")
    message = utility.generate_greeting(name)
    return func.HttpResponse(f"Hello {message}")