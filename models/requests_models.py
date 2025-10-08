from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CourierRequest:
    login: str
    password: str
    firstName: str
    
@dataclass
class OrderRequest:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    address: Optional[str] = None
    metroStation: Optional[int] = None
    phone: Optional[str] = None
    rentTime: Optional[int] = None
    deliveryDate: Optional[str] = None
    comment: Optional[str] = None
    color: Optional[List[str]] = field(default_factory=list)

    
    