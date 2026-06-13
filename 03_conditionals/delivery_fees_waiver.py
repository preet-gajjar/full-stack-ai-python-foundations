order_amount = float(input("Enter the amount to be paid: "))

# Type 1
if order_amount > 300:
  print(f"Delivery is free")
else:
  print(f"Delivery cost: 30rs")

#Type 2
delivery_fees = 0 if order_amount > 300 else 30
print(f"order amount is {order_amount} rs and delivery fees is {delivery_fees} rs")