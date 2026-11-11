import json
from pathlib import Path

from chatgpt_workflow import process_product_request


def process_batch(file_path: str) -> dict:
    """Process multiple product requests without stopping on errors."""

    path = Path(file_path)
    payloads = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(payloads, list):
        raise ValueError("Batch input must be a JSON list")

    results = []

    for request_number, payload in enumerate(payloads, start=1):
        result = process_product_request(payload)

        results.append(
            {
                "request_number": request_number,
                **result,
            }
        )

    successful = sum(
        1 for result in results if result.get("success") is True
    )

    return {
        "total_requests": len(results),
        "successful_requests": successful,
        "failed_requests": len(results) - successful,
        "results": results,
    }


if __name__ == "__main__":
    batch_result = process_batch("batch_requests.json")
    print(json.dumps(batch_result, indent=2))