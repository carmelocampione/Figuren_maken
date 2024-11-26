#vierkant
rij = 5
for i in range(rij):
    for j in range(rij):
        print("*",end=" ")
    print()

# driehoek
rij = 5
for i in range(rij):
    for j in range(i+1):
        print("*",end=" ")
    print()

# omgekeerde driehoek
rij = 5
for i in range(rij):
    for j in range(i,rij):
        print("*",end=" ")
    print()

# driehoek van rechts naar links
rij = 5
for i in range(rij):
    for j in range(i,rij-1):
        print(" ",end=" ")
    for a in range (i+1):
        print("*",end=" ")
    print()

# omgekeerde driehoek van rechts naar links
rij = 5
for i in range(rij):
    for j in range(i):
        print(" ",end=" ")
    for a in range(i,rij):
        print("*",end=" ")
    print()

# kerstboom
rij = 5
for i in range(rij):
    for j in range(i,rij-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
