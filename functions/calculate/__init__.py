"""
Calculate module

Use:

>>> calc = Calculator()
>>> calc.method = method_map[Romanovsky.id_]()
>>> answ = calc.calculate_with(
>>>    [0.93, 0.93, 0.93, 1.6], 0.95)
return [1.6]
"""

from .context import Calculator
from .strategy.strategy import *

# Configuration dict
method_map = {
    Romanovsky.id_: Romanovsky,
    Charlier.id_: Charlier,
    Dixon.id_: Dixon,
}
