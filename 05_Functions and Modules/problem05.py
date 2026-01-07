# 5. Modules and Pip – Using External Libraries

# Import the math module  and use it to

# 1. find the square  root 144

import math
import requests

# print(math.sqrt(144))

# calculate sin90

print(math.sin(math.radians(90)))

r = requests.get("https://api.github.com")

print(r.json())
