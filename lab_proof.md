# API Calling with JSON

## Implementation
[Notebook](product_validation_lab.ipynb)

Validates product inputs with Pydantic, generates listings with
OpenAI, and validates the output structure.

## Examples
- [Valid input](valid_product.json)
- [Invalid input](invalid_product.json)
- [Batch inputs](batch_requests.json)
- [Batch results](batch_results.json)

## Running
Create a local .env containing OPENAI_API_KEY.
Run the notebook setup and definition cells before the batch cells.

## Validation tested
- Positive prices required.
- Empty names and names containing only spaces rejected.
- Required output fields checked.
- Invalid requests return errors without stopping the batch.

## Limitation
Output validation checks structure and types, but cannot guarantee
that generated product claims are factually correct.