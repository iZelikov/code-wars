def get_count(sentence):
    vovels="aeiou"
    count = 0
    for ch in vovels:
        count+= list(sentence).count(ch)
    return count