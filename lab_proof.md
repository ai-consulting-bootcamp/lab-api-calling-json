# LAB | API Calling with JSON

## Overview

This project extends the product-listing generator with JSON validation using Pydantic.

The workflow:

1. Load a JSON request.
2. Validate the request with Pydantic.
3. Reject invalid data before making an API call.
4. Send valid product data to ChatGPT.
5. Request structured product-listing output.
6. Validate the ChatGPT response.
7. Process multiple requests in a batch.
8. Return consistent success and error responses.

## Implementation

- [Product models](product_models.py)
- [Simple Pydantic model](simple_model.py)
- [JSON validation workflow](json_validation.py)
- [ChatGPT workflow](chatgpt_workflow.py)
- [Batch processing](batch_processing.py)
- [Client request handler](request_handler.py)

## Input examples

- [Valid product JSON](valid_product.json)
- [Invalid product JSON](invalid_product.json)
- [Malformed product JSON](malformed_product.json)
- [Batch request JSON](batch_requests.json)

Example valid request:

```json
{
  "name": "Wireless Headphones",
  "price": 79.99,
  "category": "Electronics",
  "description": "Bluetooth headphones with noise cancellation",
  "additional_info": "30-hour battery life",
  "image_path": "product_images/headphones.jpg"
}
```

## Validation evidence

The validation workflow was run with:

```bash
python json_validation.py
```

Evidence:

- [JSON validation output](evidence/json_validation_output.txt)

The workflow demonstrated that valid JSON is accepted, invalid product values are rejected, and malformed JSON syntax produces a clear parsing error.

## ChatGPT workflow evidence

The validated ChatGPT workflow was run with:

```bash
python chatgpt_workflow.py
```

Evidence:

- [ChatGPT workflow output](evidence/chatgpt_workflow_output.txt)

The workflow validated the product input, called ChatGPT only after successful validation, and validated the structured listing returned by ChatGPT.

## Batch-processing evidence

The batch workflow was run with:

```bash
python batch_processing.py
```

Evidence:

- [Batch processing output](evidence/batch_processing_output.txt)

The batch contained three requests: one successful request and two invalid requests. The final result was one successful request and two failed requests. Processing continued after the invalid requests.

## Request-handler evidence

The reusable client handler was run with:

```bash
python request_handler.py
```

Evidence:

- [Request-handler output](evidence/request_handler_output.txt)

The handler returns a consistent response structure containing `success`, `request_id`, `data`, and `error` fields.

## Failure and limitation

Invalid input is rejected before the ChatGPT API call, preventing unnecessary API usage. The batch workflow makes an API call for each valid request, so larger batches may increase cost and processing time.

Structured output guarantees the response shape, but it does not guarantee perfect writing quality. Generated text may still contain wording or spacing issues and could be improved through prompt refinement or post-processing.

## Security

The API key is stored locally in `.env`. The `.env` file is excluded by `.gitignore` and is not included in the submission. No API key is included in the source code, JSON files, evidence files, or this report.

## Conclusion

This project demonstrates an end-to-end validated JSON workflow:

```text
JSON input
-> Pydantic validation
-> ChatGPT processing
-> Structured output validation
-> Batch processing
-> Consistent client response
```
