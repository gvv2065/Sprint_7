from dataclasses import dataclass

@dataclass
class CourierRequest:
    login: str
    password: str
    firstName: str