#!/usr/bin/env python3
import re

from TVM import a_, cent, conr, PaymentFrequency as freq
from dataclasses import dataclass


@dataclass(frozen=True)
class Loan:
    BALANCE: float
    APR: float
    PAYMENT_FREQUENCY: freq
    LENGTH: str

    def get_number_of_payments(self):
        length = self.LENGTH.lower()
        numbers = float(''.join(re.findall(r'\d+', length)))
        if any(char is 'm' for char in length):
            return numbers * 12
        elif any(char is 'y' for char in length):
            return numbers
        else:
            raise ValueError("Error, invalid length type")

    def get_payment(self):
        i = conr(self.APR, self.PAYMENT_FREQUENCY)
        n = self.get_number_of_payments()
        return self.BALANCE / a_(n, i)

    def get_total_paid(self):
        return self.get_number_of_payments() * self.get_payment()


