# Description:
# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The day_1.txt string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vovels="aeiou"
    count = 0
    for ch in vovels:
        count+= list(sentence).count(ch)
    return count