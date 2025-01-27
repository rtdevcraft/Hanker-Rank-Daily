#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Create a dictionary to store the frequency of each string
    string_counts = {}
    
    # Count occurrences of each string in the input array
    for s in strings:
        string_counts[s] = string_counts.get(s, 0) + 1
    
    # Create result array by looking up each query in the dictionary
    result = []
    for query in queries:
        # If query exists in dictionary, add its count, otherwise add 0
        result.append(string_counts.get(query, 0))
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
