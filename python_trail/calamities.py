from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List
from run_func import roll_dice

@dataclass
class Calamity:
    name: str
    desc: str
    resolve: str
