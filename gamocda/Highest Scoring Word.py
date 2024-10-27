def high(x):
    def score(word):
        return sum(ord(char) - ord('a') + 1 for char in word)
    
    words = x.split()
    highest_score = 0
    highest_word = ""
    
    for word in words:
        current_score = score(word)
        if current_score > highest_score:
            highest_score = current_score
            highest_word = word
            
    return highest_word