#!/usr/bin/env python3

""" Calculate, show the time a chicken needs to be in the oven. """

import argparse

def main():
    """ Main entry point. """
    parser = argparse.ArgumentParser(description='Calculate chicken roast time.')
    parser.add_argument('weight',
                        metavar='kg',
                        type=float,
                        help="Weight of chicken in kilograms")
    args = parser.parse_args()
    weight_of_chicken = float(args.weight)
    time_in_oven = 30 + 20 * weight_of_chicken / .5
    print(time_in_oven)


if __name__ == "__main__":
    main()
