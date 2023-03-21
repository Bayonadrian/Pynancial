from typing import Any
from Pynancialyst.Types import fTypes
import numpy as np

class interestRateOfReturn():

    def __init__(self, ending: Any, beggining: Any, pd= False) -> None:
        
        # If user uses a Pandas Dataframe, then shift comes automatically.
        if pd == True:

            # Ending value.
            self.ending = ending
            # Beggining value
            self.beggining = beggining.shift(1)

        # Otherwise shift is not incorporated.
        else:

            # Ending value.
            self.ending = ending
            # Beggining value
            self.beggining = beggining

    def simple(self) -> fTypes.sInterestRate:

        return (self.ending -  self.beggining) / self.beggining

    def logarithmic(self) -> fTypes.lInterstRate:

        interest = self.ending / self.beggining

        return np.log(interest)