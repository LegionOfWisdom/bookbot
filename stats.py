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

def sort_on(d):
    return d["num"]

def to_be_sorted(num_char):
    sorted_list = []
    for ch in num_char:
        sorted_list.append({"char":ch, "num":num_char[ch]})
    sorted_list.sort(reverse=True, key=sort_on)    
    return sorted_list

