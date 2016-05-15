"""
test for merge function for 2048 game.
"""
import merge_2048_game

test = merge_2048_game 

print test.merge([2])
print test.merge([2,0,2,2])
print test.merge([2,8,2,2])
print test.merge([2,8,2,2])
print test.merge([16,8,2,2])
print test.merge([16,8,32,8,8,2,4,4,8])
