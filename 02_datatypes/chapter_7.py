# Tuples -> ()

main_spices = ("cinnamon", "cloves", "cardamom")
(spice1, spice2, spice3) = main_spices

print(f"Total spices: {main_spices}")

cinnamon_ratio, cloves_ratio = 2, 1
print(f"The ratio of Cinnamon is {cinnamon_ratio} and ratio of cloves is {cloves_ratio}")
cinnamon_ratio, cloves_ratio = cloves_ratio, cinnamon_ratio #swapping
print(f"The ratio of Cinnamon is {cinnamon_ratio} and ratio of cloves is {cloves_ratio}")

print(f"Is ginger available in main spices? {'ginger' in main_spices}")