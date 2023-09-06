"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .

Constraints

Output Format

Output True or False for each test case on separate lines.
"""

num_of_TC = int(input("Enter Number of Test Cases : "))
for i in range(num_of_TC):
    j = int(input("Number of elements of Set A"))
    setA = set(map(int, input().split()))
    k = int(input("Number of elements of Set B"))
    setB = set(map(int, input().split()))
    print(setA.issubset(setB))
    # my_dict = {i : setA.issubset(setB)}

# print(my_dict.values())
