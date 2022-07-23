
pp=open("Counting Words assignment.txt")

content=pp.read()

print(content)

datta=content.split()

count=0

for a in datta:
    count=count+1


print(count)
 
