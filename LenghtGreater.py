""" A program to identify words with length of greater than L """
def find_words(words, H):
    #Create an empty list to store words greater than H
    result = []

    for i in words:
    #Check if the length of the i is greater than H
        if len(i) > H:
    #If yes, append it to the result list
            result.append(i)
    return result
word_list = ["clue", "christmas", "news", "introduction", "newspaper", "fueles"]
L = 6
long_words = find_words(word_list, L)
print(f"Words longer than {L} characters: {long_words}")