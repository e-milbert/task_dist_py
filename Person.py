import Chore

#Person is the class to whose instances chores will be distributed to.


class Person:
    '''
    Class used to represent a person to whom a task or chore may be distributed.
    Must be called only after class Chores is finished. 
    If person has any individual tasks, those will be added to the specified days 
    and the needed time will be subtracted automatically.

    Attributes
    ----------
    people : list
        list to which each new instance of Person will be appended, used later in distribution
    name : str
        name of the person
    individual_task : object
        Instance of class Chore, personal chore like "clean bedroom"
    time_points_mon : int
        short:tp; time the person has to do chores each day. 10 min = 1, 60 min = 6
    days_time_points : dict
        automatically initialiesed dictionary with day:tp pairs
    monday_chores : list
        lists of each week day for each instance to append tasks for the day

    Methods
    -------
    '''
    
    people=[] 

    def __init__(self, name=str, time_points_mon=int, time_points_tue=int, time_points_wed=int, time_points_thu=int, time_points_fri=int, time_points_sat=int, time_points_sun=int, individual_task=None, individual_task_day=None):
        '''
        Parameters
        ----------
        name : str
            name of the person
        time_points_mon : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_tue : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_wed : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_thu : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_fri : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_sat : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6
        time_points_sun : int
            time the person has to do chores each day. 10 min = 1, 60 min = 6     
        individual_task : optional, default None
            Instance of class Chore, personal chore like "clean bedroom"
        individual_task_day : optional, default None
            str, day on which task will be sheduled   
        
        '''
        
        self.name = name
        
        self.tp_mon = time_points_mon
        self.tp_tue = time_points_tue
        self.tp_wed = time_points_wed
        self.tp_thu = time_points_thu
        self.tp_fri = time_points_fri
        self.tp_sat = time_points_sat
        self.tp_sun = time_points_sun

        self.individual_task = individual_task
        self.individual_task_day=individual_task_day

        self.days_time_points={                 #used for subtracting needed time to fullfil a task. values will change
            "mon":self.tp_mon,
            "tue":self.tp_tue,
            "wed":self.tp_wed,
            "thu":self.tp_thu,
            "fri":self.tp_fri,
            "sat":self.tp_sat,
            "sun":self.tp_sun
        }

        self.monday_chores=[]
        self.tuesday_chores=[]
        self.wednesday_chores=[]
        self.thursday_chores=[]
        self.friday_chores=[]
        self.saturday_chores=[]
        self.sunday_chores=[]

        Person.people.append(self) #instance appended to list of people

        if type(individual_task)!=None and type(individual_task_day)==str:
            self.add_task_to_day_list(individual_task_day,individual_task)
            self.subtract_task_tp_from_persons_day(individual_task_day,individual_task)

        
    

    #should be in utility??
    def subtract_task_tp_from_persons_day(self, day=str, task_name=object):
        '''
        Time needed to perform certain task are subtracted from persons available time point of the given day.

        Person's available time points are taken from the individual dictionary days_time_points. 

        Parameters
        ----------
        day = str
            one of the following: mon, tue, wed, thu, fri, sat, sun; keys used in days_time_points
        task_name = object
            chore/task instance
        
        Variables
        ---------


        '''

        available_tp_day=int
        task_tp=int
        new_available_tp_day=int

        available_tp_day=self.days_time_points[day]
        task_tp=task_name.tp

        if available_tp_day >= task_tp:
            new_available_tp_day=available_tp_day-task_tp
            self.days_time_points[day]=new_available_tp_day         #value in dictionary of self updated


    def time_for_task_check(self, day=str, task_name=object):
        '''
        Function checks if person has enough time points left on a certain day to do a task.

        Parameters
        ----------
        day: str
            one of the following: mon, tue, wed, thu, fri, sat, sun; keys used in days_time_points
        task_name = object
            name of chore/task instance
        
        Returns
        ------
        bool
            returns True if person has enough time, else False will be returned 
        '''
        
        available_tp_day=int
        task_tp=int

        available_tp_day=self.days_time_points[day]
        task_tp=task_name.tp

        if available_tp_day >=task_tp:
            return True
        else:
            return False


    def add_task_to_day_list(self, day=str, task_name=object):
        '''
        Adds task to persons to-Do list.

        Parameters
        ----------
        day: str
            one of the following: mon, tue, wed, thu, fri, sat, sun; keys used in days_time_points
        task_name = object
            name of chore/task instance

        '''
        
        match day:
            case "mon" :
                self.monday_chores.append(task_name)
                
            case "tue" :
                self.tuesday_chores.append(task_name)
                
            case "wed" :
                self.wednesday_chores.append(task_name)
                
            case "thu" :
                self.thursday_chores.append(task_name)
                
            case "fri" :
                self.friday_chores.append(task_name)
                
            case "sat" :
                self.saturday_chores.append(task_name)
                
            case "sun" :
                self.sunday_chores.append(task_name)
                

    def sorted_days(self): #called in func.dist_of_twice 
        '''
        Function gets list out of week_tp_dict with days(keys) sorted by value(descending).
        :param self: Person instance
        :return: list with sorted weekdays by available time points
        '''
        dic_days=self.week_tp_dict
        days_desc_tp=[]
        days_by_tp=[]

        for key_day in dic_days:
            tup=(key_day, dic_days[key_day])
            days_desc_tp.append(tup)

        days_desc_tp.sort(key=lambda y:y[1],reverse=True)

        for tup in days_desc_tp:
            day=tup[0]
            days_by_tp.append(day)

        return days_by_tp