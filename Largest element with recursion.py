def list_max(apple):
    if len(apple) == 1:
        return apple[0]
    rest = list_max(apple[1:])
    return apple[0] if apple[0] > rest else rest
input("Recursive max - compare head to max of tail. Press Enter")
print(" list_max([3, 7, 2]) =", list_max([3, 7, 2]))
print(" list_max([8, 1, 5]) =", list_max([8, 1, 5]))


