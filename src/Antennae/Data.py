from dataclasses import dataclass

@dataclass
class Note:
    start: float
    duration: float
    pitch: str

@dataclass 
class Segment:
    start: float
    duration: float
    notes: list[Note]