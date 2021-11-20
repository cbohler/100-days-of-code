import math
##################################################
#                                List Practice                                  #
# https://pynative.com/python-list-exercise-with-solutions/   #
#                                                                                    #
##################################################

#Exercise 1: Reverse a given list in Python
aList1 = [100, 200, 300, 400, 500]
#Expected Output: [500, 400, 300, 200, 100]
bList = []
revNums = ' '

length = len(aList1)
for i in range(length):
    index =  (length - 1) - i
    revNums = aList1[index]
    bList.append(revNums)
print(bList)

#Exercise 2: Concatenate two lists index-wise
#Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#Expected Output: ['My', 'name', 'is', 'Kelly']

newList = []
newword = ' '

for i in range(len(list1)):
    newword = list1[i] + list2[i]
    newList.append(newword)
print(newList)

#Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
#Given
aList = [1, 2, 3, 4, 5, 6, 7]
#Expected Output: [1, 4, 9, 16, 25, 36, 49]
power2 = 0
for i in range(len(aList)):
    aList[i] = aList[i]**2
print(aList)

#Exercise 4: Concatenate two lists in the following order
#Given:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
entry = ' '
for i in range(len(list1)):
    while(i==
        entry = list1[i] + list2[i]
        list3.append(entry)

print(list3)

#Expected Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

#Exercise 5: Given a two Python list. Iterate both lists simultaneously
#such that list1 should display item in original order and list2 in reverse order
#Given:
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

#Expected output:
#10 400
#20 300
#30 200
#40 100

#Exercise 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

#Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in
#such a way that it will look like the following list
#Given
List: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

#Sub List to be added = ["h", "i", "j"]

#Expected output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

#Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
#Given:
list1 = [5, 10, 15, 20, 25, 50, 20]
#Expected output: list1 = [5, 10, 15, 200, 25, 50, 20]

#Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
#Expected output: [5, 15, 25, 50]
