'''
    Check Permutation: Given two strings, write a method to decide if one is a
    permutation of the other.

    Naive solution: sort the strings then check if they match
    Time Complexity: O(nlogn), Space Complexity: O(1)

    Better solution: first, check if the lengths match, if they do, add the
    first string in a dictionary then check if all the
    characters match.
    Time Complexity: O(n), Space Complexity: O(n)

    Missed: is it case-sensitive? Does whitespace matter?
'''


def is_permutation(str_1: str, str_2: str) -> bool:
    dict = {}

    if(len(str_1) != len(str_2)):
        return False

    for c in str_1:
        if c in dict:
            dict.update({c: dict.get(c) + 1})
        else:
            dict.update({c: 1})

    for c in str_2:
        if c in dict:
            if (dict.get(c) == 1):
                dict.pop(c)
            else:
                dict.update({c: dict.get(c) - 1})
        else:
            return False

    if len(dict) == 0:
        return True
    else:
        return False


print(is_permutation("abcd", "bcda"))
print(is_permutation("abce", "abcd"))
