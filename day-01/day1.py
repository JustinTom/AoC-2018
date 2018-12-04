import argparse

parser = argparse.ArgumentParser(description="Day 1 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def part_one():
	input_values = open("input.txt", "r")
	return sum([int(frequency) for frequency in input_values])


def part_two():
	input_values = open("input.txt", "r")
	frequencies = [int(frequency.strip()) for frequency in input_values]

	sum = 0 
	repeat_flag = True
	seen_frequencies = set()

	# Make-shift fail safe to prevent it from going into an infinite loop. Can increase the value to up the amount of iterations to loop through.
	loop_count = 0
	max_loops = 10000

	while repeat_flag:
		if loop_count < max_loops:
			loop_count += 1

			for frequency in frequencies:
				sum += frequency
				if sum in seen_frequencies:
					return sum
				seen_frequencies.add(sum)
		else:
			print("Unable to find a duplicate frequency after {max} iterations - stopping...".format(max=max_loops))
			repeat_flag = False


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
