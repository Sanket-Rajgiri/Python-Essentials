gift_presented_to = [2, 1, 5, 3, 4]
# or we can take input as gift_presented_to= [int(i) for i in input("Enter values: ").split()]

n=len(gift_presented_to)

#initalizing array
gift_received_from = [0]*(n)

#logic
for i in range(0,n):
 x = gift_presented_to[i]
 gift_received_from[x-1]=i+1

  #output
print(gift_received_from)
