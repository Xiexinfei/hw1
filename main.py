# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061223.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.

# pick out the five stations
target_data_5 = list(filter(lambda item: item['station_id'] == 'C0A880'
 or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640'
 or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260', data))

# pick out ID and WDSD
target_data = [[column['station_id'],float(column['WDSD'])]for column in target_data_5]

min_new = 0.0     # initialize the value
max_new = 0.0
max_range = 0.0
station_5 = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
m=2               # two column, one for ID, one for WDSD's max range
n=5               # five stations
out=[[0]*m]*n     # to store what to be printed out(ID and WDSD's max range)

i = 0
while i < len(target_data):                     # remove -99.000 and -999.000
   if target_data[i][1] == -99.0 or target_data[i][1] == -999.000:
      target_data.remove(target_data[i])        # remove the whole row
   else:
      i += 1

for j in range(len(station_5)):                 # loop for five station
   for i in range(len(target_data)):            # go through the whole list 
      if target_data[i][0] == station_5[j]:     # when first meet the desired station
         botton = target_data[i][1]             # initial minimum and maximum
         top = target_data[i][1]
         break

   for i in range(len(target_data)):
      if target_data[i][0] == station_5[j]:     # when find the desired station
         if target_data[i][1] < botton:         # compare WDSD value
            botton = target_data[i][1]          # if smaller, set it to be minimum
            min_new = botton
         else:
            min_new = botton                    # if not, do not change the minimum

         if target_data[i][1] > top:
            top = target_data[i][1] 
            max_new = top
         else:
            max_new = top
   max_range = max_new - min_new                # calculate the maximum for WDSD's range
   if max_range == 0: Range = 'None'
   else: Range = max_range                      # the final result of range
   out[j] = [station_5[j],Range]                # store ihe result into out array

#=======================================

# Part. 4
#=======================================
# Print result
print(out)


