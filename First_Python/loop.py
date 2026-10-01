# for loop
# for i in range(1, 6): # it will print 5 tiemes, means 1 to 5
#     print("iterations :", i)

# iterating through a string
# for char in "python":
#     print(char)

# while loop
# count = 1
# while count <= 5:
#     print("count :", count)
#     count += 1

# break and continue

# break
# for i in range (1, 10):
#     print(i) # break the program after print 5
#     if i == 5:
#         break
#     # print(i) # break the program before print 5 (after 4)

# continue
for i in range(1, 9):
    if i % 2 == 0:
        continue
    print(i)