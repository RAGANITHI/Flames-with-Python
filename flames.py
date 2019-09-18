x=input("enter name 1")
y=input("enter name 2")
x1,y1=[],[]
for im in x:
    x1.append(im.lower())

for il in y:
    y1.append(il.lower())

f=["f","l","a","m","e","s"]

x2,y2=x1,y1
if len(x1)>len(y1):
    for a in x1:
        if a in y1:
            x2.remove(a)
            y2.remove(a)
        else:
            pass
    
else:
    for a in y1:
        if a in x1:
            x2.remove(a)
            y2.remove(a)
        else:
            pass
print(x2,y2)

c= len(x2)+len(y2)

print(c)

d=len(f)

while(d>1):
    v=c%d
    f.pop(v)
    d=d-1
if f[0]=="f":
    print("Friends")

if f[0]=="l":
    print("lovers")

if f[0]=="a":
    print("acquaintences")

if f[0]=="m":
    print("marriage")

if f[0]=="e":
    print("enemies")

if f[0]=="s":
    print("sisters")
