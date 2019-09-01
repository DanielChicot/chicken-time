#!/usr/bin/env python3

import sys

weight_of_chicken = float(sys.argv[1])

# time in the oven = 30 minutes plus 20 minutes for each half kg of bird.
time_in_oven = 30 + 20 * weight_of_chicken / .5

print(time_in_oven)
