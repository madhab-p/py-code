'''
Created on Apr 17, 2017

@author: pneela
'''
#exercise-8

# various way to format strings to print

# there is difference in  %r & %s - %r prints it the way you'd write 
# it in your file, but %s prints it the way you'd like to see
  
formatter = "%s %s %r %r"
var = 1
print (formatter %(1,2,34,4))
print(formatter %('one','two','three','four'))
print(formatter %(formatter, formatter,formatter,formatter))

#Note this text print the text -a & text - with single quotes
text = "this is %r %r for replacement" %("a","text")
print(text)

# String formating can be done using .format() mehtod of string

# .format() mehtod does the replacement without the quotes
text = "this is {} {} for replacement".format("a","text")
print(text)


# The numbers in {} can be used to reorder/reuse the arguments usages
string = "This is {0} string {2} number {1}".format('a', 'of', 1)
print(string) 