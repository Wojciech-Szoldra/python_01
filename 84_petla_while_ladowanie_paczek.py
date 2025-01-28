# Pętla umieszcza w liście box elementy z listy cargo w taki sposób,
# aby być jak najbliżej maksymalnej wartości ustalonej w box_capacity

cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print('The cargo list is:', cargo)

box_capacity = 90
box = []
i = 0

while i < len(cargo) and (box_capacity - sum(box)) >= min(cargo):
    if (box_capacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print('The collected items sum is:', sum(box))
print('The elements are:', box)

# *** If w while - LAB ***

print('\n*** LAB ***')
print('\nTask 1\n')

num_max = 50
i = 0

while i < 50:
    print(f'{i} + {i+1} = {i+(i+1)}')
    i+=1