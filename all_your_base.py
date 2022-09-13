# def rebase(input_base, digits, output_base):
#     pass
# remove the function piece for now...  working on the algorithm first put back into function form
import numpy as np
import math

#  use the formula from the Wiki page.  First step is to convert arbitrary base number to base_10;  then convert the base_10 number to another base
#  Algorithm:  (a3a2a1)b = (a3*b^n-1) + (a2*b^n-2) (a1*b^b-3) + (a0*b^n-4)   where n is length of original number input by user (in this example n=4)
# convert a number input by user into an array of integers
input = 1316               # iput from the user
n = input
base = 8
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
# for i in range (0,len-1):
#   v3 =  base**(i+1)
  
# v = np.array([base**(len-1), base**(len-2)])

# print (v2.dot(v1))

# convert list of digits back to number
# number = int(''.join(map(str, list_of_digits)))
print(new_num)
