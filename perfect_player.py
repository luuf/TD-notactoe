'''Perfect Player'''
import collections as c
import random
def choice(states):
    for state in states:
        if getset(get_q_string(state)) in p_set:
            return state
    return random.choice(states)  
def end():
    pass
def game_win(win):
    pass
def bag(string):
    b = c.Counter({'c': 0, 'a': 0,'b': 0, 'd': 0 })
    b.update(string)
    return b
def get_q_string(state):
    string = ""
    for board in state:
        string += q_values[board]
    return string
def getset(string):     
    quotient = bag(string)
    while True:
        if quotient in monoid:
                break
        if quotient['a'] > 1:
            quotient['a'] -= 2
            if quotient in monoid:
                break
        if quotient['b'] > 2:
            quotient['b'] -= 2
            if quotient in monoid:
                break
        if quotient['c'] > 2:
            quotient['c'] -= 1
            quotient['a'] += 1
            if quotient in monoid:
                break
        if quotient['b'] > 1 and quotient['c'] > 0:
            quotient['b'] -= 2
            if quotient in monoid:
                break
        if quotient['b'] > 1 and quotient['d'] > 0:
            quotient['b'] -= 2
            if quotient in monoid:
                break
        if quotient['c'] > 0 and quotient['d'] > 0:
            quotient['c'] -= 1
            quotient['a'] += 1
            if quotient in monoid:
                break
        if quotient['d'] > 1:
            quotient['d'] -= 2
            quotient['c'] += 2
            if quotient in monoid:
                break
    return quotient
monoid = [bag(''),bag('a'),bag('b'),bag('ab'),
          bag('bb'),bag('abb'),bag('c'),bag('ac'),
          bag('bc'),bag('abc'),bag('cc'),bag('acc'),
          bag('bcc'),bag('abcc'),bag('d'),bag('ad'),
          bag('bd'),bag('abd')]
p_set = [bag('cc'),bag('bc'),bag('bb'),bag('a')]
q_values = ['c','','','cc','ad','b','b',
                'b','a','a','b','a','','b','ab',
                'd','a','d','d','a','ab','a',
                'a','','ab','b','a','a','a','b',
                'b','b','ab','ab','b','b','a','b',
                'a','b','a','b','b','a','a','a','a']

        
