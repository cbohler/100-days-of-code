#HackerRank Challenge
#Introduction to Sets

#A set is an unordered collection of elements without duplicate entries.
#When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

    ##Example

    ##	print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
    ##	{0, 1, 2, 3, 4, 5, 6, 9, 12, 22}
    ##
    ##	print(set('HackerRank'))
    ##	{'n', 'a', 'e', 'r', 'H', 'k', 'R', 'c'}
    ##
    ##	print(set("HackerRank"))
    ##	{'n', 'a', 'e', 'r', 'H', 'k', 'R', 'c'}
    ##	print(set((1,2,3,4,5,5)))
    ##	{1, 2, 3, 4, 5}
    ##	print(set(['H','a','c','k','e','r','r','a','n','k']))
    ##	{'n', 'a', 'e', 'r', 'H', 'k', 'c'}
    ##	print(set(set(['H','a','c','k','e','r','r','a','n','k'])))
    ##	{'e', 'r', 'H', 'k', 'n', 'c', 'a'}
    ##	print(set({'Hacker' : 'DOSHI', 'Rank': 616}))
    ##	{'Rank', 'Hacker'}
    ##	print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
    ##	{(0, 'H'), (9, 'k'), (7, 'a'), (3, 'k'), (5, 'r'), (2, 'c'), (6, 'r'), (4, 'e'), (1, 'a'), (8, 'n')}

##Basically, sets are used for membership testing and eliminating duplicate entries.

                        ##################  Problem  #######################
## Now, let's use our knowledge of sets and help Mickey.
## Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

## Formula used: Avg. = (Sum of District Heights)/(Total number of Distinct Heights)

##  Function Description #######################
##  Complete the average function in the editor below.
##  average has the following parameters:
##
##  1. int arr: an array of integers
##
##  2. Returns:  (float): the resulting float value rounded to 3 places after the decimal
##
##  Input Format
##
##      STDIN                                      Function
##      -----                                      --------
##      10                                         arr[] size N = 10
##      161 182 161 154 176 170 167 171 170 174    arr = [161, 181, ..., 174]
##
##  -> SAMPLE OUTPUT: 168.375

#   Algorithm
#
#   Ask user for number of integers : N
#   Ask for N number of values: nums
#   Store (nums) in arr of length (N)

#   Set arr to remove duplicates
#   Average all numbers instored in arr
#   Return the result in a float

def average(array):
    arr2 = set(arr)
    length = len(arr2)
    for i in range(length):
        avg = sum(arr2)/(float(length))
    return avg

if __name__ == '__main__':
    n = 10
    arr= [161,182, 161, 154, 176, 170, 167, 171, 170, 174]
    #n = int(input())
    #arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



