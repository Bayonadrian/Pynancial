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

    def test_sInterestRate(self):

        ''' Here there are the arrors for simple interest rate '''

        simple = self.interest.simple()
        simple_period = self.interest.simple(250)

        # Error if period is less than 1.
        with self.assertRaises(AssertionError):

            self.interest.simple(0)

        # Simple with period == 1.
        self.assertEqual(simple.tolist()[1:], [-0.008015827205964691, -0.014141328169356726, 0.002049033243804463, -0.004090124880830296])
        # Simple with period < 1.
        self.assertEqual((simple_period[0].tolist()[1:], simple_period[1]), ([-0.008015827205964691, -0.014141328169356726, 0.002049033243804463, -0.004090124880830296], -1.5123904382717035))
        
    def test_lInterestRate(self):

        logarithmic = self.interest.logarithmic()
        logarithmic_period = self.interest.logarithmic(250)

        # Error if period is less than 1.
        with self.assertRaises(AssertionError):

            self.interest.logarithmic(0)

        # Logarithmic with period == 1.
        self.assertEqual(logarithmic.tolist()[1:], [-0.008048126669266648, -0.014242269510283803, 0.0020469368384351963, -0.004098512319861675])
        # Logarithmic with period < 1.
        self.assertEqual((logarithmic_period[0].tolist()[1:], logarithmic_period[1]), ([-0.008048126669266648, -0.014242269510283803, 0.0020469368384351963, -0.004098512319861675], -1.5213732288110582))
        