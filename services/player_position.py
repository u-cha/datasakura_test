from pydantic import UUID4

from models.models import Board


class PlayerPosition:
    def __init__(self, uuid: UUID4, start_position: int, board: Board) -> None:
        self._uuid = uuid
        self._start_position = start_position
        self._board = board
        self._home_range = self._get_home_range()
        self._enemy_home_range = self._get_enemy_home_range()

    def update(self, board: Board) -> None:
        self._board = board

    @property
    def uuid(self) -> UUID4:
        return self._uuid

    @property
    def start_position(self) -> int:
        return self._start_position

    @property
    def bar_count(self) -> int:
        return self._board.bar_counts.get(self._uuid, 0)

    @property
    def checkers_count(self) -> int:
        checkers_count = 0
        for point in self._board.points:
            if point.occupied_by == self._uuid:
                checkers_count += point.checkers_count

        return checkers_count

    @property
    def checkers_at_home_count(self) -> int:
        checkers_at_home_count = 0
        for point in self._board.points:
            if point.number in self._home_range and point.occupied_by == self._uuid:
                checkers_at_home_count += point.checkers_count

        return checkers_at_home_count

    @property
    def checkers_at_enemy_home_count(self) -> int:
        checkers_at_enemy_home_count = 0
        for point in self._board.points:
            if point.number in self._enemy_home_range and point.occupied_by == self._uuid:
                checkers_at_enemy_home_count += point.checkers_count

        return checkers_at_enemy_home_count

    def _get_home_range(self):
        if self._start_position == 0:
            return range(0, 6)
        elif self._start_position == 23:
            return range(18, 24)

    def _get_enemy_home_range(self):
        if self._start_position == 23:
            return range(0, 6)
        elif self._start_position == 0:
            return range(18, 24)
