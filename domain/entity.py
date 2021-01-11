from dataclasses import asdict, dataclass


@dataclass
class User:
    id: str
    name: str
    age: int

    def asdict(self):
        return asdict(self)