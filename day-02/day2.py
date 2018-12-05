import argparse

from collections import Counter

parser = argparse.ArgumentParser(description="Day 2 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	input_values = open("input.txt", "r")
	return [box_id.strip() for box_id in input_values]


def part_one():
	def letter_count_exists(id_string, count):
		for letter in id_string:
			if id_string.count(letter) == count:
				return True
		return False
	
	box_ids = parse_input_file()
	two_count = 0
	three_count = 0

	for box_id in box_ids:
		if letter_count_exists(box_id, 2):
			two_count += 1
		if letter_count_exists(box_id, 3):
			three_count += 1

	return two_count * three_count


def part_two():
	box_ids = parse_input_file()
	for index_a, box_id_a in enumerate(box_ids):
		for box_id_b in box_ids[index_a:]:
			differing_letters = {}
			differ_count = 0

			for letter_index in range(len(box_id_a)):
				if box_id_a[letter_index] != box_id_b[letter_index]:
					differ_count += 1
					differing_letters[letter_index] = differ_count

			if differ_count == len(differing_letters) == 1:
				differing_letter_index = list(differing_letters.keys())[0]
				return box_id_a[:differing_letter_index] + box_id_a[differing_letter_index + 1:]


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
