# String Operations: indexing, slicing, encoding, decoding, core

chai_type = "Ginger"
customer_name = "Preet"

print(f"{chai_type} tea for : {customer_name} please!")

# String indexing and slicing

chai_description = "Aromatic and Bold"
print(f"Description of chai: {chai_description[0:8:1]}") # [start:ending+1:jump]
print(f"Description of chai: {chai_description[:8:1]}") #same [:ending+1:jump]
print(f"Description of chai: {chai_description[0:8:2]}")

print(f"Description of chai: {chai_description[12:]}") # [start:(whole part)]
print(f"Description of chai: {chai_description[12::2]}") # [start:(whole part):jump]

print(f"Description of chai: {chai_description[:7:-1]}") # [:ending+1:-jump]

# String encoding and decoding 

label_txt = "Chāi Special"
encoded_label = label_txt.encode("utf-8")
print(f"Non encoded label: {label_txt}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")
