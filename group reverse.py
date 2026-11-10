def group_reverse(n):
    arr =[1,2,3,4,5,6]
    for i in range(0,6,n):
        arr[1:1+n] = arr[1:i+n][::-1]
    return arr
input("group_reverse(n) reverse[1,2,3,4,5,6] in chunks of n.Press Enter")
print( " group_reverse(2) =", group_reverse(2))
print(" group_reverse(3)",group_reverse(3))