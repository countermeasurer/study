

import argparse
from bowling import get_score


parser = argparse.ArgumentParser(description='Get Bowling Score')
parser.add_argument('result', type=str, help='Input frames to get score')
args = parser.parse_args()
get_score(get_string=args.result)
