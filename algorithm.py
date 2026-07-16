# Algorithm : Use the shortcut formula to get the answer instantly.
#Pseudocode : total = n* (n+1)/2
# Time cost : 1 step - stays the same no matter how big n its 
# space cost : 1 variable (total)
n=4
total = n*(n+1)/2
print("Formula way :totla = ",total,"| steps=1")

total = 0
steps = 0
for round_num in range(1,n+1):
    total += round_num
    steps += 1
print("Loop way : total = ",total,"| steps=",steps)
 

total= 0
steps = 0
for round_num in range(1,n+1):
    for point in range(1,round_num+1):
        total += 1
        steps += 1
print("Nested Loop way : total = ",total,"| steps=",steps)

