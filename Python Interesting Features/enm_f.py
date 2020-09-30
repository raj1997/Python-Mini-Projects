months = [  'January','February','March','April',
            'May','June','July','August',
            'September','October','November','December'
        ]

count = 1
print("=="*20)
for month in months:
    print("{0:<4} {1:<25}".format(count,month) )
    count+=1
print("=="*20)

print("=="*20)
for count,month in enumerate(months,1):
    print("{0:<4} {1:<25}".format(count,month) )
print("=="*20)
