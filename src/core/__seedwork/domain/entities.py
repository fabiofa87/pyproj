from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import Any

from src.core.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):
    unique_entity_id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId())

    @property
    def id(self):
        return str(self.unique_entity_id.id)
    
    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop('unique_entity_id')
        entity_dict['id'] = self.id
        return entity_dict

