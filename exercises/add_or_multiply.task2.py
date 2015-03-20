#first coding challenge!  

# You will learn about:

# - print statements (output)
# - standard input
# - integer conversion of strings
# - string conversion and appending in stdout
# - conditional statements


# task 2 solution:
import sys
n1=int(sys.argv[1])
n2=int(sys.argv[2])
operation=int(sys.argv[3])

print 'hello world! This is (WHO?)s pi!'
print 'n1 is ' + str(n1)
print 'n2 is ' + str(n2)
print 'operation is '+str(operation)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 1: 
# write a conditional statement that 
#  - adds n1 and n2 if operation is 1 and prints output 
#  - multiplies n1 and n2 if operation is 2 and prints output
# ++++++++++++++++++++++++++++++++++++++++++++++++++++


# solution: 
if operation==1:
  u=n1+n2
  print ' n1+n2 = '+ str(u) 
if operation==2:
  u=n1*n2
  print ' n1*n2 = '+ str(u) 


# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK2: 
# instead of prompting for the input, read the input as
# part of the command line 
# use these commands:
#
# import sys
# n1=int(sys.argv[1])
# n2=int(sys.argv[2])
# operation=int(sys.argv[3])
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

