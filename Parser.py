from __future__ import print_function
import yaml
from GameState import GameState
from Requirement import Requirement
from Task import Task
from Action import Action
from NewFunctions import *
#from TestLambdas import *
#from Lambdas import *


def parse(file_name):
    game_state = GameState()
    f = open(file_name)
    quest_script_source = yaml.safe_load(f)
    f.close()
    for task_source in quest_script_source["tasks"]:
        task = fillTask(task_source)
        game_state.add_task(task)

    return game_state


def fillTask(task_source):
    task = Task()
    map(lambda req:    task.add_success_requirement(
            Requirement(eval(req))), task_source["success_requirements"])
    map(lambda req:    task.add_failure_requirement(
            Requirement(eval(req))), task_source["failure_requirements"])
    map(lambda action: task.add_success_action(
            Action(eval(action))), task_source["success_actions"])
    map(lambda action: task.add_failure_action(
            Action(eval(action))), task_source["failure_actions"])
    task.title = task_source["title"] if "title" in task_source else "No title"
    task.id = task_source["id"]
    return task