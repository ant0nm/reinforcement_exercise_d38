def longestConsecutive(string_array, k):
    if len(string_array) == 0 or k < 0 or k > len(string_array):
        return ""
    else:
        max_combo = ""
        for index in range(len(string_array)):
            current_combo = ""
            if index + (k-1) < len(string_array):
                for i in range(k):
                    current_combo += string_array[index + i]
                if len(current_combo) > len(max_combo):
                    max_combo = current_combo
            else:
                break
        return max_combo

# testing out the function
# empty array
strings = []
k = 0
print(longestConsecutive(strings, k))

# negative k
strings = ["how", "are", "you"]
k = -1
print(longestConsecutive(strings, k))

# k > len(strings)
strings = ["hello", "world"]
k = 3
print(longestConsecutive(strings, k))

# my test
# should return 'Antonheywhat'
strings = ["my", "name", "is", "Anton", "hey", "what", "up"]
k = 3
print(longestConsecutive(strings, k))

# test 1 on Alexa
strings = ['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus']
k = 3
print(longestConsecutive(strings, k))

# test 2 on Alexa
strings = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
k = 2
print(longestConsecutive(strings, k))
