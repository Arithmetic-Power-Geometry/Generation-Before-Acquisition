from dataclasses import dataclass
from typing import Callable, Any

@dataclass(frozen=True)
class ResourceVector:
    time: float = 0.0
    energy: float = 0.0
    writes: float = 0.0
    movement: float = 0.0
    comparisons: float = 0.0
    fee: float = 0.0

    def scalar(self, weights: "ResourceVector") -> float:
        return (self.time * weights.time + self.energy * weights.energy + self.writes * weights.writes + self.movement * weights.movement + self.comparisons * weights.comparisons + self.fee * weights.fee)

    def __add__(self, other: "ResourceVector") -> "ResourceVector":
        return ResourceVector(self.time + other.time, self.energy + other.energy, self.writes + other.writes, self.movement + other.movement, self.comparisons + other.comparisons, self.fee + other.fee)

@dataclass
class OracleAction:
    name: str
    cost: ResourceVector
    apply: Callable[[list[Any]], Any]
