# the problem:
"""
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
Test your code using the data we've provided.
"""
def blocks_sum(n):
    return n * (n + 1) // 2

def get_highest(blocks):
    if blocks % 2 != 0:
        ph = (blocks // 2) + 1
    else:
        ph = blocks / 2
    
    while ph > 1:
        if blocks_sum(ph) == blocks:
            return ph
        ph -= 1
    
    return "not sufficient"

def main():
    b = int(input("Enter the number of blocks: "))
    print(get_highest(b))

main()
