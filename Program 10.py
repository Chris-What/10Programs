#Program 10

num_list = []

for i in range(100):
    if i % 10 != 0:
        num_list.append(i)

print(f"The numbers from 0 to 100, excluding those ending in 0, are {num_list}.")