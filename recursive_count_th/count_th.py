'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    #the count is initialized and set to zero
    if "th" in word:
        #checks if there's a th in the word and if so it replaces it. l is a placeholder because without it other letters combining would create th later in the recursion
        p = word.replace("th", "l", 1)
        count += 1
        #recursively calls the function to see if there's still th in the word
        return count + count_th(p)
    else:
        # if there's no more th the count is returned
        return count
