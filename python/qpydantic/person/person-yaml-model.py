# generated by datamodel-codegen:
#   filename:  person.yaml
#   timestamp: 2023-04-10T05:22:51+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field, conint


class Pet(BaseModel):
    age: Optional[int] = None
    name: Optional[str] = None


class Person(BaseModel):
    age: Optional[conint(ge=0)] = Field(None, description='Age in years.')
    comment: Optional[Any] = None
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    pets: Optional[List[Pet]] = None