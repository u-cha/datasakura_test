from enum import Enum
from pydantic import BaseModel, UUID4, conint
from typing import Dict, List, Optional


class GameWinType(str, Enum):
    Oin = 'oin'
    Mars = 'mars'
    Koks = 'koks'


class BoardPoint(BaseModel):
    number: conint(ge=0, le=23)
    checkers_count: conint(ge=0, le=15)
    occupied_by: Optional[UUID4] = None  # None if the point is not occupied


class Board(BaseModel):
    bar_counts: Dict[
        UUID4, int]  # UUID is the player's identifier, int - checkers count for the given player on the bar
    points: List[BoardPoint]


class GameResultInput(BaseModel):
    board: Board
    start_position: Dict[UUID4, conint(ge=0,
                                       le=23)]  # Key - UUID is the player's identifier. Value - board position number
    # starting from 0 to 23 (24 positions total)


class GameResultOutput(BaseModel):
    points: conint(ge=0)
    win_type: GameWinType
