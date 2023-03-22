import numpy as np
import pandas as pd
# from Pynancialyst.Types.f_types import Union, Number, SInterestRate, LInterstRate, PandasDataFrame
from Types.f_types import Union, Number, SInterestRate, LInterstRate, PandasDataFrame
from interest_rate import interestRateOfReturn

class portfolioRiskAna(interestRateOfReturn):

    def __init__(self, ending: PandasDataFrame, beggining: PandasDataFrame, pd: bool = False) -> None:
        super().__init__(ending, beggining, pd)

    def portfolio(self, period: int = 1, adjust: bool = True, report: bool = False):

        log = super().logarithmic(period= period)

        mean = log[1]

        std = log[0].std()

        cov = log[0].cov()

        cor = log[0].corr()

        if adjust == True:

            std = std * 250 ** 0.5

            cov = cov * 250

            sd = {'Standard Deviation': std, 'Mean': mean}

            table = pd.merge(sd, cov.iloc[:,0], left_index=True, right_index=True, how='outer').merge(cor.iloc[:,0], left_index=True, right_index=True, suffixes=('_Variation', '_Correlation'), how='outer')

            non_table = mean, std, cov, cor

        else:

            sd = {'Standard Deviation': std, 'Mean': mean}

            table = pd.merge(sd, cov.iloc[:,0], left_index=True, right_index=True, how='outer').merge(cor.iloc[:,0], left_index=True, right_index=True, suffixes=('_Variation', '_Correlation'), how='outer')

            non_table = mean, std, cov, cor

        if report == True:

            return table
        
        else:

            return non_table
