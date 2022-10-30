#!/usr/bin/env python3

""" Calculate, show the time a chicken needs to be in the oven. """

import argparse
import re
from pprint import pprint
from datetime import time, tzinfo, timedelta


def main():
    """ Main entry point. """
    parser = argparse.ArgumentParser(description='Calculate chicken roast time.')
    parser.add_argument('weight',
                        type=float,
                        help="Weight of chicken in kilograms")
    parser.add_argument('time',
                        help="Time to carve")
    args = parser.parse_args()
    weight_of_chicken = float(args.weight)
    time_re = re.compile(r"^(\d{2}):(\d{2})$")
    match = time_re.match(args.time)
    carve_time = timedelta(hours=int(match.group(1)), minutes=int(match.group(2)))
    roasting_time = timedelta(minutes=(30 + 20 * weight_of_chicken / .5))
    resting_time = timedelta(minutes=15)
    in_oven_time = carve_time - roasting_time - resting_time
    oven_on_time = in_oven_time - timedelta(minutes=15)
    print(oven_on_time)
    print(in_oven_time)


if __name__ == "__main__":
    main()
