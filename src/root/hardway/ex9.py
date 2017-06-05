'''
Created on Apr 17, 2017

@author: pneela
'''

# Here's some new strange stuff, remember type it exactly.
# printing multiple lines

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# check the difference in the o/p of following two
print("%s" %(months))
print("%r" %(months))
# Multi line printing and also prints special characters 
# without escaping them.


print('''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
''')

'''
while True:
    for i in ["/","-","|","\\","|"]:
        print("%s \r" %i)
    
'''