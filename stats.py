def get_num_words(text):
    words = text.split()
    return len(words)

def char_counter(text):
    char_dic = {}
    
    for char in text:
        low_char = char.lower()
        if low_char not in char_dic:
            char_dic[low_char] = 1
        else:
            char_dic[low_char] +=1
    return (char_dic)
