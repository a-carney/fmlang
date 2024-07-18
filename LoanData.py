#!/usr/bin/env python3
import re

from TVM import a_, cent, conr, PaymentFrequency as freq
from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Debt:
    BALANCE: float
    APR: float


@dataclass(frozen=True)
class Loan:
    BALANCE: float
    APR: float
    PPY: int
    YEARS: float

    def num_pmt(self):
        return round(self.PPY + self.YEARS)

    def interest_rate(self):
        return conr(self.APR, self.PPY)


def get_loan_pmt(l: Loan) -> float:
    return l.BALANCE / a_(l.num_pmt(), l.interest_rate())


"""
Ah yes, Loans. If money is the root of all evil, loans might as well be the apple tree in the garden of eden. 

Consumers generally find themselves in this payment structure for a few reasons:
    1.) Car Loan 
    2.) Student Loan 
    3.) Credit Card Debt
    
Though these loans are typically compounded daily or monthly, we will assume monthly for the time being

"""


class DebtType(Enum):
    CAR = 0
    STUDENT = 1
    CREDIT = 2

@dataclass(frozen=True)
class PaymentPlan:
    PMT: float
    PPY: int

def get_loan_data(balance: float, apr: float, length: float, ppy=12):





