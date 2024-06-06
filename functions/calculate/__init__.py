
from .context import Calculator
from .strategy import *

#Конфигурационный словарик https://www.youtube.com/watch?v=yHckrS1lvG8&t=7024s 2:56:29
method_map = {
    Romanovsky.id: Romanovsky,
    Charlier.id: Charlier,
    Dixon.id: Dixon,
}
