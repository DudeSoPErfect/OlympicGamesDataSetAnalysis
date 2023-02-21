# OlympicGamesDataSetAnalysis

### The essence of the program
The program analyzes the dataset of Olympic medalists from 1896 to 2016. Sorts the winners by weight, age and height. Produces analytics of male and female prize winners in each year. Conducts analytics on the most successful countries by the number of winners in each year and for all time. Conducts analytics on the age of the winners in each year. Creates the appropriate directories in the startup directory, consisting of the necessary tables and graphs.

### File Description
* **main.py ** - The main program file. 
Calls functions from other files, namely those that are responsible for the preparation, analysis, generation of tables and graphs.
* **set_options ** - Auxiliary program file.
Sets the necessary parameters for the correct operation of the pandas library.
* **sex_stat.py ** - Auxiliary program file.
Analysis of the winners of the Olympiad, depending on gender.
* **age_stat.py ** - Auxiliary program file.
Analysis of the winners of the Olympiad, depending on age.
* **sorting_data.py ** - Auxiliary program file.
Sorting of winners by weight, age and height.
* **top_countries.py ** - Auxiliary program file.
Analysis of the most successful countries by the number of winners.
* **athlete_events.rar ** - Archive with an excel spreadsheet.
Contains the table required for analysis.

### How to launch
1. Upload all project files to one directory, unpacking the archive there.
2. Install the python interpreter (recommended version 3.8 and later).
3. Install the pandas and matplotlib libraries (you can use the pip package management system by pre-installing it and writing in the console: pip install pandas and pip install matplotlib).
4. Go to the files directory
5. Run the python interpreter file main.py .
6. Enjoy generating directories with tables and graphs.
