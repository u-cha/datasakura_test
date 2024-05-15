from fastapi import FastAPI
from models.models import GameResultInput, GameResultOutput
from services.game_service import GameResultService

app = FastAPI()


@app.post("/calculate_game_result", name="Calculates game resuls (points and win type)",
          response_model=GameResultOutput)
def calculate_game_result_output(game_result_input: GameResultInput):
    game_result_service = GameResultService(game_result_input)
    return game_result_service.calculate_game_result_output()
