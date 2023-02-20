#!/usr/bin/python3
"""Import Libraries """


import requests
import sys

""" Import libraries """

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_data = requests.get(todos_url).json()

    employee_name = requests.get(users_url).json()["name"]

    total_user_todos = 0
    completed_todos = 0
    titles = []
    for todo in todo_data:
        #Checks if the user_id is the same input as parameter
        if user_id == todo["userId"]:
            #get the total number of todos
            totoal_user_todos += 1
            #Get the total number of completed tasks
            if todo["completed"]:
                completed_todos += 1
                #Get the titles of the completed tasks
                titles.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_todos, total_user_todos))

    for title in titles:
        print("\t {}".format(title))
