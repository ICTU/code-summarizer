"""Summary model class."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Summary:
    """Summary of code."""

    path: Path
    path_summary: str
    summaries: tuple[Summary, ...] = field(default_factory=tuple)
