import argparse

parser = argparse.ArgumentParser(description="Day 5 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	return open("input.txt", "r").read().strip()


def part_one():
	polymer = parse_input_file()
	polymer_flag = True

	while polymer_flag:
		polymer_length = len(polymer)

		for letter_index in range(polymer_length):
			first_index = letter_index
			next_index = first_index + 1

			if next_index < polymer_length:
				first_letter = polymer[first_index]
				next_letter = polymer[next_index]

				# If there is a reaction (ie. Same letter, but different capitilzation/case)
				if first_letter != next_letter and first_letter.lower() == next_letter.lower():
					# Craft new polymer string by removing the reactioned characters.
					polymer = polymer[:first_index] + polymer[next_index + 1:]
					# Have to break in order to re-evaluate the newly created polymer (as the length has now changed).
					break
					
			# If there is no more reactions in the polymer, exit the infinite loop.
			else:
				print("No more reactions")
				polymer_flag = False
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
