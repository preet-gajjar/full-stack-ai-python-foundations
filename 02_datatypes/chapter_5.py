#Real numbers

from decimal import Decimal
from fractions import Fraction

ideal_temp = Decimal('95')
current_temp = Decimal('94.99')
long_temp = Decimal('94.999999999999')

temp_diff = ideal_temp - current_temp
temp_long_diff = ideal_temp - long_temp

print(f"temp_diff: {temp_diff}")
print(f"long_temp_diff: {temp_long_diff:f}") # ':f' for formated decimal output 


