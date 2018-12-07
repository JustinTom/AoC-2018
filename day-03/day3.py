import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Day 3 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	input_values = open("input.txt", "r")
	return [specs.strip() for specs in input_values]


def setup_fabric():
	fabric_height = 1000
	fabric_width = 1000
	return np.chararray([fabric_height, fabric_width], itemsize=4, unicode=True)
	# return [["." for x in range (fabric_width)] for y in range(fabric_height)]


def parse_specifications(spec_data):
	# Sample Spec Data - '#1 @ 100,366: 24x27'
	spec_sections = spec_data.split(" ")

	spec = {
		"number": spec_sections[0][1:],
		"x_start": int(spec_sections[2].split(",")[0]),
		"y_start": int(spec_sections[2].split(",")[1][:-1]),
		"width": int(spec_sections[3].split("x")[0]),
		"height": int(spec_sections[3].split("x")[1])
	}

	return spec


def update_fabric_grid(fabric, spec):
	start_height = spec["y_start"]
	start_width = spec["x_start"]

	for height_position in range(spec["height"]):
		for width_position in range(spec["width"]):
			target_height = start_height + height_position
			target_width = start_width + width_position

			# Set the value to 'X' if there is an existing value there - else set the value.
			fabric[target_height, target_width] = "X" if fabric[target_height, target_width] != "" else spec["number"]


def part_one(part_two=False):
	fabric = setup_fabric()
	claim_list = parse_input_file()
	specs = [parse_specifications(spec) for spec in claim_list]

	for spec in specs:
		update_fabric_grid(fabric, spec)

	if part_two:
		return fabric, specs

	return "The total number of square inches of fabric that are within two or more claims is: " + str(fabric.count("X").sum())


def part_two():
	fabric, specs = part_one(part_two=True)

	for spec in specs:
		number_id = spec.get("number")
		area = int(spec.get("width")) * int(spec.get("height"))

		if np.count_nonzero(fabric == number_id) == area:
			return "The ID of the only claim that does not overlap is: {id}".format(id=number_id)

	return "Unable to find a number ID who has an un-affected area of fabric."



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
