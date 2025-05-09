def is_isogram(string):
    string = string.lower()
    l = list(string)
    s = set(string)
    return len(l)==len(s)
