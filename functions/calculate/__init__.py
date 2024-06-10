"""
Calculate module
"""
from .context import Calculator
from .strategy.strategy import *

#Конфигурационный словарик
method_map = {
    Romanovsky.id_: Romanovsky,
    Charlier.id_: Charlier,
    Dixon.id_: Dixon,
}
