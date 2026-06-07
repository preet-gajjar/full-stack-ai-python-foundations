# sets -> {} ~ Uniqueness

essential_spices = {"ginger", "cardamom", "cinnamon"} 
optional_spices = {"ginger", "black pepper", "cloves"}

#union -> unique values
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

#intersection -> common values
all_spices = essential_spices & optional_spices
print(f"All spices: {all_spices}")

#minus/difference -> subtracts set 1's values from set 2
only_essential_spices = essential_spices - optional_spices
print(f"All spices: {only_essential_spices}")

#membership
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")