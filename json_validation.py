import json
from pathlib import Path

from pydantic import ValidationError

from product_models import ProductRequest


def load_and_validate_product(file_path: str) -> dict:
    """Load a JSON file and validate it as a ProductRequest."""

    path = Path(file_path)

    try:
        raw_data = path.read_text(encoding="utf-8")
        payload = json.loads(raw_data)

    except FileNotFoundError:
        return {
            "success": False,
            "error_type": "file_not_found",
            "errors": [f"File not found: {file_path}"],
        }

    except json.JSONDecodeError as error:
        return {
            "success": False,
            "error_type": "invalid_json",
            "errors": [
                f"Invalid JSON at line {error.lineno}, column {error.colno}: "
                f"{error.msg}"
            ],
        }

    try:
        product = ProductRequest.model_validate(payload)

    except ValidationError as error:
        return {
            "success": False,
            "error_type": "validation_error",
            "errors": [
                {
                    "field": detail["loc"],
                    "message": detail["msg"],
                }
                for detail in error.errors()
            ],
        }

    return {
        "success": True,
        "data": product.model_dump(),
    }


if __name__ == "__main__":
    test_files = [
        "valid_product.json",
        "invalid_product.json",
        "malformed_product.json",
    ]

    for file_name in test_files:
        print(f"\nTesting: {file_name}")
        result = load_and_validate_product(file_name)
        print(json.dumps(result, indent=2))