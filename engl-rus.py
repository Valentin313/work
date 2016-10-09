#!/user/bin/evn python3

dect = {"f": "а", "l": "д"}
lst = input("Enter the word: ")
lst = list(lst)

for a in dect:
for b in lst:
    if a == b:
	   print(dect.get(a))
           
