import pandas as pd
import numpy as np

class CorrelationCalculator:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def calculate_correlation(self, column1, column2):
        return self.data[column1].corr(self.data[column2])

    def calculate_correlation_matrix(self):
        return self.data.corr()

    def get_correlation_coefficient(self, column1, column2):
        return self.data[column1].corr(self.data[column2])

    def get_correlation_coefficient_matrix(self):
        return self.data.corr()

# Misol uchun ma'lumotlar
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 5, 7, 11],
    'C': [3, 5, 7, 11, 13]
}

calculator = CorrelationCalculator(data)

print(calculator.calculate_correlation('A', 'B'))
print(calculator.calculate_correlation_matrix())
print(calculator.get_correlation_coefficient('A', 'B'))
print(calculator.get_correlation_coefficient_matrix())
