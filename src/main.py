from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from services.input_service import emu

class ClickOptions(BaseModel):
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]
    value: str


app = FastAPI()

@app.post("/move-click-paste")
def read_click(data: ClickOptions):
    emu.simulate_move_click_paste(
        data.x,
        data.y,
        data.width,
        data.height, 
        data.value
    )
    return data
