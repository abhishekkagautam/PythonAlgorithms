num = int(input(" Enter number of desired Rows "))
char = input(" Enter character in the pattern")

num=num+1
#Right angled trangle
for i in range(num):
    print(char*i)

#equalatrial triangle
for i in range(num):
    print((" ")*(num-i),end="")
    print((" "+char)*i)

#inverse rignt angled triangle
print("\n")
for i in range(num-1,0,-1):
    print(char*i)

print("\n")

#invrse equalatrial triangle

for i in range(num-1,0,-1):
    print(" "*(num-i),end="")
    print((" "+char)*(i))
