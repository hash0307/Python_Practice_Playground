"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.
"""

setA = set(map(int, input().split()))
num_otherSet = int(input())
# resultList = []
result = "True"
for _ in range(num_otherSet):
    newSet = set(map(int, input().split()))
    if not newSet.issubset(setA):
        result = "False"
        # print("False")
        break

    elif len(newSet) >= len(setA):
        result = "False"
        # print("False")
        break

print(result)
#     resultList.append(setA.issuperset(newSet))
#
# if "False" in resultList:
#     print("False")
# else:
#     print("True")
