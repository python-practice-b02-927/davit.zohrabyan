#!/usr/bin/python3

from pyrob.api import *

def cross():
	fill_cell()
	for i in range(2):
		move_right()
		fill_cell()
	move_left()
	move_down()
	fill_cell()
	move_up(n=2)
	fill_cell()
	move_down()
	move_right()
		

@task(delay=0.02)
def task_2_4():
	move_down(n=2)
	while not wall_is_beneath():
		move_up()
		cross()
		while not wall_is_on_the_right():
			move_right(n=2)
			cross()
		move_down(n=5)
		while not wall_is_on_the_left():
			move_left()
	move_up()
	cross()
	while not wall_is_on_the_right():
		move_right(n=2)
		cross()
	move_up()
	while not wall_is_on_the_left():
		move_left()
		
			

if __name__ == '__main__':
	run_tasks()
