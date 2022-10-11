from random import shuffle


class Chore:
    '''
    Class used to represent chores or tasks to be assigned to members of 
    the Person class.
    
    Chores or tasks should be initialized before persons. Tasks are 
    categorized by how often they have to be performed during the week.

    Attributes
    ----------
  
    daily: list
        all tasks which need to be performed every day, appended during 
        init
    daily_copy: list
    twice: list
        all tasks which need to be performed twice per week, appended 
        during init
    twice_copy: list
    once: list
        all tasks which need to be performed once a week, appended 
        during init
    once_copy: list
    individual_tasks: list
        list of tasks which are permanently assigned to one or more 
        people, will not be assigned
    open_tasks: list
        used to store unassigned tasks

    name: str
        name of task
    time_points: int
        time required to finish the task, 1 = 10 min, 6 = 60 min
    frequency: str
        once, twice or daily; how often a task has to be performed per week
    individual: optional, default: False
        True if it is an individual task, eg. "cleaning bedroom". 
        individual tasks may be assigned to more than one person. they 
        will not be assigned randomly
    counter: default=5
        determines how often the program tries to assign the task before 
        storing it in open_tasks

    '''
    
    daily=set()
    daily_copy=[]

    twice=set()
    twice_copy=[]

    once=set()
    once_copy=[]

    individual_tasks=[]

    open_tasks=[]

    def __init__(self, name: str, time_points: int, frequency: str, 
        individual: bool = False):
        
        self.name=name
        self.tp=time_points
        self.frequency=frequency
        self.individual=individual
        self.counter=5

        match individual:
            case True:
                Chore.individual_tasks.append(self)    
            case False:
                if frequency=="once":
                    Chore.once.add(self)
                elif frequency=="twice":
                    Chore.twice.add(self)
                elif frequency=="daily":
                    Chore.daily.add(self)

    def del_task_after_dist(self):
        '''
        Removes task from copy of frequency list. Needs to be called 
        after assignment of a task.
        '''

        freq_task=self.frequency

        match freq_task:
            case "once":
                Chore.once_copy.remove(self)
            case "twice":
                Chore.twice_copy.remove(self)
            case "daily":
                Chore.daily_copy.remove(self)

def copy_frequency_lists():
    '''
    Used after all tasks/chores have been initialized.
    Copies lists: daily, twice, once for assignment
    '''
    
    for task in Chore.daily:
        Chore.daily_copy.append(task)
    for task in Chore.twice:
        Chore.twice_copy.append(task)
    for task in Chore.once:
        Chore.once_copy.append(task)

def get_random_task(frequency:str):     #not used
    '''
    Chooses a random task for assignment.

    Parameters
    ---------
    frequency: string
        "once", "twice", "daily"

    Returns
    -------
    object
        returns chore instance

    '''

    tasklist=[]    

    match frequency:
        case "once":
            for task in Chore.once_copy:
                tasklist.append(task)
        case "twice":
            for task in Chore.twice_copy:
                tasklist.append(task)
        case "daily":
            for task in Chore.daily_copy:
                tasklist.append(task)
    
    shuffle(tasklist)
    task=tasklist[0]
    return task
