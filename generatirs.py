def my_generator(n):
 nums = 0
 while nums<n:
  nums+=1
  yield nums
 
 
 
value = sum(my_generator(10))
print(value)
 