from Types import fTypes
import numpy as np

def LoanP(total: float, anualInterest: float, period: int, r: int=2)-> fTypes.LoanPayments:

    interest = anualInterest/12

    return np.round((total*interest*(1+interest)**period)/(((1+interest)**period) -1), r)