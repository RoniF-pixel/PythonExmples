"""Remove a character from a string"""
def remove_char(input_Str, i):
    if i < 0 or i >= len(input_Str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_Str
 #Remove the i-th character using slicing
    result_Str = input_Str[:i] + input_Str[i + 1:]
    return result_Str
sentence = "Hello! elet's start it."
j = 7 
new_String = remove_char(sentence, j)
print(f"Original String: {sentence}")
print(f"String after removing {j}th character : {new_String}")
