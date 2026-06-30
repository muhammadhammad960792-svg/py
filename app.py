n=int(input("enter number :"))

f=open("class_notes.txt",'r')

print(f.read(n))
f.close()

print()

file =open("Class_notes.txt","r")
lines =file.readlines()
file.close()
print("Total lines:",len(lines))
for i in range(len(lines)):
    print(i + 1, "->",lines[i].strip())

