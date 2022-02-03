from itertools import product, permutations, combinations, combinations_with_replacements, accumulate, groupby, count, cycle, repeat
import operator

a = [1,2]
b = [3,4]
prod = product(a,b)  #[(1,3),(1,4),(2,3),(2,4)]

a = [1,2]
b = [3]
prod = product(a,b, repeat = 2)  # [(1,3,1,3),(1,3,2,3),(2,3,1,3),(2,3,2,3)]

a = [1, 2, 3, 4]
perm = permutations(a)
perm = permutations(a, 2) # permutations of length 2

a = [1, 2, 3, 4]
comb = combinations(a, 2) # combinations of length 2

comb_wr = combinations_with_replacements(a, 2) 

acc = accumulate(a)  #[1, 3, 6, 10]
acc_m = accumulate(a,func = operator.mult)  # [1, 2, 6, 24]

a = [1, 2, 4, 3]
acc_max = accumulate(a,func = max) # [1, 2, 4, 4]


def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3)
for key,value in group_obj:
    print(key, list(value))


for i in count(10):    # print infinite loop starting from 10, unless a condition satisfies
    print(i)
    if i == 15:
        break


a = [1, 2, 3]
for i in cycle(a):   # print infinite loop repeating the values of "a", unless a condition satisfies
    print(i)


a = [1, 2, 3]
for i in repeat(1, 5):   # print infinite times "1", unless a condition satisfies
    print(i)             # second argument is given to limit the repeats