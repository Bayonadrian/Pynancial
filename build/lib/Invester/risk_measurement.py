import pandas as pd
import numpy as np
from Types.f_types import PandasDataFrame, Union, List
from Invester.interest_rate import interestRateOfReturn

class portfolioRisk(interestRateOfReturn):

    def __init__(self, data: PandasDataFrame) -> None:
        super().__init__(data= data)

    def portfolio(self, period: int = 250, adjust: bool = True, report: bool = False):

        log = super().logarithmic(period= period)

        mean = log[1]

        std = log[0].std()

        cov = log[0].cov()

        cor = log[0].corr()

        if adjust == True:

            std = std * period ** 0.5

            cov = cov * period

            sd = pd.DataFrame({'Standard Deviation': std, 'Mean': mean})

            table = pd.merge(sd, cov.iloc[:,:], left_index=True, right_index=True, how='outer').merge(cor.iloc[:,:], left_index=True, right_index=True, suffixes=('_Variation', '_Correlation'), how='outer')

            non_table = mean, std, cov, cor

        else:

            sd = pd.DataFrame({'Standard Deviation': std, 'Mean': mean})

            table = pd.merge(sd, cov.iloc[:,:], left_index=True, right_index=True, how='outer').merge(cor.iloc[:,:], left_index=True, right_index=True, suffixes=('_Variation', '_Correlation'), how='outer')

            non_table = mean, std, cov, cor

        if report == True:

            return table
        
        else:

            return non_table
        
    def portfolio_var_vol_atility(self, weights: Union[List[float], np.ndarray], period: int = 250):

        log = super().logarithmic(period= period)[0]

        assert len(log.columns) == len(weights), 'You must assign a weight per each value within the data.'
        assert isinstance(weights, (list, np.array([]))), 'weights parameter must be a list.'

        weights = np.array(weights)

        var = np.dot(weights.T, np.dot(log.cov() * period, weights))

        vol = (np.dot(weights.T, np.dot(log.cov() * period, weights))) ** 0.5

        return var, vol

