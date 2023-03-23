import unittest
import pandas as pd
import numpy as np
from Pynancialyst.Invester.risk_measurement import portfolioRisk

class TestRisk(unittest.TestCase):

    def setUp(self) -> None:

        self.data = pd.read_csv('tests\TestData\yahoo_data_risk.csv')

        self.risk = portfolioRisk(self.data[['PG', 'BEI.DE']])

    def test_portfolio(self):

        # print(self.risk.portfolio())

        pass

    def test_volatility(self):

        print(self.risk.portfolio_volatility([0.5, 0.5]))