import argparse

parser = argparse.ArgumentParser(description="Day 5 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	return open("input.txt", "r").read().strip()


def part_one():
	polymer = parse_input_file()
	polymer_length = len(polymer)
	reaction = True

	while reaction:
		for letter_index in range(polymer_length):
			first_index = letter_index
			next_index = first_index + 1
			polymer_flag = False

			if next_index < polymer_length:
				first_letter = polymer[first_index]
				next_letter = polymer[next_index]

				if first_letter != next_letter and first_letter.lower() == next_letter.lower():
					polymer_flag = True
					polymer = polymer[:first_index] + polymer[next_index:]
			elif not polymer_flag:
				break

		if reaction == False:
			break

	return len(polymer)



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
