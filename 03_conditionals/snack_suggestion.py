snack = input("Choose tour snack: ").lower()

print(f"User chose {snack}")

if snack == "samosa" and "chai":
  print(f"Will be shortly back with your {snack}")
else:
  print(f"Sorry! We are not currently selling {snack}")