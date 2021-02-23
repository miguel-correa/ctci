'''Is Unique: Implement an algorithm to determine if a string has all unique
    characters. What if you cannot use additional data structures?
    Naive solution: two loops, if i == j return false
    time complexity = O(n^2), space complexity = O(1)
    Better solution: using a set (see is unique)
    With no extra space: sorting the string.
'''


def is_unique(string: str) -> bool:
    '''Time complexity: O(n)
        Space complexity: O(n)
    '''
    s = set()
    for c in string:
        if c in s:
            return False
        else:
            s.add(c)
    return True


def is_unique_v2(string: str) -> bool:
    '''Time complexity: O(n)
        Space complexity: O(1)
    '''
    string = sorted(string)
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            return False
    return True


print(is_unique_v2("not unique"))
print(is_unique("True"))
