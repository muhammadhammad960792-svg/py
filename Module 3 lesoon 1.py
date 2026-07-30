names =["sung jinwoo", "cha ha ein", "antares", "bulma", "rose"]
scores = [90,  75,   88,    62,   95]
n=len(scores)
print("==== Score Tracker (n=",n, "players) ====")
for i in range (n):
    print(i + 1 , ".", names[i], " : ", scores[i],sep="")
print()
steps = 1
print("Score at index 0 :", scores[0], "| steps =", steps, "| Theta(1) -tight bound")
print()
target = "sung jinwoo"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for",target, "| steps=", steps," |Omega(1) - best case lower bound")

target = "bulma"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for",target, "| stpes=", steps," | O(n) =",n,"- worst case upper bound")

steps = 0
target_sum = 0
print("pairs with total score =",target_sum, ":")
for i in range(n):
    for j in range (i + 1, n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(" ", names[i], "+", names[j], "=", scores[i] + scores[j])
