import azure.functions as func  # type: ignore

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    return func.HttpResponse(f"Hello {name}")