
def count_words(words: str):
    count = len(words.split())
    return count


def count_char(words: str):
    word_dict = {}
    for i in words:
        if i.isspace() or i.isalpha() == False:   # skip any whitespace char
            continue
        ch = i.lower()
        word_dict[ch] = word_dict.get(ch, 0) + 1

    # sort by count (descending)
    items = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    result = "\n".join(f"{k}:{v}" for k, v in items)
    return result
