from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


from src.core.__seedwork.domain.entities import Entity

@dataclass(kw_only=True, frozen=True, slots=True) 
class Category(Entity):

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )

    def _set(self, attr: str, value: str):
        object.__setattr__(self, attr, value)

    def update(self, name: str, description: Optional[str] = None):
        self._set('name', name)
        self._set('description', description)


    def activate(self):
        self._set('is_active',True)

    def deactivate(self):
        self._set('is_active',False)
