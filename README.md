## Individual Project: Python Todo List CLI
### Requirements
- [ ] The user can run your program from the command line.
- [ ] If the user does not supply the correct arguments, or supplies a --help flag, the user sees a "usage" message. 
- [ ] The user can add a todo from the command line, by calling add_todo. The fields specified should be text, due_date, and project_id. The fields due_date and project_id are optional. Text is required.
- [ ] Todos added, by default should be marked as incomplete.
- [ ] The user should see a message giving information about the todo that was added.
- [ ] The user can call a function called mark_complete and pass the id of the todo to mark complete. 
- [ ] The user can see all todos from the command line by passing a list command, sorted with the ones due first. 
- [ ] The user can supply arguments to the list command to only see todos that are complete. 
- [ ] The user can supply arguments to the list command to only see todos of a particular project_id. 
- [ ] The user can supply arguments to the list command to reverse the default sort, to now see the todos by due_date descending.
- [ ] The user can supply arguments to the list command to combine the above options.

### Optional Requirements
- [ ] The user can add a project by calling add_project. Each project must have a name. 
- [ ] The user can see all projects from the command line.

### Bonus Requirements
- [ ] The user can add a user_id to each todo. 
- [ ] The user can add a user to the system by passing add_user. Each user should have a name, email_address, and id. 
- [ ] The user can call a list_users command that shows all the users in the system.
- [ ] The user can call a staff command that shows each project, combined with each of the users working on that project.
- [ ] The user can call a who_to_fire command that lists all users who are not currently assigned a todo.

Additional Screenshots
Reference Reading and Tools
Google Python Fire
A really useful utility that will make our program accessible from the command line. 
https://github.com/google/python-fire. To install, go to your directory and type pip3 install fire.

The documentation is good, but we'll be using it in a quite simple way.

VS Code SQLite Extension
Looking at the state of your SQLite database is super useful. Check out the SQLite Extension for VSCode:

Image

Now you'll get an interface to query and inspect your database.

Image

### Tutorials
* https://stackabuse.com/a-sqlite-tutorial-with-python/
* https://www.pythoncentral.io/introduction-to-sqlite-in-python/

### Official Documentation
* https://docs.python.org/2/library/sqlite3.html