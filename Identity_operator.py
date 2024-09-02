# Identity operator
a=20
b=20
if (a is b):
    print("Line1-a and b have same identity")
else:
    print("Line1-a and b have different identity")
if(id(a)==id(b)):
    print("Line2-a and b have same identity")
else:
    print("Line2-a and b have different identity")
