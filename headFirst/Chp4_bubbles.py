scores = [60, 50, 60, 58, 54, 54,
           58, 50, 52, 54, 48, 69,
           34, 55, 51, 52, 44, 51,
           69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
        .33, .31, .25, .29, .27, .22,
        .31, .25, .25, .33, .21, .25,
        .25, .25, .28, .25, .24, .22,
        .20, .25, .30, .25, .24, .25,
        .25, .25, .27, .25, .26, .29]

highest_score = 0

# Find length of scores list
length = len(scores)

# Iterate through scores list to store associated bubble solution
# to corresponding score value
for i in range(length):
    print('Bubble solution: #', i, ' score', scores[i])
    if scores[i] > highest_score:
        highest_score = scores[i]

print('Bubbles tests:', length)
print('Highest bubble score', highest_score)

# List the bubble solutions w/ the highest score
highScr = []
for j in range(length):
   if scores[j] == highest_score:
       highScr.append(j)

print('Solutions with highest score: ',highScr)

# Find the cheapest cost from the list of bubble solutions w/
# the highest bubbles score.

best_choice = 0 # variable to store index #
cost = 100.0 # variable to hold lowest cost value
for k in range(length):
    if scores[k] == highest_score and costs[k] < cost:
        best_choice = k
        cost = costs[k]        
print('Solution #' , best_choice , 'is the most effective with a cost of', cost) 
