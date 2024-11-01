def reverse_string(s):
    # Initialize an empty string for the reversed version
    reversed_str = ""
    
    # Loop through the original string in reverse order using a loop
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str


s="karim"
result=reverse_string(s)
print(result)