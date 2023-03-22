import numpy as np
from Pynancialyst.Types.fTypes import Union, Number, SInterestRate, LInterstRate, PandasDataFrame

class interestRateOfReturn():

    def __init__(self, ending: Union[Number, PandasDataFrame], beggining: Union[Number, PandasDataFrame], pd: bool= False) -> None:
        
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

    def simple(self, period: int = 1) -> SInterestRate:

        assert period > 0, 'period value must be more than 0'

        rate = (self.ending -  self.beggining) / self.beggining

        return rate, np.mean(rate) * period

    def logarithmic(self, period: int = 1) -> LInterstRate:

        assert period > 0, 'period value must be more than 0'

        rate = self.ending / self.beggining

        rate = np.log(rate)

        return rate, np.mean(rate) * period