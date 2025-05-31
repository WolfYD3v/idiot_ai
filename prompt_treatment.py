def _fill_words_map(words_map , word) :
    if not word in words_map :
        words_map[word] = 1
    else :
        words_map[word] += 1
    return words_map

def is_word_correct(word) :
    return word != ""

def create_words_map(prompt) :
    words_map = {}
    word = ""
    for letter in prompt :
        if letter not in [" " , "." , "," , "!" , ":" , "/"] :
            word += letter
        else :
            if is_word_correct(word) :
                words_map = _fill_words_map(words_map , word)
                word = ""
    if is_word_correct(word) :
        words_map = _fill_words_map(words_map , word)
    return words_map

def calculate_words_map_score(words_map) :
    score = 0
    for word_score in words_map.keys() :
        score += words_map[word_score] + len(word_score)
    return score