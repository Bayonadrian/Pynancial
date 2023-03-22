from Pynancialyst.Types import f_types
import numpy as np

def LoanP(total: float, anualInterest: float, period: int, r: int=2)-> f_types.LoanPayments:

    interest = anualInterest/12

    return np.round((total*interest*(1+interest)**period)/(((1+interest)**period) -1), r)