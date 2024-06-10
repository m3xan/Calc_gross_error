"""
model
"""

from pydantic import BaseModel, Field, model_validator, field_validator
from PySide6.QtCore import Qt

from functions.calculate import MethodId

class CanvasModel(BaseModel):
    text: str
    canvas: str

class MainWindowElement(BaseModel):
    dockWidget: Qt.DockWidgetArea = Field(..., enum= Qt.DockWidgetArea)
    toolBar: Qt.ToolBarArea = Field(..., enum= Qt.ToolBarArea)

class Window(BaseModel):
    element: MainWindowElement
    theme: str
    canvas_settings: CanvasModel

class AutoSave(BaseModel):
    switched: bool
    time: int= None

    @field_validator('time')
    @classmethod
    def validate_time(cls, v):
        if isinstance(v, int | float) and v % 60000 == 0:
            return int(v)
        if isinstance(v, str):
            try:
                if int(v) % 60000 == 0:
                    return int(v)
            except ValueError as err:
                raise ValueError(f'time must be int | float not {v}') from err
        raise ValueError(
            'time field must be int | float | str presentation minute -> millisecond'
        )

class Calculation(BaseModel):
    method: MethodId = Field(..., enum= MethodId)
    significance_level: float

    @model_validator(mode= 'after')
    def validate_significance_level(self):
        if not self.significance_level in [0.99, 0.98, 0.95, 0.9]:
            raise ValueError(
                f'significance_level must be 0.99, 0.98, 0.95, 0.9 not {self.significance_level}'
            )
        return self

class GraphSettings(BaseModel):
    window_size: int = 5

class UserSettings(BaseModel):
    window: Window = Field(default_factory= Window)
    auto_save: AutoSave = Field(default_factory= AutoSave)
    calculation: Calculation = Field(default_factory= Calculation)
    graph_settinsgs: GraphSettings = Field(default_factory= GraphSettings)
    save_user_name: bool
