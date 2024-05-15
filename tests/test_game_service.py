import typing

from uuid import uuid4
from pydantic import UUID4

from models.models import Board, GameResultInput, BoardPoint, GameResultOutput, GameWinType
from services.game_service import GameResultService


def get_bar_count_for_player(player_uuid: typing.Optional[UUID4] = None) -> dict:
    if not player_uuid:
        return dict()
    return {player_uuid: 1}


def get_game_result_input(board: Board, start_position: dict[uuid4, int]) -> GameResultInput:
    return GameResultInput(board=board, start_position=start_position)


loser_uuid = uuid4()

start_pos = {loser_uuid: 0,
             uuid4(): 23}


def test_one_checker_left__win_type_is_oin():
    # arrange
    brd = Board(bar_counts=get_bar_count_for_player(),
                points=[
                    BoardPoint(number=1, checkers_count=1, occupied_by=loser_uuid)]
                )
    game_result_input = get_game_result_input(board=brd, start_position=start_pos)
    game_service = GameResultService(game_result_input)

    # act
    result_output = game_service.calculate_game_result_output()

    # assert
    assert result_output == GameResultOutput(points=1, win_type=GameWinType.Oin)


def test_loser_got_checkers_at_bar__win_type_is_koks():
    # arrange
    brd = Board(bar_counts=get_bar_count_for_player(loser_uuid),
                points=[
                    BoardPoint(number=0, checkers_count=15, occupied_by=loser_uuid)]
                )
    game_result_input = get_game_result_input(board=brd, start_position=start_pos)
    game_service = GameResultService(game_result_input)

    # act
    result_output = game_service.calculate_game_result_output()

    # assert
    assert result_output == GameResultOutput(points=3, win_type=GameWinType.Koks)


def test_loser_got_checkers_at_enemy_home__win_type_is_koks():
    # arrange
    brd = Board(bar_counts=get_bar_count_for_player(loser_uuid),
                points=[
                    BoardPoint(number=23, checkers_count=1, occupied_by=loser_uuid),
                    BoardPoint(number=0, checkers_count=14, occupied_by=loser_uuid)]
                )

    game_result_input = get_game_result_input(board=brd, start_position=start_pos)
    game_service = GameResultService(game_result_input)

    # act
    result_output = game_service.calculate_game_result_output()

    # assert
    assert result_output == GameResultOutput(points=3, win_type=GameWinType.Koks)


def test_loser_got_checkers_at_home__win_type_is_mars():
    # arrange
    brd = Board(bar_counts=get_bar_count_for_player(),
                points=[
                    BoardPoint(number=0, checkers_count=14, occupied_by=loser_uuid),
                    BoardPoint(number=7, checkers_count=1, occupied_by=loser_uuid)]
                )

    game_result_input = get_game_result_input(board=brd, start_position=start_pos)
    game_service = GameResultService(game_result_input)

    # act
    result_output = game_service.calculate_game_result_output()

    # assert
    assert result_output == GameResultOutput(points=2, win_type=GameWinType.Mars)
