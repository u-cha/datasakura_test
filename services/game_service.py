import typing
from uuid import uuid4

from pydantic import UUID4

from models.models import Board, GameResultInput, GameResultOutput, GameWinType
from services.player_position import PlayerPosition


def get_bar_count_for_player(player_uuid: typing.Optional[UUID4] = None):
    if not player_uuid:
        return dict()
    return {player_uuid: 1}


def get_game_result_input(board: Board, start_position: dict[uuid4, int]) -> GameResultInput:
    return GameResultInput(board=board, start_position=start_position)


loser_uuid = uuid4()

start_pos = {loser_uuid: 0,
             uuid4(): 23}


class GameResultService:

    def __init__(self, game_result_input: GameResultInput):
        self._game_board = game_result_input.board
        self._player_positions = tuple(
            PlayerPosition(uuid, start_position, self._game_board)
            for uuid, start_position in game_result_input.start_position.items()
        )

    def calculate_game_result_output(self):
        if not self._is_win_condition_satisfied():
            return

        loser_position = self._get_loser_position()

        # loser managed to get rid of at least 1 checker -> Means 'Oin' win type
        if loser_position.checkers_count < 15:
            return GameResultOutput(points=1, win_type=GameWinType.Oin)

        elif loser_position.checkers_count == 15:
            # loser has checkers at bar or at enemy home -> Means 'Koks' win type
            if loser_position.bar_count > 0 or loser_position.checkers_at_enemy_home_count > 0:
                return GameResultOutput(points=3, win_type=GameWinType.Koks)

            # loser has checkers outside home -> Means 'Mars' win type
            elif loser_position.checkers_count > loser_position.checkers_at_home_count:
                return GameResultOutput(points=2, win_type=GameWinType.Mars)

    def _is_win_condition_satisfied(self) -> bool:
        return any(player_position.checkers_count == 0 for player_position in self._player_positions)

    def _get_loser_position(self) -> PlayerPosition | None:
        for player_position in self._player_positions:
            if player_position.checkers_count > 0:
                return player_position


