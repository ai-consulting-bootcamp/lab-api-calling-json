from pydantic import BaseModel, Field, ValidationError, field_validator


class SimpleProduct(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(default=1, gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Name must not be blank")

        return value


print("1. Valid product:")

try:
    product = SimpleProduct(
        name="Widget",
        price=10.99,
        quantity=5,
    )

    print("Valid:", product.model_dump())

except ValidationError as error:
    print("Unexpected error:", error)


print("\n2. Invalid product:")

try:
    invalid_product = SimpleProduct(
        name="",
        price=-10.99,
        quantity=0,
    )

    print(invalid_product)

except ValidationError as error:
    print("Expected validation error:")
    for detail in error.errors():
        print(f"- Field: {detail['loc'][0]}, Error: {detail['msg']}")


print("\nSimple Pydantic model test completed.")