"""
Write a python script to Change the values "SQL" and "Reactnative"
with the values "NoSQL" and "Flutter" (List is thislist =
["Java", "SQL", "C","Reactnative","Javascript", "Python"]
"""

thislist = ["Java", "SQL", "C","Reactnative","Javascript", "Python"]
i = 0
while i < len(thislist):
    if thislist[i] == "SQL":
        thislist[i] = "NoSQL"
    elif thislist[i] == "Reactnative":
        thislist[i] = "Flutter"
    i += 1  
print()
print(thislist)
print()
