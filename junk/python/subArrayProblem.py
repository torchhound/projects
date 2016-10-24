'''
Write an algorithm that, given a 1-dimensional array of integers, returns the sum, starting index, and ending index of the largest-summing contiguous subarray. The algorithm should compute this in linear time. That is, doubling the size of the input should double how long it takes to find the answer, quadrupling should take 4 times as long, etc.
'''

def sum(lst):
    y = 0
    for x in lst:
        y = x + y
    return y

def searchSub(array):
    start = 0
    end = 0
    if len(array) == 0 or len(array) == 1:
        return array, start, end
    else:


