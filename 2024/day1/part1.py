left_column = []
right_column = []

with open('input.txt', 'r') as file:
    for line in file:

        left_number = line.strip().split()[0]
        left_column.append(int(left_number))

        right_number = line.strip().split()[1]
        right_column.append(int(right_number))
   
left_column.sort()
right_column.sort()

sum = 0

for i in range(len(left_column)):
    sum += abs(left_column[i]-right_column[i])

print(sum)