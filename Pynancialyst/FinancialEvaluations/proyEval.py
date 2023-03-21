import numpy as np
from Pynancialyst.Types import fTypes

class Eval:

    def __init__(self, cashFlow: list) -> None:

        self.cashFlow = np.array(cashFlow)

        self.pv = 0

    def PV(self, interest: float, decimals: int)-> fTypes.PresentValue:

        assert interest < 1 and interest > 0, 'interest has to be a float between 1 and 0.'
        assert type(decimals) == int, 'Decimals has to be an integer.'

        cEnumerated: list = list(enumerate(self.cashFlow))
        
        pv= list(map(lambda x: x[1]/((1+interest)**x[0]), cEnumerated))
        
        self.pv = np.round(pv, decimals)

        return np.round(pv, decimals)
    
    def NPV(self)-> fTypes.NetPresentValue:

        # assert self.pv != 0, 'Don\'t forget to use PV method first'

        return np.sum(self.pv)

    def IRR(self, steps = 0.00001, min=0.001)-> fTypes.InternalRateOfReturn:

        cEnumerated: list = list(enumerate(self.cashFlow))

        for interest in np.arange(0, 1, steps):

            pv= list(map(lambda x: x[1]/((1+interest)**x[0]), cEnumerated))

            if sum(pv) < min:

                return sum(pv), interest

