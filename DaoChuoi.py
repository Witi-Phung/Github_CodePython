s = "This is an apple"
s.split(" ")
lst = []
for v in s.split(" "):
	lst.append(v)
print(lst)
lst.reverse()
print(" ".join(lst))