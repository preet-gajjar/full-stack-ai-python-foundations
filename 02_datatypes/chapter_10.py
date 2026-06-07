# dictionary -> if data then use dict() else use {} for an empty dict

chai_order = dict(
  type = "Masala chai",
  size = "Large",
  sugar = "2",
  Note = "Note"
)

print(f"Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# printing only values through their keys 
print(f"Base recipe of chai: {chai_recipe['base']}")
print(f"Liquid recipe of chai: {chai_recipe['liquid']}")
# del chai_recipe["liquid"]

# membership test
print(f"Is sweetness in 'chai recipe'? {'sweetness' in chai_recipe}")

chai_recipe["sweetness"] = "sugar"
print(f"Is sweetness in 'chai recipe'? {'sweetness' in chai_recipe}")

chai_recipe = {"type": "Ginger chai", "size": "medium", "sugar": 2}

print(f"Keys of chai recipe: {chai_recipe.keys()}")
print(f"Values of chai recipe: {chai_recipe.values()}")
print(f"Items of chai recipe: {chai_recipe.items()}")

# remove custom item
last_item = chai_recipe.pop('type') 
print(f"Items: {last_item}")

# removing last item
last_item = chai_recipe.popitem() 
print(f"Items: {last_item}")

# updating and concatening 2 dicts
extra_spices = {"caradom" : "crushed", "ginger" : "sliced"}
chai_recipe.update(extra_spices)

print(f"Chai recipe: {extra_spices}")
print(f"Chai recipe: {chai_recipe}")

## .get(key, backup_string) 

# Note key exists hence true
customer_note = chai_order.get("Note", "NO Note") 
print(f"Customer Note: {customer_note}")