
"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above.
Iterate through each command in order and perform the corresponding operation on your list
"""

if __name__ == '__main__':
    N = int(input("Enter total number of commands :"))
    # print("Number of commands : ", N)

    commands = []
    list1 = []
    for i in range(N):
        i = input("Enter command : ").split()
        # print(i)
        commands.append(i)

    for command in commands:
        if command[0] == "print":
            print("Print statement from program", list1)
        elif command[0] == "insert":
            list1.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            list1.remove(int(command[1]))
        elif command[0] == "append":
            list1.append(int(command[1]))
        elif command[0] == "sort":
            list1.sort()
        elif command[0] == "pop":
            list1.pop()
        elif command[0] == "reverse":
            list1.reverse()
        else:
            print("Invalid input. Please try again")

#Print the final Output , even if not requested
print("Final output ", list1)
