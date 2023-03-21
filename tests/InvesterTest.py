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

        self.assertEqual(self.simple.tolist()[1:], [-0.008015766338726919, -0.014141266314460766, 0.002049095857393118, -0.004090500051719038])

    def test_lInterestRate(self):

        self.assertEqual(self.logarithmic.tolist()[1:], [-0.00804806531018693, -0.014242206768132409, 0.002046999323986804, -0.004098889031619274])