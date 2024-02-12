# Lists - Test your comprehension:
# - how to copy a list? (4 ways)
# - how to concatenate 2 lists? (2 ways)
# - how to add something to the end of a list?
# - how to add something in specific index?
# - how to delete last element?
# - how to delete by value?
# - how to delete by index?
# - how to count all occurrences of a value?
# - how to sort? (2 ways)
# - how to reverse? (2 ways)
# - how to skip every 2 elements?
# - make an n*n matrix of `None`s using exactly 2 lines (1st for `a=[]`).

mylist = ["1", 2, True]
mylist_2 = mylist[:]

print(mylist)
print(mylist_2)

mylist.insert(1, "orange")

print(mylist)
print(mylist_2)
