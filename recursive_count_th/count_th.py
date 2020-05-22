'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
Inside the r̲e̲c̲u̲r̲s̲i̲v̲e̲_̲c̲o̲u̲n̲t̲_̲t̲h̲ directory you'll find the c̲o̲u̲n̲t̲_̲t̲h̲.̲p̲y̲ file. In this file, p̲l̲e̲a̲s̲e̲ a̲d̲d̲ y̲o̲u̲r̲ r̲e̲c̲u̲r̲s̲i̲v̲e̲ i̲m̲p̲l̲e̲m̲e̲n̲t̲a̲t̲i̲o̲n̲ t̲o̲ t̲h̲e̲ c̲o̲u̲n̲t̲_̲t̲h̲(̲)̲ m̲e̲t̲h̲o̲d̲ f̲o̲l̲l̲o̲w̲i̲n̲g̲ t̲h̲e̲s̲e̲ r̲u̲l̲e̲s̲:̲

*𝗬𝗼𝘂𝗿 𝗳𝘂𝗻𝗰𝘁𝗶𝗼𝗻 should take
in a s̲i̲n̲g̲l̲e̲ p̲a̲r̲a̲m̲e̲t̲e̲r̲ (̲a̲ s̲t̲r̲i̲n̲g̲ w̲o̲r̲d̲)̲

*𝗬𝗼𝘂𝗿 𝗳𝘂𝗻𝗰𝘁𝗶𝗼𝗻 should r̲e̲t̲u̲r̲n̲ a̲ c̲o̲u̲n̲t̲ o̲f̲ h̲o̲w̲ m̲a̲n̲y̲ o̲c̲c̲u̲r̲e̲n̲c̲e̲s̲ o̲f̲ "̲t̲h̲"̲ o̲c̲c̲u̲r̲ w̲i̲t̲h̲i̲n̲ w̲o̲r̲d̲.̲ Case matters.
Your function must utilize recursion.
I̲t̲ c̲a̲n̲n̲o̲t̲ c̲o̲n̲t̲a̲i̲n̲ a̲n̲y̲ l̲o̲o̲p̲s̲.̲

* Run python 𝘁𝗲𝘀𝘁_𝗰𝗼𝘂𝗻𝘁_𝘁𝗵.𝗽𝘆 to run the tests for your 𝗰𝗼𝘂𝗻𝘁_𝘁𝗵() function to ensure that your implementation is correct.
"""


def count_th(word):
    """
    Recursive function must always have at least
    one base case and one recursive.
    """
    # Were checking for two characters, 'th'
    # base case: 1 character or less:
    print
    if len(word) <= 1:
        return 0

    # looking at our first two characters in the string
    # if it's 'th and lower':
    if word[:2] == 'th' and word[:2].islower():
        # add 1 to our count
        # recurse through our word
        # starting from our first index:
        return 1 + count_th(word[1:])
    else:
        # if our frist 2 characters are not 'th'
        # recurse through our word:
        return count_th(word[1:])
