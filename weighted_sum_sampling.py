import os
import sys
import json
import random
from sets import set
import time



def test_weighted_sampling(color_weight):
    sample_colors = {}

    total_freq = 0
    for i in range(10000):
        color = weighted_sampling(color_weight)
        total_freq += 1
        if color in sample_colors:
            sample_colors[color] += 1
        else:
            sample_colors[color] = 1

    for color in sample_colors:
        print "color:", color, "freq distribution:", sample_colors[color] = 1.0 / total_freq

    print "==================================="



if __name__ == "__main__":
    color_weight = {}
    color_weight["red"] = 0.3
    color_weight["yellow"] = 0.5
    color_weight["blue"] = 0.2

#   \---\-----\--\
#     R    Y    B
    test_weighted_sampling(color_weight)
