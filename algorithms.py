#remove duplicates from arrays
list_one = [1,2,3,4,5,6,7,8,9,0]
list_two = [1,3,6,9,0]
list_three = []
for value in list_one:
    if value in list_two:
        next
    else:
        list_three.append(value)
print(list_three)

#find largest element in array

list1 = [1,2,3,4,5,6,7,8,9,99,99999]
max = 0
for i in list1:
    if i > max:
        max=i
print(max)
#find smallest element in array
list2 = [1,2,3,4,5,6,7,8,9,9,9,9,999,99,999,1234567]
min = list2[0]
for x in list2:
    if x < min:
        min=x
print(min)
#duplicate an array
try_to_dup = [1,2,3,4,5]
#want result {[1,2,3,4,5,1,2,3,4,5]}

for dup in range(0,len(try_to_dup),1):
    try_to_dup.append(dup+1)

print(try_to_dup)
a = [1,2,3,4,5]
b = a + a
print(b)

#create tree with *
#character count 9*2-1
#stars = line number *2 -1
count = 1
lines = 9
white_space = " "
star_symbol = "*"
while count <= lines:
    space = (lines - count)
    stars = count * 2 - 1
    print(f'{white_space*space}{star_symbol*stars}{white_space*space}')
    count = count + 1
