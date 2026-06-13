size = input("Choose your cup size (small/medium/large): ").lower()

if size == "small": 
  print(f"Price is 10rs")

elif size == "medium":
  print(f"Price is 15rs")

elif size == "large":
  print(f"Price is 20rs")

else:
  print(f"Invalid option {size}")