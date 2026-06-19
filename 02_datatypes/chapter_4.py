# 'boolean' datatype, 'bool' variable, NoneType 'None'

is_boiling = True # boolean datatype
a = 5
total = is_boiling + a
print(f"Total: {total}")   # Total: 6

milk_present = 0 # No milk
print(f"Is there any milk present?: {bool(milk_present)}") # bool function

milk_present = None # NoneType datatype for no milk
print(f"Is there any milk present?: {bool(milk_present)}") # bool function

tea = True
coffee = False

print(f"Tea and coffee: {tea and coffee}")
print(f"Tea or coffee: {tea or coffee}")