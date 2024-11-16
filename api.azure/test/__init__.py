import azure.functions as func  # type: ignore

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../core.lib'))

# Import the Utility class
from utility import Utility

def main(req: func.HttpRequest) -> func.HttpResponse:
    utility = Utility()
    name = req.params.get("name")
    message = utility.generate_greeting(name)
    return func.HttpResponse(f"Hello {message}")