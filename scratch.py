# Add up and print the sum of the all of the minimum elements of each inner array:
the_arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.

# set total to zero
total = 0

# for loop through all indexes using i
for arr in the_arr:
    # add total to total plus min(arr[i])
    total = total + min(arr)

print(total)
