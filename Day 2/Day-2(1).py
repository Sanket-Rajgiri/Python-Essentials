#Assignment Day-2 Remove all occurences of an element from a list


li=[1,2,1,6,4,2,7,3,2,9,6,0,2,5,8]

print(li)

# Remove all the two's from list

for i in li:
  if(i==2):
    li.remove(2)


print(li)