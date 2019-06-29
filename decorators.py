def bold(smth):
    def inner():
        return "<b>" + smth() + "</b>"
    return inner

def btch_in_the_end(smth):
    def inner(): 
        return smth() + " BTCH"
    return inner


@bold
def hi():
    return "Hello"

print(hi())

@btch_in_the_end
def goodbye():
    return "Bye"

print(goodbye())

"""
Output:
<b>Hello</b>
Bye BTCH
"""