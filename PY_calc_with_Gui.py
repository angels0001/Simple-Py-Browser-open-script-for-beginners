#python App 
from weakref import WeakValueDictionary
import webbrowser


print("Hello, what would you like to do?")

print("Open Google?")

input1 = input("$  ")
if input1 == "Google":
    webbrowser.open("google.com")
else:
    print("error? please reinput")