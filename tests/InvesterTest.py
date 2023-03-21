import unittest
import pandas as pd
from Pynancialyst.Invester import interestRate

class TestInterest(unittest.TestCase):

    def setUp(self) -> None:

        ''' This class could admit any numerical value or list of numerical values, we are going to use a yahoo data set for testing. '''

        self.data = pd.read_csv('tests/TestData/yahoo_data.csv').head()

        self.ending = self.data['Adj Close']
        self.beggining = self.data['Adj Close']
        
        self.interest = interestRate.interestRateOfReturn(ending= self.ending, beggining= self.beggining, pd= True)
        self.simple = self.interest.simple()
        self.logarithmic = self.interest.logarithmic()

    def test_sInterestRate(self):

        ''' First element is Nan due to the shift then we remove it with [1:] '''

        self.assertEqual(self.simple.tolist()[1:], [-0.008015827205964691, -0.014141328169356726, 0.002049033243804463, -0.004090124880830296])

    def test_lInterestRate(self):

        self.assertEqual(self.logarithmic.tolist()[1:], [-0.008048126669266648, -0.014242269510283803, 0.0020469368384351963, -0.004098512319861675])