a = input()
b = input()
possible = True

for letter in b:
    if b.count(letter) > a.count(letter):
        possible = False
        break

if possible:
    print("Yes")
else:
    print("No")