if __name__ == '__main__':
    n = int(input("Enter number of elements: "))

# Read inputs in a list from the user
# list1 = [] # Read input from user to list
# for i in range(0, n):
#     print("Occurence : ", i)
#     element = int(input("Enter elements : "))
#     list1.append(element)
# print("List is : ", list1)


# Read inputs from user to a map
arr = map(int, input("\n Enter Elements : ").split()) # To read input using map
list1 = list(arr)
list1.sort()
print("List is : ", list1)
print("Sorted List :", sorted(set(list1)))
print("List is : ", list1.sort())

# second_max_ele_index = list1.index(max(sorted(set(list1)))-1)
print("Runner Up Score is :", list1[list1.index(max(sorted(set(list1))))-1])