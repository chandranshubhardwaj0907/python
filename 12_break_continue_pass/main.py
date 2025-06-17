# This code snippet demonstrates the use of `break`, `continue`, and `pass` statements in Python loops. 
# Break
for i in range(1,21):
    print(i)
    if i == 11:
        break

# Continue

for i in range(1,21):
    if i ==10: 
        continue # continue the loop for the nexr iteration here itself
    print(i)

# Pass

for i in range(1,21):
    if i == 10:
        pass  # pass statement does nothing, just a placeholder
    print(i)
