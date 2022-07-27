# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# this function should return a string.

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


    

# dont touch down - this is the test for your code.
print(increment_string("foo")) # => foo1
print(increment_string("foobar23")) # => foobar24
print(increment_string("foo0042")) # => foo0043
print(increment_string("foo9")) # => foo10
print(increment_string("foo099")) # => foo099