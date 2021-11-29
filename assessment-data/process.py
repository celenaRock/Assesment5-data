log_file = open("um-server-01.txt") #This command will open the file um-server-01.txt, it will loop through the file depending on the commands we use next.


def sales_reports(log_file): #this line sets up a function to print text from the file.
    for line in log_file:    #setting up a loop to read a line in the terminal.
        line = line.rstrip() #this line removes white space in the beginning and end of a string.
        day = line[0:3]      #printing this row at this index of data
        if day == "Mon":     #setting up the parameter value
            print(line)      #ensures the data for var 'line' will print in the terminal


sales_reports(log_file)      #calls out the function to be run, prints in terminal
