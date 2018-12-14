import argparse
import re

from datetime import datetime

parser = argparse.ArgumentParser(description="Day 4 challenge of the Advent of Code 2018")
parser.add_argument("-p", "--part", type=int, choices=[1, 2], help="Determines which part of the challenge to run")


def parse_input_file():
	input_values = open("input.txt", "r")
	return [guard_schedule.strip() for guard_schedule in input_values]


def get_datetime(log):
	return log[1:17]


def get_minute_time(log):
	# Don't have to get hour value, but rather only minute as the assumption is that the hour will always at the midnight hour.
	return log[15:17]


def get_date(log):
	return log[6:11]


def get_description(log):
	return log[19:]


def parse_schedule_log(guard_schedule):
	master_schedule = {}
	guard_id = None
	asleep_time = 0
	awake_time = 0

	for log_entry in guard_schedule:
		# Sample logs: Guard #1 begins shift | falls asleep | wakes up
		description = get_description(log_entry)

		if "Guard" in description:
			group_regex = re.search("Guard #(.+?) begins shift", description)
			guard_id = group_regex.group(1)

			if guard_id not in master_schedule:
				master_schedule[guard_id] = {minute: [] for minute in range(60)}
		
		elif "asleep" in description:
			asleep_time = int(get_minute_time(log_entry))
		
		elif "wakes" in description:
			awake_time = int(get_minute_time(log_entry))

			if asleep_time and awake_time:
				for minute in range(asleep_time, awake_time):
					master_schedule[guard_id][minute].append("#")

				asleep_time = 0
				awake_time = 0

	return master_schedule


def get_sleep_count(schedule):
	count = 0
	for minute, asleep in schedule.items():
		if asleep:
			count += asleep.count("#")
	return count


def get_guard_with_most_minutes_asleep(guard_schedules):
	guard_minutes = {}
	for guard_id, guard_schedule in guard_schedules.items():
		guard_minutes[guard_id] = get_sleep_count(guard_schedule)
	return max(zip(guard_minutes.values(), guard_minutes.keys()))


def get_minute_guard_is_most_asleep(guard_id, guard_schedule):
	minute_leader = None
	occurences_leader = 0

	for minute_value, minute_log in guard_schedule.items():
		occurences = len(minute_log)

		if occurences > occurences_leader:
			minute_leader = minute_value
			occurences_leader = occurences

	return (minute_leader, occurences_leader)


def part_one():
	guard_schedule = parse_input_file()
	guard_schedule.sort(key=get_datetime)
	guard_sleep_schedules = parse_schedule_log(guard_schedule)

	total_sleep, guard_id = get_guard_with_most_minutes_asleep(guard_sleep_schedules)
	minute_value, occurences = get_minute_guard_is_most_asleep(guard_id, guard_sleep_schedules[guard_id])

	print("Guard ID: {} slept a total of {} minutes".format(guard_id, total_sleep))
	print("Said guard sleeps the most on minute {} at {} times.".format(minute_value, occurences))

	return int(guard_id) * int(minute_value)


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
