#/usr/bin/python3

### Leetcode problem:
##### https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Goal is to analyze a string of characters and find a subset of unique characters
### that don't repeat.  


s = "abcabcbb"
#s = "p"

def lengthOfLongestSubstring(s: str):
    ### First Attempt ###
    #####################
    ### Address corner case of empty string.
    if len(s) == 0:
        return 0

    ### For strings length 1 or more, we need to keep track of our substrings in a set.
    ### We initially populate our set with the first character in the string, as the minimum value. .
    ### Then we need a loop to go through our string, and analyze each chunk of characters.
    ### if character does not repeat add it to a new_substring, then compare it to our largest
    ### discovered substring longest_substring, if greater than assign a new greatest value. 
    longest_substring = s[0]
    current_substrings = set(longest_substring)
    #print(longest_substring)
    #print(current_substrings)

    for character in s[1:]:
        #print(character)
        #print(longest_substring)
        #print(current_substrings)
        next_substrings = set(character)
        for substring in current_substrings: 
            if character not in substring:
                new_substring = substring + character
                next_substrings.add(new_substring)
                if len(new_substring) > len(longest_substring):
                    longest_substring = new_substring

        current_substrings = next_substrings.copy()

    return len(longest_substring)
   
    ### I'm not happy with this solution. It works but it's not optimal, there are a 2 For loops 
    ### and a lot of if statements. I feel like it can be cleaned up.

    ### That said I do appreciate Python here, and how readable it is. It's tools like X not in Y. 
    ### Overall the language is supremely understandable when doing complex tasks like these. 

#print(lengthOfLongestSubstring(s))

def sliding_window(s: str):
    ### Second Attempt ###
    ######################
    ### Using sliding window algorithm

    ### Using this method we can cut down complexity to O(n)
    print(s)
    chSet = set()
    ### Sliding window uses left pointer and a right pointer. Right pointer moves to the right to test values.
    lp = 0
    result = 0    

    for rp in range(len(s)):
        #print(rp)
        #print(s[rp])
        #print(chSet)
        while s[rp] in chSet:
            #print(rp)
            #print(lp)
            #print(chSet)
            chSet.remove(s[lp])
            lp += 1
        chSet.add(s[rp])
        #print(chSet)
        #print(rp)
        #print(lp)
        result = max(result, rp - lp + 1)
        print(result)
    return result


print(sliding_window(s))



    
