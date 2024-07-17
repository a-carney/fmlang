#!/usr/bin/env python3
from enum import Enum
from dataclasses import dataclass
from math import log

# interest functions
cent = lambda r: r / 100
conr = lambda apr, ppy: cent(apr) / ppy
v = lambda i: 1 / (1 + i)
d = lambda i: 1 - v(i)

# annuity functions
a_ = lambda n, i: (1 - v(i) ** n) / i
s_ = lambda n, i: ((1 + i) ** n - 1) / i

# rule 72 (time to get increase of factor <growth> for interest rate <rate>
years_to_grow = lambda growth, rate: log(growth) / log(1 + cent(rate))


class PaymentFrequency(Enum):
    YEARLY = 1
    MONTHLY = 12
    WEEKLY = 52
    DAILY = 365




