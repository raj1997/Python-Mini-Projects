a = [1,3,5,7,2]

print("=="*30)
for i in a:
    if i%2 == 0:
        print("Breaking the loop : Even Number Found : ",i)
        break
    else:
        print("Odd number : ",i)
else:
    print("Brek stmt is not used in For Loop")
print("=="*30)

b = [1,3,5,7,9]
print("=="*30)
for i in b:
    if i%2 == 0:
        print("Even Number Found : ",i)
        break
    else:
        print("Odd number : ",i)
else:
    print("Break stmt is not used in For Loop")
print("=="*30)
