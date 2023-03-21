from Pynancialyst.Types import fTypes
import numpy as np

class interestRateOfReturn():

    def __init__(self, ending: float, beggining: float) -> None:
        
        self.ending = ending
        self.beggining = beggining

    def simple(self) -> fTypes.sInterestRate:

        return (self.ending -  self.beggining) / self.beggining

    def logarithmic(self) -> fTypes.lInterstRate:

        interest = self.ending / self.beggining

        return np.log(interest)