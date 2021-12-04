import time
y = 10
for x in range (10):
    print(y)
    y -= 1
    time.sleep(1)
    if y == 0:
        print('0')
print("Fogo!")