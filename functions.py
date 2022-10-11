from random import shuffle
import Person as P
import Chore as C



def chore_to_person(person, chore, day: str):
    
    task=chore

    person.subtract_task_tp_from_persons_day(day, task)
    person.add_task_to_day_list(day, task)

def print_week(person):
    '''
    Prints readable overview of person's tasks

    Parameters
    ----------
    person : object
    '''

    mon=[]
    tue=[]
    wed=[]
    thu=[]
    fri=[]
    sat=[]
    sun=[]

    for task in person.monday_chores:
        mon.append(task.name)
    for task in person.tuesday_chores:
        tue.append(task.name)
    for task in person.wednesday_chores:
        wed.append(task.name)
    for task in person.thursday_chores:
        thu.append(task.name)
    for task in person.friday_chores:
        fri.append(task.name)
    for task in person.saturday_chores:
        sat.append(task.name)
    for task in person.sunday_chores:
        sun.append(task.name)


    print(f"{person.name}'s tasks on\nmonday: {mon}\ntuesday: {tue}\nwednesday: {wed}\nthursday: {thu}\nfriday: {fri}\nsaturday: {sat}\nsunday: {sun}")



def distribution_of_daily():
    '''
    Assigns all daily tasks randomly to people. if a person does not 
    have enough time points, another person is chosen.
    Uses shuffle from random module to shuffle list of person instances
        
    '''

    for task in C.Chore.daily_copy:

        distribution_check=False
        counter=task.counter
        
        while counter!=0 and distribution_check==False:

            counter=counter-1
                
            week=["mon","tue", "wed", "thu", "fri", "sat", "sun"]
            
            for day in week:
                shuffle(P.Person.people)
                chosen_person=P.Person.people[0]
                if chosen_person.time_for_task_check(day, task)==True:
                    chore_to_person(chosen_person,task,day)
                    distribution_check=True #wrong position, maybe use if including sunday to set dist check
                else:
                    counter=counter-1
        
            if counter==0:
                C.Chore.open_tasks.append(task)

        
        
       
    

def distribution_of_twice():
    '''
    Task will be assigned to a random person on a random first day. 
    the first day dictates on which other days the task might be carried 
    out. This means it excludes days within 2 days of the first day. 
    This is accomplished by using match case and lists which are used 
    for the second assignment.

    '''
            

    for task in C.Chore.twice_copy:

        distribution_check=False
        counter=task.counter

        while counter!=0 and distribution_check==False:

            counter=counter-1

            week=["mon","tue", "wed", "thu", "fri", "sat", "sun"]
            shuffle(week)
            shuffle(P.Person.people)

            day=week[0]
            person=P.Person.people[0]

            match day:
                case "mon":
                    possibledays=["thu","fri"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)

                    
                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,other_day,task)
                    
                    else:

                       counter=counter-1
                    
                    

                case "tue":
                    possibledays=["fri","sat"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    elif person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True
                    
                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task, other_day)
                        distribution_check=True
                    
                    else:
                        counter=counter-1
                
                case "wed":
                    possibledays=["sat","sun"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True
                    
                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task,other_day)
                        distribution_check=True
                    
                    else:
                        counter=counter-1
                
                case "thu":    
                    possibledays=["sun","mon"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True
                    
                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task,other_day)
                        distribution_check=True
                    
                    else:
                        counter=counter-1
                
                case "fri":
                    possibledays=["mon","tue"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True

                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task,other_day)
                        distribution_check=True
                    else:
                        counter=counter-1
                
                case "sat":
                    possibledays=["tue","wed"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True

                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task,other_day)
                        distribution_check=True

                    else:
                        counter=counter-1
                
                case "sun":
                    possibledays=["wed","thu"]
                    shuffle(possibledays)
                    second_day=possibledays[0]
                    other_day=possibledays[1]

                    if person.time_for_task_check(day, task)==True:
                        chore_to_person(person,task,day)
                    
                    if person.time_for_task_check(second_day, task)==True:
                        chore_to_person(person,task,second_day)
                        distribution_check=True
                        
                    elif person.time_for_task_check(other_day, task)==True and (person.time_for_task_check(second_day, task)==True or person.time_for_task_check(day, task)==True):
                        chore_to_person(person,task,other_day)
                        distribution_check=True
                    
                   
        
        if counter ==0:
            C.Chore.open_tasks.append(task)
            
        
            


def distribution_of_once():
    '''
    Used for assignment of weekly tasks. 
    Sunday and monday are excluded to make sure the gap between task 
    appointments is big enough.
    '''

    for task in C.Chore.once_copy:

        distribution_check=False
        counter=task.counter

        while counter!=0 and distribution_check==False:
            counter=counter-1

            week_no_mon_sun=["tue", "wed", "thu", "fri", "sat"]

            shuffle(P.Person.people)
            shuffle(week_no_mon_sun)
            person=P.Person.people[0]
            day=week_no_mon_sun[0]

            if person.time_for_task_check(day, task)==True:
                chore_to_person(person,task,day)
                distribution_check=True
           

        if counter==0:
            C.Chore.open_tasks.append(task)
        