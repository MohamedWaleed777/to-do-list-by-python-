# **To-Do List Program by Python**
 **Simple command line To-Do list program**


 ## **features** 
 - Add New Tasks
 - View The Old Tasks
 - Remove The Completed Tasks
 - Tracking Your Tasks as It Saves Your Tasks Always
***
 ### **How to Run?**
 

 1. download the files
 2. open terminal in project folder and Run it
***

 * You can also run it in vs studio code directly  

 ### **Requirments**
 * **It requires python 3.7 or above as dictionaries before that version was unordered**



 ***
 ***
 ### Challenges 
 ***
 1. The saving  and loading process after quiting the program 
 2.  the status of every task 

 #### How I Solved Them ?
 * by importing and using json library and save file using it 
 * making functions to save the file before quiting and checking if the file have tasks in the beginning 
 * by making the status appear in the view function or remove function to know which tasks done 
 
 as here in main file 
 ``` python
 if tasks[i]["status"]:
                                status ="   Done"
            else:
                                status="   Pending"
            print (f"{i+1} - {tasks[i]['name'] } {status}")#as i =0 to print correct number of tasks as list satrts from 0 
```

### Resources
[W3 Schools](https://www.w3schools.com/python/default.asp)    

[Bro code youtube video](https://youtu.be/ix9cRaBkVe0?si=-111wXAjfiCWIzgQ)


[free code camp git & github course](https://youtu.be/mAFoROnOfHs?si=PhNekLneQRHEvMQK)
