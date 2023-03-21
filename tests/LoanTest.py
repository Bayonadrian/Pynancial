import unittest
from Pynancialyst.LoanPayments import payments


class TestLoan(unittest.TestCase):

    def setUp(self) -> None:
        
        self.loan = payments.LoanP(300000,0.03,120)

    def test_Loan(self):

        self.assertEqual(self.loan, 2896.82)