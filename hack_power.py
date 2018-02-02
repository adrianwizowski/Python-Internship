from collections import OrderedDict
from operator import itemgetter

def hack_calculator(hack, phrases, letters):
    '''Function calculates power of hack provided by brave hacker used to hack reality and fight corporations.
    Function takes 3 parametrs:
    hack: type string - used to calculate hack power from letters in it. Eg. hack = 'baaca'.
    phreses: type dict - add additional hack power to result, if hack contains a phrase from that dict.
    Eg. phrases = {'baa': 20, 'ba': 10}
    letters: type dict - collection of letters that might be used in hack with their power.
    Eg. letters = {'a': 1, 'b':2, 'c':3}
    In hack you can use only letters from letters dict. Otherwise the return of fnction will be 0.
    Eg if hack = 'baad' and there is no 'd' in letters dict, hack power = 0.'''

    hack_power = 0
    for letter in hack:
        if letter not in letters:
            #I guess there is no point of calculating any futher if there is ineffective letter in our string.
            return hack_power  # got 0

    hack_phrases_copy = hack[:] #better copy than sorry.
    #sorting phrases dict so the more powerful phrases will be counted first
    sorted_phrases = OrderedDict(sorted(phrases.items(), key=itemgetter(1), reverse=True))

    for phrase in sorted_phrases.keys():
        if phrase in hack_phrases_copy:
            hack_power += phrases[phrase] * hack_phrases_copy.count(phrase)
            #phrases can't overlap, thats why counted phrases will be deleted from hack
            hack_phrases_copy = hack_phrases_copy.replace(phrase, '')

    hack_letters_copy = hack[:]
    for letter in letters.keys():
        for i in range(1,hack_letters_copy.count(letter) +1):
            hack_power += letters[letter] * i

    return hack_power