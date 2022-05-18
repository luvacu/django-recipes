from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class IngredientDTO:
    name: str


@dataclass(frozen=True)
class RecipeDTO:
    id: str
    name: str
    description: str
    ingredients: List[IngredientDTO]
