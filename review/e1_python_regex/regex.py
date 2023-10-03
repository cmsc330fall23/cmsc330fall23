'''Write a regular expression with a person's title and their bountiy separated by a colon and a space. The bounty is a number
with a common between every 3 numbers and a dollar sign at the beginning of the number.
The title can contain multiple words but each word has to start with a capital letter. Load a data structure where the key is the person's title
and the value is their bounty.
'''
import re
from functools import reduce

bounties = ["Monkey D Luffy: $30,000,000", "Zoro the Pirate Hunter: $60,000,000", "Buggy the Clown: $15,000,000",
             "Arlong the Saw: $20,000,000","Gold Roger: ???", "Mihawk: Bounty Cancelled"]
def load_bounties(bounties):
    res = {}
    r = r'^(([A-Z][A-Za-z]* )*[A-Z][A-Za-z]*): \$((\d{1,3},(\d{3},)*\d{3})|\d{1,3})$'
    for bounty in bounties:
        match = re.fullmatch(r,bounty)
        if match:
            res[match[1]] = match[3]
    return res
    pass

'''
Given a list of people and their bounties calculate the total bounty amount. Hint use load bounties first.
'''
def total_bounty(bounties):
    data = load_bounties(bounties)
    bounty_amounts = list(map(lambda x: int(x.replace(',','')), data.values()))
    return reduce(lambda a,h: a + h, bounty_amounts, 0)
    pass
