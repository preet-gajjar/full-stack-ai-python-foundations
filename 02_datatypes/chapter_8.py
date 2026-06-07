# Lists -> []

# appending elements
ingredients = ["milk", "water", "black_tea"]
ingredients.append("sugar")
print(f"The ingredients are: {ingredients}")

# removing elements
ingredients.remove("water")
print(f"The ingredients are: {ingredients}")

# list concatenation using exetend
chai_ingredients = ["milk", "water"]
spice_options = ["ginger", "cardamom"]

chai_ingredients.extend(spice_options)
print(f"Chai Ingredients are: {chai_ingredients}")

# inserting element between or into a already created list
chai_ingredients.insert(2, "black tea")
print(f"Chai Ingredients are: {chai_ingredients}")

# popping the last inserted element from the list
last_added = chai_ingredients.pop()
print(f"Chai Ingredients are: {chai_ingredients}")

# reversing the list
chai_ingredients.reverse()
print(f"Chai Ingredients are: {chai_ingredients}")

# sorting the list in alphabetical order
chai_ingredients.sort()
print(f"Chai Ingredients are: {chai_ingredients}")

# min, max functions
sugar_levels = [1,2,3,4,5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# operator overloading: adding lists directly with '+'
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Complete Liquid Mix: {full_liquid_mix}")

# operator overloading: multiplying with lists
strong_brew = ["black tea", "water"]
three_shotted_brew = strong_brew * 3
print(f"Three more shots please: {three_shotted_brew}")

ingredient = "olive oil"
recipie = []

recipie.append(ingredient)
print(f"The ingredient added to the recipie is: {recipie}")

# byteArray
raw_spice_data = bytearray(b"CINNAMON")
main_raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {main_raw_spice_data}")