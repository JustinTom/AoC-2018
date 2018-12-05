import argparse

parser = argparse.ArgumentParser(description="Day 3 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	input_values = open("input.txt", "r")
	return [box_id.strip() for box_id in input_values]


def part_one():
	pass


def part_two():
	pass


def main(args):
	if args.part == 1:
		result = part_one()
	elif args.part == 2:
		result = part_two()
	else:
		result = "Invalid value provided for part argument."

	print(result)


if __name__ == "__main__":
	args = parser.parse_args()
	main(args)
