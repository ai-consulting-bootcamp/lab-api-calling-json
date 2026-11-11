import json

from chatgpt_workflow import process_product_request


def handle_client_request(
    payload: object,
    request_id: str = "request-1",
) -> dict:
    """
    Validate and process one client request.

    The response always has the same structure:
    success, request_id, data, and error.
    """

    try:
        result = process_product_request(payload)

    except Exception as error:
        return {
            "success": False,
            "request_id": request_id,
            "data": None,
            "error": {
                "type": "unexpected_error",
                "message": str(error),
            },
        }

    if result.get("success") is True:
        return {
            "success": True,
            "request_id": request_id,
            "data": {
                "product": result.get("validated_product"),
                "listing": result.get("listing"),
            },
            "error": None,
        }

    return {
        "success": False,
        "request_id": request_id,
        "data": None,
        "error": {
            "type": result.get("error_type", "processing_error"),
            "stage": result.get("stage"),
            "details": result.get("errors", []),
        },
    }


if __name__ == "__main__":
    with open("invalid_product.json", encoding="utf-8") as file:
        invalid_payload = json.load(file)

    invalid_result = handle_client_request(
        invalid_payload,
        request_id="invalid-001",
    )

    print("Invalid request result:")
    print(json.dumps(invalid_result, indent=2))