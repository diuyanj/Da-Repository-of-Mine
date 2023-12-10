# given a list of dictionaries and a list of named variables
# find the dictionary index to travel to all variables with the shortest path

# so heres the hypothetical blocks with the stuff that either is or isnt there but its always listed
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True   
    }
]

# and heres the stuff you want to be on a block
valued_places = ["gym", "school", "store"]

# initial function
def best_location(blocks, values):
    results = []
    blocks_by_distance = []
    for i in range(len(blocks)):
        results.append(ar(blocks, values, i))
    for result in results:
        a = []
        for dict in result[1]:
            for d in dict:
                a.append(abs(d - result[0]))
        blocks_by_distance.append((result[0], (sum(a))))
    FINAL_FUCKING_ANSWER = min(blocks_by_distance,key=lambda x: x[1])
    print(f"block {{{FINAL_FUCKING_ANSWER[0]}}}, has the shortest distance traveled of {{{FINAL_FUCKING_ANSWER[1]}}}")
    return FINAL_FUCKING_ANSWER

# i dont remember
def ar(blocks, values, start):
    results = []
    for value in values:
        results.append(ar2(blocks, value, start, start))
    return (start, results)

# yay recursion! did i spell that right. nothing looks right anymore...
def ar2(blocks, value, current_block, end_block, increment=True, size_of_increment=1):
    # increment tells it to index up or down. i probably could have named it something else but i cant think
    # size of increment does what it sounds like
    if not increment:
        size_of_increment+= 1
    if end_block == len(blocks)-1:
        increment = not increment

    if blocks[current_block][value]:
        if current_block < 0:
            current_block = len(blocks)-1
        # current block: name of the current valued place: distance to travel to that block ;)
        return {current_block: {value: abs(current_block-end_block)}}
    
    # little bit of switcheroo for some algorithmic searching
    elif increment:
        increment = not increment
        return ar2(blocks, value, current_block+size_of_increment, end_block, increment, size_of_increment)
    else:
        increment = not increment
        return ar2(blocks, value, current_block-size_of_increment, end_block, increment, size_of_increment)

best_location(blocks, valued_places)