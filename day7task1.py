import mymodule
from mymodule import j

print("Before editing the list: ", j)
j[2] = "another file"
print("After editing the list: ", j)
