from fastapi import FastAPI, HTTPException
from starlette import status

from models.models import GameResultInput, GameResultOutput
from services.game_service import GameResultService

app = FastAPI()


@app.post("/calculate_game_result", name="Calculates game resuls (points and win type)",
          response_model=GameResultOutput)
def calculate_game_result_output(game_result_input: GameResultInput):
    game_result_service = GameResultService(game_result_input)
    result = game_result_service.calculate_game_result_output()
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Provided game result is inconsistent with the endpoint you are trying to use. "
                                   "Please check, that the game is over.")
