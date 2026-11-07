# API Calling with JSON — Evidence

This file is the entry point for the reviewer. The complete workflow is in the
step-by-step notebook [`product_generator.ipynb`](product_generator.ipynb).

## Setup

The notebook uses Pydantic for JSON validation. The required packages are listed
in [`requirements.txt`](requirements.txt), and Pydantic was installed in the
active notebook kernel with:

```python
%pip install pydantic
```

The OpenAI API key was loaded locally from `.env` and was never hard-coded or
included in this submission.

## Workflow and input

The notebook implements the required validation pipeline:

1. Define a simple Pydantic model and test valid and invalid values.
2. Create `ProductRequest` and `ProductListing` models.
3. Validate valid and invalid JSON files.
4. Validate input before calling the ChatGPT vision API.
5. Validate the API output after processing.
6. Process a mixed batch of valid and invalid requests.
7. Provide a reusable `handle_client_request(payload)` function.
8. Save structured results and validation errors.

Example input payload:

```json
{
  "name": "Turtle Check Men Navy Blue Shirt",
  "price": 79.99,
  "category": "Apparel",
  "additional_info": "Colour: Navy Blue; Usage: Casual",
  "image_base64": "<encoded product image>"
}
```

Supporting examples are [`valid_product.json`](json_examples/valid_product.json),
[`invalid_product.json`](json_examples/invalid_product.json), and
[`batch_requests.json`](json_examples/batch_requests.json).

## Evidence and final output

The validated end-to-end request returned:

```text
Input validation: successful
API processing: successful
Output validation: successful
```

The structured final response is saved in
[`outputs/validated_request_result.json`](outputs/validated_request_result.json).
It contains a validated title, description, features, and keywords.

The mixed batch produced:

```text
Total requests: 2
Valid requests: 1
Invalid requests: 1
```

The batch evidence is saved in
[`outputs/batch_validation_summary.json`](outputs/batch_validation_summary.json).

## Error handling and limitation

The invalid request used an empty product name and a negative price. Pydantic
rejected it with clear field-level errors before any API call was made. This
demonstrates that invalid requests do not waste API calls or stop the batch.

A limitation is that valid API processing requires a configured OpenAI API key,
available credits, and network access. The API output also requires validation
because a model can occasionally return data that does not match the requested
schema.

## Reflection

- Pydantic provides automatic type checking and clear field-level errors.
- Validating input early prevents invalid data from reaching the API.
- Validating output ensures generated listings follow a predictable schema.
- Batch validation allows valid requests to continue while invalid ones are reported.
- A reusable request handler makes the workflow suitable for a future API endpoint.
