def left_rotate(n):
    arr=[1,2,3,4,5]
    n=n%len(arr)
    return arr[n:] + arr[:n]
input("left_rotate(n) shofts [1,2,3,4,5]left by n positions.Press Enter")
print(" left_rotate (1) =" ,left_rotate(1))
print(" left rotate (2) =", left_rotate(2))
n = int(input("Rotate by how many? (try 6 or 7):"))
guess = input("What is left_rotate(" + str(n) +")? ")
input("Slice form index n to end , then attach the first n elements.Press Enter")
print("left_rotate(" + str(n) + ") =", left_rotate(n), " your guess:", guess)