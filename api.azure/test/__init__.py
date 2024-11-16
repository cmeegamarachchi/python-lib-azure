import json
import azure.functions as func  # type: ignore

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../core_lib'))
sys.path.append(os.path.join(os.getcwd(),"core_lib"))

# Import the Utility class
from utility import Utility

def main(req: func.HttpRequest) -> func.HttpResponse:
    utility = Utility()
    name = req.params.get('name')

    payload = {
        "message": utility.generate_greeting(name),
    }

    return func.HttpResponse(json.dumps(payload), mimetype="application/json")