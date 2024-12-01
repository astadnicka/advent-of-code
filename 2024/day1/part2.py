left_column = []
right_column = []

with open('input.txt', 'r') as file:
    for line in file:

        left_number = line.strip().split()[0]
        left_column.append(int(left_number))

        right_number = line.strip().split()[1]
        right_column.append(int(right_number))
   
similarity = 0

for curr_left in left_column:
    appear = 0
    for curr_right in right_column:
        if curr_right == curr_left:
            appear+=1
    similarity+=curr_left*appear

print(similarity)