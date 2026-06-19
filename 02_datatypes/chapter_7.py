# Tuples -> ()

main_spices = ("cinnamon", "cloves", "cardamom")
(spice1, spice2, spice3) = main_spices

print(f"Total spices: {main_spices}")

cinnamon_ratio, clove_ratio = 2, 1
print(f"The ratio of Cinnamon is {cinnamon_ratio} and ratio of cloves is {clove_ratio}")
cinnamon_ratio, clove_ratio = clove_ratio, cinnamon_ratio #swapping
print(f"The ratio of Cinnamon is {cinnamon_ratio} and ratio of cloves is {clove_ratio}")

print(f"Is ginger available in main spices? {'ginger' in main_spices}")