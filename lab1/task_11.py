#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
	while not wall_is_on_the_right():
		if wall_is_above() and wall_is_beneath():
			move_right()
		else:
			fill_cell()
			move_right()


if __name__ == '__main__':
	run_tasks()
