import os, sys

os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# code imported from another module is executed when imported
import module1

# note__name__ is module1 when ran from outside of module.py
# when module1.py is ran -> __name = "__main__"

# when importing a module - a reference will be created to sys.module
print("globals namespace")
print(globals()["module1"])

# when importing a module - it will be stored in sys.modules
print("sys.modules")
print(sys.modules["module1"])



print(f"\n{'='*30}main.py{'='*30}")

