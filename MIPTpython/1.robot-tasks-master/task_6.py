#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():    
    while not wall_is_beneath():    #пока стены снизу нету, идём вправо     
         move_right()
    while wall_is_beneath():        #пока стена есть, идём вправо
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()
