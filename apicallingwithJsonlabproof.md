# Lab Proof — API Calling with JSON

## Reviewer entry point

This document provides the proof for the JSON/Pydantic validation lab. The workflow extends the product-listing generator by validating incoming product data before calling the ChatGPT API, validating generated output, processing multiple requests, and returning consistent client responses.

## Code / workflow export

The complete workflow is in [`APICallingwithJson.ipynb`](APICallingwithJson.ipynb).

Supporting files:

- Valid input: [`valid_product.json`](valid_product.json)
- Invalid input: [`invalid_product.json`](invalid_product.json)
- Batch input: [`product_requests.json`](product_requests.json)

No API key or environment file is included.

## Run and input

The notebook defines a Pydantic `ProductRequest` model with these rules:

- `name` is required.
- `category` is required.
- `price` is optional.
- When provided, `price` must be positive.

The single-request inputs are:

### Valid request

[`valid_product.json`](valid_product.json)

```json
{
  "name": "Navy Blue Shirt",
  "category": "Apparel",
  "price": 29.99
}
```

### Invalid request

[`invalid_product.json`](invalid_product.json)

```json
{
  "name": "Navy Blue Shirt",
  "category": "Apparel",
  "price": -10
}
```

The batch run loads [`product_requests.json`](product_requests.json), which contains three requests: two valid requests and one invalid negative-price request.

## Evidence produced

The saved notebook outputs show:

- Pydantic installation and basic validation succeeded.
- Valid product data was accepted.
- Negative price data was rejected with `Price must be positive`.
- Missing required data was rejected with `Field required`.
- The valid JSON file was accepted.
- The invalid JSON file was rejected before API processing.
- Invalid data was skipped before the ChatGPT API call.
- A generated product listing passed output validation with `title`, `description`, `category`, `features`, and `keywords` fields.
- The batch loaded 3 requests, accepted 2, rejected 1, and continued processing.
- The client request handler returned structured success and error responses.

## Final output

The final batch summary produced by the notebook was:

```json
{
  "total_requests": 3,
  "listings_generated": 2,
  "rejected_before_api": 1,
  "generation_failures": 0,
  "validation_errors": [
    {
      "request_number": 2,
      "reason": "Value error, Price must be positive"
    }
  ],
  "generation_errors": []
}
```

The handler produced:

- For the invalid request: `success: false`, no listing, and a validation error.
- For the valid request: `success: true`, a validated Navy Blue Shirt listing, and `error: null`.

These results are preserved in the output cells of [`APICallingwithJson.ipynb`](APICallingwithJson.ipynb).

## Failure or limitation

The notebook produced deprecation warnings because it uses the Pydantic v1-style `@validator` decorator with Pydantic 2.13.4. The validation worked, but future maintenance should migrate these validators to the Pydantic v2 `@field_validator` style.

The API-processing portion also depends on an available OpenAI API key and network access, so the notebook does not provide an offline mock for API failures.

