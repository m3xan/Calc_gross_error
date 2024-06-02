from pydantic import BaseModel, Field, model_validator

from PySide6.QtCore import Qt

class Canvas(BaseModel):
    text: str
    canvas: str

class Window(BaseModel):
    dockWidget: Qt.DockWidgetArea = Field(..., enum=Qt.DockWidgetArea)
    toolBar: Qt.ToolBarArea = Field(..., enum=Qt.ToolBarArea)
    theme: str
    canvas: Canvas

class AutoSave(BaseModel):
    switched: bool
    time: int = None

    @model_validator(mode='after')
    def validate_switched(self):
        if not self.switched:
            if self.time is None:
                return self
        else:
            if isinstance(self.time, int):
                if self.time % 60000 == 0: #minute -> millisecond
                    return self
                raise ValueError('time field must be int presentation minute -> millisecond')
        raise ValueError("The 'time' field must be set if 'switched' is True.")

class Calculation(BaseModel):
    method: int
    significance_level: float

class UserSettings(BaseModel):
    window: Window = Field(default_factory=Window)
    auto_save: AutoSave = Field(default_factory=AutoSave)
    calculation: Calculation = Field(default_factory=Calculation)
    save_user_name: bool
