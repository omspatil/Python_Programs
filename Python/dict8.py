"""Consider following dictionary and fetch the {k:v} pair from it which contains “in” in either key or 
value.
dict1 = {“college”: “amazing”, “king”: “packing”, “being”: “power”, “inning”: “donate”}
create a new dictionary contains resulting {k:v} pairs"""

dict1 = {"college": "amazing", "king": "packing",
         "being": "power", "inning": "donate"}
r = {}
for k, v in dict1.items():
    if "in" in k or "in" in v:
        r[k] = v
print(r)
