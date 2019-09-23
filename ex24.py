def secret(start):
    jelly = start *500
    bowl =jelly /1000
    box = bowl /100
    return jelly,bowl,box


start_dot = 10000
jelly ,bowl,box = secret(start_dot)
print(f"{jelly} {bowl} {box}")

start_dot = start_dot/10

formal = secret(start_dot)

print("{}  {}  {}".format(*formal))


