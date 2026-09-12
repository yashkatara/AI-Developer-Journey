friennds  = [ "Yash", "Rohit", "Ramesh", 5,False,3.14,"Suresh", "Mahesh"]
print(friennds[3])
print(friennds[0:3])
print(friennds[2:5])

#lists are mutable and its index are like strings and they start from 0 to n-1 where n is the length of the list
print(len(friennds))
friennds[3] = "Rohit"
print(friennds[3])
friennds.append("Rakesh")

l1 = [1,26,13,40,5]
l1.sort()
print(l1) 