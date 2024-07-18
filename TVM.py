#!/usr/bin/env python3
from enum import Enum
from dataclasses import dataclass
from math import log, e, pow

"""
COMMONLY USED TERMS FOR INTEREST THEORY CALCULATIONS

TERM                VARS        INFO
interest as rate    i,r         interest rate in range 0 -> 1 (i.e. 0.25 == 5%) 
interest as apr     apr         interest rate in range 0 -> 100 (i.e. 5.0 == 5%)
discount fact ('v') v           commonly used FM variable == 1/(1+i)
discount rate ('d') d           another common FM var == 1-v
PV                  PV          present value of future payment(s) 
FV                  FV          future value
annuity             a_          a term for a recurring payment structure over fixed period, this var is for PV
""                  s_          same as above but FV                  
payments            PMT         value of single payment in level annuity 
number of payments  n           when evaluating annuities, n is used for number of payments
periods per year    ppy         number of payments for one year
"""

cent = lambda r: r / 100
conr = lambda apr, ppy: cent(apr) / ppy
v = lambda i: 1 / (1 + i)
d = lambda i: 1 - v(i)

a_ = lambda n, i: (1 - v(i) ** n) / i
s_ = lambda n, i: ((1 + i) ** n - 1) / i

years_to_grow = lambda growth, rate: log(growth) / log(1 + cent(rate))
rate_of_return = lambda growth, years: pow(e, (log(growth) / years)) - 1


class PaymentFrequency(Enum):
    YEARLY = 1
    MONTHLY = 12
    WEEKLY = 52
    DAILY = 365


def _get_pmt_freq(ppy):
    if ppy == 1:
        return PaymentFrequency.YEARLY
    elif ppy == 12:
        return PaymentFrequency.MONTHLY
    elif ppy == 52:
        return PaymentFrequency.WEEKLY
    elif ppy == 365:
        return PaymentFrequency.DAILY
