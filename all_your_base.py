# def rebase(input_base, digits, output_base):
#     pass
# remove the function piece for now...  working on the algorithm first put back into function form later

# the coding work and debugging is being done in colab (colab.research.google.com) and copied on to this github page here as I get various pieces working.
import numpy as np
import math

#  use the formula from the Wiki page.  First step is to convert arbitrary base number to base_10;  then convert the base_10 number to another base
#  Algorithm:  (a3a2a1)b = (a3*b^n-1) + (a2*b^n-2) (a1*b^b-3) + (a0*b^n-4)   where n is length of original number input by user (in this example n=4)
# convert a number input by user into an array of integers
input = 1316               # iput from the user, hardcoded in now for test purposes
n = input
base = 8                   # using base_8, hardcoded in for testing purposes
v1 = []

int_vec = [int(i) for i in str(n)]
# count number of elements in the number submitted by user
len = 0            
while n != 0:    
  n //= 10
  len +=1         

for i in range(0,len):
  t = i
  v1.append(base**t)
v1 = v1[::-1]

new_num = np.dot(int_vec, v1)
print(new_num)
#
#      original number was in one base and converted to base_10;  below the base_10 number will now be converted to another base
base=4        # test out the algorithm by now converting to another base.  Hardcode this base to be 4 for test purposes
# now convert the base_10 number to another base
new_base = ""     # Initialize
while new_num > 0:     # 'new_num' variable is the base_10 conversion from the original user input
  dig = int(new_num%base)
  if dig<10:
      new_base += str(dig)
  new_num //= base

new_base = new_base[::-1]  # reverse the order again
print (new_base)  
# ran a few numbers on an automatic base converter on the internet to confirm this algorithm.  This is now working thus far.  
# work still to be done for working with alphanumeric characters (ie ABCDEF for base_16 etc).  Also need to convert the code here into
# function format.  The expeptions and error trapping has not be started.
