"""
Task
Given an integer, n, and  n space-separated integers as input, create a tuple, t, of those  integers.
Then compute and print the result of hash(t)
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format
Print the result of hash(t)
"""

n = int(input("Number of elements in tuple: "))
# t = tuple(input().split())

# list1 = map(int, input().split())
# t = tuple(list1)
# print(t)
# print(hash(t))

print(hash(tuple(map(int, input().split()))))

