import argparse
from score_tournament import score_tournament, score_tournament_europe


parser = argparse.ArgumentParser(description='Get Bowling Score File')
parser.add_argument('input', type=str, help='Input file to get scores')
parser.add_argument('output', type=str, help='Output file to get scores')
args = parser.parse_args()
score_tournament(in_file=args.input, out_file=args.output)