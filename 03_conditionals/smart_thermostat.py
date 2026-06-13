temp = float(input("Enter the temperature: "))

device_status = "active"

if device_status == "active":
  if temp > 35:
    print(f"WARNING: HIGH TEMPERATURE")
  else: 
    print(f"Temperature is normal")
else:
  print(f"Device is offline")

