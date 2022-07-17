# For K
K = ""
j = 5
i = 0

for row in range(0,7):
    for col in range(0,7):
        if (col == 1 or ((row == col + 1) and col != 0)):
            K = K + "#"
        elif (row == i and col == j):
              K = K + "#"
              i = i + 1
              j = j - 1
        else:
            K = K + " "
    K = K + "\n"

print(K)

#For I
for rows in range(7):
    for columns in range(7):
        if ((rows == 0 or rows == 7 - 1) or (columns == 7 // 2)):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
# For S
S = ""
for row in range(0,7):
    for col in range(0,7):
        if (((row == 0 or row == 3 or row == 6) and col > 1 and col < 5) or (col == 1 and (row == 1 or row == 2 or row == 6)) or (col == 5 and (row == 0 or row == 4 or row == 5))):
            S = S + "#"
        else:
            S = S + " "
    S = S + "\n"
print(S)

# For H
H = ""
for row in range(0,7):
    for col in range(0,7):
        if ((col == 1 or col == 5) or (row == 3 and col > 1 and col < 6)):
            H = H + "*"
        else:
            H = H + " "
    H = H + "\n"
print(H)

# For O
O = ""
for row in range(0,7):
    for col in range(0,7):
        if (((col == 1 or col == 5) and row != 0 and row != 6) or ((row == 0 or row == 6) and col > 1 and col < 5)):
            O = O + "#"
        else:
            O = O + " "
    O = O + "\n"
print(O)

# For R
R = ""
for row in range(0,7):
    for col in range(0,7):
        if (col == 1 or ((row == 0 or row == 3) and col > 1 and col < 5) or (col == 5 and row != 0 and row < 3) or (col == row - 1 and row > 2)):
            R = R + "#"
        else:
            R = R + " "
    R = R + "\n"
print(R)

# For E
E = ""

for row in range(0,7):
    for col in range(0,7):
        if (col == 1 or ((row == 0 or row == 6) and (col > 1 and col < 6)) or (row == 3 and col > 1 and col < 5)):
            E = E + "#"
        else:
            E = E + " "
    E = E + "\n"

print(E)

