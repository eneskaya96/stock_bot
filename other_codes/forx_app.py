from forex_python.converter import CurrencyRates
c = CurrencyRates()

rates = c.get_rate('USD', 'ACSEL')
print(rates)