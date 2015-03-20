import sys

n_columns = int(sys.argv[1])
n_rows    = int(sys.argv[2])

# open repl and show how range works
# explaing ( 1, n+1 usage )

# this loop gets added last
printrow=4*' '
for column in range(1,n_columns+1):
  printrow+='%4d'%(column)

print printrow
printrow=4*(n_columns+1)*'-'
print printrow
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 1: 
# write two for loops that will build a multiplication 
# table and print to standard out.
# make sure the teacher explains ranges!
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# TASK 2: 
# there are redundant values in this table (1x2 is the same as 2x1)
# let's write a table that only writes out one of these for each product
# ++++++++++++++++++++++++++++++++++++++++++++++++++++

for row in range(1,n_rows+1):
  printrow='%3d)'%(row)
  for column in range(1,n_columns+1):
    product=row*column
    #print 'multiplying '+ str((row,column)) +' = '+str(product)
    if (row>=column):
      product = row*column
      printrow += '%4d'%(product) 
    else:
      printrow+=' '*4
  
  print printrow
   
