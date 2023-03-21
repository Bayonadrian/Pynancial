import unittest
from Pynancialyst.FinancialEvaluations import proyEval


class TestEval(unittest.TestCase):

    def setUp(self) -> None:
        
        self.Eval = proyEval.Eval([-500,30,120,200,120,120])
        self.PV = self.Eval.PV(0.1, 3) 
        self.NPV = self.Eval.NPV()
        self.IRR = self.Eval.IRR()

    def test_PV(self):

        self.assertEqual(list(self.PV), [-500, 27.273, 99.174, 150.263, 81.962, 74.511])

    def test_NPV(self):

        self.assertEqual(self.NPV, -66.81699999999998)
    
    def test_IRR(self):

        self.assertEqual(self.IRR, (-0.006466674612326528, 0.0519))