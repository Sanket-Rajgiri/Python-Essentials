list=[ int(i) for i in input("Enter values: ").split()]

print("Before Sorting: ",list)

list.sort(reverse=True)
# we can use sorted(list,reverse=True)

print("After Sorting in descending order: ",list)
