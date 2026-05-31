from dataclasses import dataclass
from datetime import datetime

@dataclass
class MemoryRecord:
    source_id: str
    target_id: str
    summary: str
    score: int = 0
    timestamp: datetime = datetime.utcnow()
