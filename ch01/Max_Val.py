#/usr/bin/python3

my_list = [7, 4, 22, 1, -2, 0, 3]

print(my_list)

## This implementation is flawed as it relies on 0 to be lowest value. 
"""
def largest(A):
    my_max = 0;
    for v in A:
        if my_max < v:
            my_max = v
    return my_max
"""

### Let's set the my_max to the first value in the list/array.
##### I've also reset the function to provide the lowest number in the list.

def smallest(A):
    my_max = A[0]
    for v in A:
        if my_max > v:
            my_max = v
    return my_max

### Now the book also provides a solution using range.
### Range basically gives us a sequence of numbers increasing by 1
### and we use that range as the List index, and compare each element in the list
### against our my_max value.
##### Largest will still throw error if list is empty.
##### How many times do we use the key operation "<" ? N-1

def largest(A):
    my_max = A[0]
    for idx in range(1, len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max

### Alternate algorithm has two loops, and when properly sorted it can find the result very quickly. 
### If the conditions of the input are not perfect then the result will be very slow and burdensome. 

def alternate(A):
    for v in A:
        v_is_largest = True
        # print(v)
        for x in A:
           # print(x)
            if v < x:
                v_is_largest = False
                break
        if v_is_largest:
            return v
    return None

### Few more algorithms to solve this problem.

### This is amazingly compact, uses power of sorting and tuples to quickly pluck out the two largest.
def sorting_two(A):
    return tuple(sorted(A, reverse=True) [:2])/

### This method uses max() to get the largest value, then it makes a copy of the list
### and then removes the previous largest value from the 2nd list. 
### We return the one found value, and then search the copy list.
def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return (my_max, max(copy))

### This method tries to avoid making copies of the list. It finds the largest value.
### It then saves that value in a variable.
### It then deletes the value from the list, runs max and finds the 2nd largest value.
### It returns the first highest back to the list.
### And then returns the first and second largest values.

def mutable_two (A):
    idx = max(range(len(A)), key=A._getitem_)
    my_max = A[idx]
    del A[idx]

    second = max(A)
    A.insert(idx, my_max)
    return (my_max, second)


print(smallest(my_list))
print(largest(my_list))
print(alternate(my_list))
