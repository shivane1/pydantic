import pytest
from pydantic import BaseModel, ValidationError

class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address | None = None

def test_optional_nested_model_missing_required_field():
    data = {
        "name": "Alice",
        "address": {
            "street": "Main Street"
        }
    }

    with pytest.raises(ValidationError) as exc_info:
        User(**data)

    errors = exc_info.value.errors()
    assert any("address.city" in str(error["loc"]) for error in errors)
