"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    lenth = len(line)
    sort = []
    l_no = 0
    #concetrate list by removing zero value
    for every_no in line:
        if every_no == 0:
            pass
        else:
            sort.append(every_no)
    while len(sort) < lenth:
        sort.append(0)
    #Iterate over the line input and calculate
    while l_no < len(sort)-1:
        if sort[l_no] != 0 and sort[l_no+1] != 0 and sort[l_no] == sort[l_no+1]:
            sort[l_no] += sort[l_no+1]
            del sort[l_no+1]
            while len(sort) < lenth:
                sort.append(0)
        l_no += 1
    return sort

