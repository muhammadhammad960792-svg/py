def list_sum(apple):
    if apple ==[]:
        return 0
    return apple[0] + list_sum(apple[1:])
input("Recursive sum - add head to sum of tail until empty. Press Enter")
print(" List_sum([1, 2, 3]) =", list_sum([1, 2, 3]))
print(" List_sum([4, 5, 6]) =", list_sum([4, 5, 6]))
apple = [int(x) for x in input("Enter 4 numbers seperated by spaces:").split()]
guess = input("What is the sum of " + str(apple) + "? ")
input("list_sum adds head to list_sum(tail) until the list is empty. Press Enter")
print(" sum:", list_sum(apple), " your guess", guess)


        