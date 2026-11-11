from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator


class ProductRequest(BaseModel):
    """Validated product data received from a client JSON request."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(
        min_length=2,
        max_length=100,
        description="Product name",
    )

    price: float = Field(
        gt=0,
        le=1_000_000,
        description="Product price",
    )

    category: str = Field(
        min_length=2,
        max_length=50,
        description="Product category",
    )

    description: str | None = Field(
        default=None,
        max_length=1_000,
    )

    additional_info: str | None = Field(
        default=None,
        max_length=1_000,
    )

    image_path: str | None = Field(
        default=None,
        max_length=500,
    )

    @field_validator("name", "category")
    @classmethod
    def text_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Value must not be blank")

        return value


if __name__ == "__main__":
    valid_product = {
        "name": "Wireless Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Bluetooth headphones with noise cancellation",
        "additional_info": "30-hour battery life",
        "image_path": "product_images/headphones.jpg",
    }

    print("Valid product:")
    product = ProductRequest.model_validate(valid_product)
    print(product.model_dump())

    invalid_product = {
        "name": "",
        "price": -10,
        "category": "Electronics",
        "unexpected_field": "This should be rejected",
    }

    print("\nInvalid product:")
    try:
        ProductRequest.model_validate(invalid_product)
    except ValidationError as error:
        for detail in error.errors():
            print(f"- Field: {detail['loc']}, Error: {detail['msg']}")


class ProductListing(BaseModel):
    """Expected structured output from ChatGPT."""

    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    features: list[str] = Field(min_length=5, max_length=7)
    keywords: list[str] = Field(min_length=1)