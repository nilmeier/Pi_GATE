# third coding challenge!

# You will learn about:
# - defining numpy ranges
# - multiplying and adding arrays
# - plotting results
# - defining functions

# this is the modification of the original script to have:
# a function called for the value
# b returned

import matplotlib.pyplot as plt
import numpy as np
import sys

b=0
xmax = int(sys.argv[1])
m    = int(sys.argv[2])
if len(sys.argv)==4:
  b    = int(sys.argv[3])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 1: 
# - using xmax as the maximum value, create an array of 
#   values from 0 to xmax.
# - multiply all of those values by m
# - review the results with the teacher. 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

x=np.arange(xmax+1)
y=m*x

# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 2: 
# - write a function line(m,x,b) that will multiply 
#   all values by m and add b... ( ie: y=m*x+b ) 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 3 (optional): 
# - what about another equation, like y=m*x*x + b?  
# - what if x went from -xmax to xmax instead of 0 to xmax?
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# 



plt.plot(x,y,'-o')
plt.grid()

plt.xlabel('x')
plt.ylabel('y = '+ str(m) +'*x'+'+'+str(b))
plt.show(block=False)

print "x: "+str(x)
print "y: "+str(y)


import rlcompleter; import readline; readline.parse_and_bind("tab: complete")
import code; code.interact(local=locals())


