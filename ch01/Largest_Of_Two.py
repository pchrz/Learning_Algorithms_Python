#/usr/bin/python3

### Find the two largest values in an arbitrary list.

my_list = [1,2,3,4,5,6,7,25,26,40,30,20,10]

"""
My first attempt involves two loops. The first loop determins the largest # in the list.
The second loop looks to find the second highest value by running comparison against the list, it knows the highest value from the previous loop and when that number comes up it skips all comparisons. Thereby only leaving the 2nd highest number as the possible answer.
"""
### I don't think this is the most efficient solution, there should be a way to do this within the first loop. That way would be the most efficient solution. 
### Would the efficiency be (N-2)

def largest(A):
    my_max = A[0]
    for i in range(1,len(A)):
        if my_max < A[i]:
            my_max = A[i]

    my_second = A[0]
    print(my_max)
    print(my_second)
    for y in range(1,len(A)):
        if (A[y] == my_max):
            continue
        elif (my_second < A[y]):
            my_second = A[y]

    return my_second

### The Book Solution

def largest_two(A):
    my_max,second = A[:2]
    if my_max < second:
        my_max,second = second,my_max

    for idx in range(2, len(A)):
        #print(A[idx])
        if my_max < A[idx]:
            my_max,second = A[idx],my_max
        elif second < A[idx]:
            second = A[idx]
    return(my_max, second)

#print(largest(my_list))
print(largest_two(my_list))
