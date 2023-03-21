import typing

LoanPayments = typing.NewType('Loan payments', float)
sInterestRate = typing.NewType('Simple interest rate of return', float)
lInterstRate = typing.NewType('Logarithmic interest rate of return', float)
PresentValue = typing.NewType('Present value', list)
NetPresentValue = typing.NewType('Net present value', float)
InternalRateOfReturn = typing.NewType('Internal rate of return', float)