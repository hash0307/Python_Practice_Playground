elements_in_set = int(input("Enter number of elements in the set : "))
print(elements_in_set)
setA = set(map(int, input().split()))
print(setA)
other_set = int(input("Enter number of other set : "))
print(other_set)
mutation_set = []
for i in range(other_set):
    i = input("Enter command : ").split()
    opr, arg = i[0], i[1]
    print(opr, arg)
    inner_set = set(map(int, input("Enter set elements : ").split()))
    if opr == "intersection_update":
        setA.intersection_update(inner_set)
    elif opr == "update":
        setA.update(inner_set)
    elif opr == "difference_update":
        setA.difference_update(inner_set)
    elif opr == "symmetric_difference_update":
        setA.symmetric_difference_update(inner_set)
    else:
        print("Please enter correct method on set. Try Again.")
    # print(i)

print(sum(setA))