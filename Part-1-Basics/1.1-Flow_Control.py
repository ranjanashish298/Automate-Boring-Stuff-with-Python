import time

## A simple while loop that asks for the user's name until they enter "random".

# while True:
#     print("Enter your name:")
#     name= input()
#     print("Welcome", name)
#     if name == "break":
#         break
#     #eval(name)
# print("End")

# ## Some shell commands that can be executed using the os module.
# expression = input("Enter a shell command: ")
# result = os.system(expression)
# print("Result:", result)

## fiveTimes.py
print("My name is")
for i in range(5):
    print(f"Jimmy {i} times")

## Gauss.py
total = 0
start_time = time.time()

for i in range(103231131311231):
    total = total + i
    current_time = time.time()
    if current_time - start_time > 5:
        break
print(total)