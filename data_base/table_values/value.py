
import math
from decimal import Decimal

from sqlalchemy.orm import Session

from data_base.table_values.table_model import N_Value
from data_base.table_values.table_model import P_Value
from data_base.table_values.table_model import Romanovsky_Table
from data_base.table_values.table_model import Charlier_Table
from data_base.table_values.table_model import Dixon_Table

from data_base.engines import table_engine as engine

P_ = [0.99, 0.98, 0.95, 0.9]

def fill_out_the_table():
    with Session(engine) as session:
        for i in range(1, 101):
            new_n = N_Value(
                n=i
            )
            session.add(new_n)
        for i in P_:
            _p = P_Value(
                p= i
            )
            session.add(_p)
        for i in range(1, 101):
            new_sahar = Charlier_Table(
                n_id= i,
                p_id = 3,
                value = (
                    Decimal(0.3381) + Decimal(0.71441)* Decimal(math.log(i, math.e))
                    ) / (
                        1+ Decimal(0.0885) * Decimal(math.log(i, math.e))
                    )
            )
            session.add(new_sahar)
        for i in range(4, 31):
            for q in range(0, 4):
                match P_[q - 1]:
                    case 0.99:
                        value = Decimal(math.sqrt(Decimal(-1.4175 - 0.0284 * i) /
                            Decimal(1 + i * ( -0.719 + 0.01 * i))))
                    case 0.98:
                        value = Decimal(math.sqrt(Decimal(-0.8824 - 0.0191 * i) /
                            Decimal(1 + i * ( -0.5743 + 0.0125 * i))))
                    case 0.95:
                        value = Decimal(math.sqrt(Decimal(-0.6691 - 0.0029 * i) /
                            Decimal(1 + i * ( -0.5605 + 0.00631 * i))))
                    case 0.9:
                        value = Decimal(math.sqrt(Decimal(0.0018 * i - 0.42) /
                            Decimal(1 + i * ( -0.00715 * i - 0.501))))
                new = Dixon_Table(
                    p_id = q,
                    n_id = i,
                    value = value
                )
                session.add(new)
        for i in range(3, 101):
            for q in range(1, 5):
                match P_[q - 1]:
                    case 0.99:
                        answer = Decimal(4.1127) - (Decimal(4.799) / Decimal(math.sqrt(i)))
                    case 0.98:
                        answer = Decimal(3.956) - (Decimal(4.4754) / Decimal(math.sqrt(i)))
                    case 0.95:
                        if i > 20:
                            continue
                        answer = Decimal(
                            3.2177
                        ) - (Decimal(0.1513) * Decimal(i)) + (Decimal(2.9504) * Decimal(math.log(i, math.e))) - (
                            Decimal(28.079) / Decimal(math.log(i, math.e))
                            ) + (Decimal(61.048) / Decimal(i))
                    case 0.9:
                        answer = Decimal(3.3535) - (Decimal(3.3115) / Decimal(math.sqrt(i)))
                new = Romanovsky_Table(
                    value = answer,
                    p_id = q,
                    n_id = i
                )
                session.add(new)
        session.commit()
