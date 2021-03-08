# hw1
(1)how to setup and run the program:

download 108061223.csv
pick out the five station's information into target_data_5, 
only choose the column "station ID"(target_data[i][0]) and "WDSD"(target_data[i][1]) into target_data,
loop for every column "1" for target_data, to remove the rows whose column1(WDSD) are -99.000 or -999.000, 
loop for the specific station to find its maximum and minimum(compare number, store the bigger/smaller one to variables), 
calculate the maximum range(if there is only one or no number(removed previously because of -99.000 and -999.000) remained, then range = 0, print "None"), 
and store the maximum range into the column1 of the output array "out"(column0 is station ID), 
last, print "out" out. 

(2)result:

[['C0A880', 3.2], ['C0F9A0', 1.2999999999999998], ['C0G640', 3.6], ['C0R190', 2.6], ['C0X260', 4.7]]
