import numpy as np
from Pynancialyst.Types.f_types import Number, SInterestRate, LInterstRate, PandasDataFrame

class interestRateOfReturn():

    def __init__(self, data: PandasDataFrame, other_value: Number = None, pd: bool= True) -> None:
        
        assert not isinstance(data, (list, tuple, set, dict, type(np.array([])))), "Use Pandas Dataframe or numbers as params."
        assert isinstance(pd, bool), "pd argument must be a bool."

        # If user uses a Pandas Dataframe, then shift comes automatically.
        if pd == True:

            assert not isinstance(data, Number), "data parameter must be a Pandas Dataframe if pf == True."

            # Ending value.
            self.ending = data
            # Beggining value
            self.beggining = data.shift(1)

        # Otherwise shift is not incorporated.
        else:

            assert isinstance(data, Number), "data parameter must be a number(int or float)"
            assert isinstance(other_value, Number), "other_value parameter must be a number(int or float)"

            # Ending value.
            self.ending = data
            # Beggining value
            self.beggining = other_value

    def simple(self, period: int = 250) -> SInterestRate:

        assert period > 0, 'period value must be more than 0'

        rate = (self.ending -  self.beggining) / self.beggining

        return rate, np.mean(rate) * period

    def logarithmic(self, period: int = 250) -> LInterstRate:

        assert period > 0, 'period value must be more than 0'

        rate = self.ending / self.beggining

        rate = np.log(rate)

        return rate, np.mean(rate) * period