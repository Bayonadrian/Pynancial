import unittest
import pandas as pd
import numpy as np
from Pynancialyst.Invester import interest_rate

class TestInterestRate(unittest.TestCase):

    def setUp(self) -> None:

        ''' This class could admit any numerical value or list of numerical values, we are going to use a yahoo data set for testing. '''

        self.data = pd.read_csv('tests/TestData/yahoo_data_interest.csv').head()

        self.main_data = self.data['Adj Close']
        
        # Without other value parameter.
        self.interest_df = interest_rate.interestRateOfReturn(data= self.main_data, pd= True)

        # With other value parameter 
        self.interest_other = interest_rate.interestRateOfReturn(data= 5, other_value=3, pd= False)

    def test_constructor(self):

        # Data pd == True

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= [1,2,3], pd= True)

        with self.assertRaises(AssertionError):
        
            interest_rate.interestRateOfReturn(data= (1,2,3), pd= True)

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= {1,2,3}, pd= True)

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= np.array([1,2,3]), pd= True)

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= {'k': [1,2,3]}, pd= True)

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= 1, pd= True)

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= 1.1, pd= True)

        # Data pd == False

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= pd.DataFrame({'test': [1,2,3]}), pd= False)

        # Other_value pd == False required to make the test

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= pd.DataFrame({'test': [1,2,3]}), other_value=pd.DataFrame({'test': [1,2,3]}),pd= False)

        # pd

        with self.assertRaises(AssertionError):

            interest_rate.interestRateOfReturn(data= self.main_data, pd= 2)
    
    def test_sInterestRate(self):

        ''' Here there are the arrors for simple interest rate '''

        # Without other value parameter.
        simple = self.interest_df.simple(1)
        simple_period = self.interest_df.simple(250)
        # With other value parameter.
        simple_other = self.interest_other.simple(1)
        simple_other_period = self.interest_other.simple(250)

        # Error if period is less than 1.
        with self.assertRaises(AssertionError):

            self.interest_df.simple(0)

        # Simple with period == 1.
        self.assertEqual((simple[0].tolist()[1:], simple[1]), ([-0.008015827205964691, -0.014141328169356726, 0.002049033243804463, -0.004090124880830296], -0.0060495617530868140))
        # Simple with period < 1.
        self.assertEqual((simple_period[0].tolist()[1:], simple_period[1]), ([-0.008015827205964691, -0.014141328169356726, 0.002049033243804463, -0.004090124880830296], -1.5123904382717035))
        
        # Simple using other value parameter.
        self.assertEqual((simple_other[0], simple_other[1]), (0.6666666666666666, 0.6666666666666666))
        # Simple using other value parameter and period.
        self.assertEqual((simple_other_period[0], simple_other_period[1]), (0.6666666666666666, 166.66666666666666))

    def test_lInterestRate(self):

        # Without other value parameter.
        logarithmic = self.interest_df.logarithmic(1)
        logarithmic_period = self.interest_df.logarithmic(250)
        # With other value parameter.
        logarithmic_other = self.interest_other.logarithmic(1)
        logarithmic_other_period = self.interest_other.logarithmic(250)

        # Error if period is less than 1.
        with self.assertRaises(AssertionError):

            self.interest_df.logarithmic(0)

        # Logarithmic with period == 1.
        self.assertEqual((logarithmic[0].tolist()[1:], logarithmic[1]), ([-0.008048126669266648, -0.014242269510283803, 0.0020469368384351963, -0.004098512319861675], -0.00608549291524423250))
        # Logarithmic with period < 1.
        self.assertEqual((logarithmic_period[0].tolist()[1:], logarithmic_period[1]), ([-0.008048126669266648, -0.014242269510283803, 0.0020469368384351963, -0.004098512319861675], -1.5213732288110582))
        
        # Simple using other value parameter.
        self.assertEqual((logarithmic_other[0], logarithmic_other[1]), (0.5108256237659907, 0.5108256237659907))
        # Simple using other value parameter and period.
        self.assertEqual((logarithmic_other_period[0], logarithmic_other_period[1]), (0.5108256237659907, 127.70640594149768))