'''
Created on Apr 14, 2017

@author: pneela
'''

with open('text.txt', 'r') as fd:
    for line in fd:
        print(line)


''' 
# Open the file for reading
with open("text.txt", "r") as read_file:
    print(read_file.read())

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file

my_file = open("text.txt", 'r')
 
print("\n".join(dir(type(my_file))))
 
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
 
my_file.close'''