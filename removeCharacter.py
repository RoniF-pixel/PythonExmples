"""Remove a character from a string"""
def remove_char(inputStr, i):
    if i < 0 or i >= len(inputStr):
        print(f"Invalid index {i}. The string remains unchanged.")
        return inputStr
 # Remove the i-th character using slicing
    resultStr = inputStr[:i] + inputStr[i + 1:]
    return resultStr
inputStr = "Hello! let's start it."
i = 7 
newString = remove_char(inputStr, i)
print(f"Original String: {inputStr}")
print(f"String after removing {i}th character : {newString}")
