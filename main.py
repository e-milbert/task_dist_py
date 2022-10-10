from random import shuffle
import Chore as C
import Person as P
import functions as func

Tk1=C.Chore("task1d",3,"daily")
Tk2=C.Chore("task2d",4,"daily")
Tk3=C.Chore("task3d",2,"daily")
Tk4=C.Chore("task4t",4,"twice")
Tk5=C.Chore("task5t",5,"twice")
Tk6=C.Chore("task6o",4,"once")
Tk7=C.Chore("task7o",6,"once")
Tk8=C.Chore("task8ind",4,"ind",True)
Tk9=C.Chore("task9ind",2,"once",True)

P1=P.Person("Pers1",6,4,8,3,4,7,2,Tk8,"wed")
P2=P.Person("Pers2",9,9,9,9,9,9,9,Tk9,"mon")
P3=P.Person("Pers3",9,9,9,9,9,9,9)
P4=P.Person("Pers4",4,7,6,3,2,8,7)


C.copy_frequency_lists() 

func.distribution_of_daily()

func.distribution_of_twice()

func.distribution_of_once()


func.print_week(P1)
func.print_week(P2)
func.print_week(P3)
func.print_week(P4)
