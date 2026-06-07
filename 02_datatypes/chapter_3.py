# Integer

black_tea_grams = 10
ginger_grams = 7

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of value {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Difference of grams: {remaining_tea}")

milk_litres = 7
servings = 4
print(f"Serving per consumer: {milk_litres //servings}") # '//' is used when no worries with decimal

total_cadamom_pods = 10
pods_per_cup = 3              
total_pods_per_cup = total_cadamom_pods / pods_per_cup # only integer with decimal
print(total_pods_per_cup)
total_pods_per_cup = total_cadamom_pods // pods_per_cup # only int with no decimal
print(total_pods_per_cup)
total_pods_per_cup = total_cadamom_pods % pods_per_cup  # remainder
print(total_pods_per_cup)

a = 2
b = 3
print(f"Exponential: {a ** b}") # exp: 2^3 or 2*2*2

#total_tea_level_harvested = 1_000_000_000
total_tea_level_harvested = 1,000,000,000
print(total_tea_level_harvested)