# Creating Python programs in Codio

### Make a new file
Use **File > New File...** or right-click in the file tree to create a new file. You can right-click in the file tree to rename or delete files.

As Codio detects which file is in focus, simply put your cursor into whichever code editor you want to run.

### Run your code
Use the Run button (that looks like a Rocketship) to Run the file your cursor is in.

### Debug your code
Use the "Debug Current File" on the far right of the top menu bar to launch the debugger targeting the file your cursor is in.

### Reconfigure your Panels for easier development
Use the **View > Panels** menu on the top tool bar to segment your screen.

Simply drag the tab of the file or terminal (the part with the name) you want to move into the new panel.

###########################################################################################
Titanic

Overview
In this exercise you will explore the data from MarineTraffic, you can find it in this link.
The data from the website was magically exported to a JSON file, a convenient format for object serialization: serialization is basically converting objects to a format, like a text file (or JSON in our example), so you can save it to disk / send it in email / whatever you want, and then convert it again to objects in your Python program, for example.

In the exercise, you’ll build a command line interface for analyzing the data of the ships.
Data Description
You can find the data inside the file ships_data.json, which is opened for you. As you can probably see, the data in the file is stored in a nested structure.

###########################################################################################

Building Command Line Interface
A command line interface (CLI) is a fancy word for a program that interacts with the user via the command line, just like all the programs that you did until now.
This is as opposed to a program that interacts with the user via Graphical User Interface (GUI), similarly to most Desktop application, or through a web interface.

Assignment Description
Create a command line that have the following commands:
###Command: help
Prints a list of the available commands.
###Command: show_countries
Prints a list of all the countries of the ships, without duplicates.
The countries should be ordered alphabetically.
###Command: top_countries <num_countries>
Prints a list of top countries with the most ships. For example, top_countries 5, prints a list of the 5 countries which have the most ships, along with the number of ships.

##########################################################################################
Dispather
Implement the command dispatcher according to the dispatcher pattern that you saw in the lesson.
You should use a dictionary of function pointers, and all of your if conditions (related to dispatching) should be eliminated.

Ship Type
Some ships are Passenger ships, some are Cargo ships, and who knows? There may be more types.
Add a new command ships_by_types that displays how many ships there are from each type.

Search Ship By names
Add a new command search_ship for searching a ship by name. The search should be case insensitive and find by partial name.
For example, if I searched "disney", I should find the ship "DISNEY DREAM".

Speed Histogram
Add a new command speed_histogram that creates an histogram of the speed of the ships, and save it to a file.
