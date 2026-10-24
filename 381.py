x = 0
y = 0

while True:
    line = input()
    if line == "Treasure!":
        break

    direction, steps = line.split()
    steps = int(steps)

    if direction == "North":
        y += steps
    elif direction == "South":
        y -= steps
    elif direction == "East":
        x += steps
    elif direction == "West":
        x -= steps

print(x, y)