import csv
import statistics
import json

days = [r"9.17.2024", r"9.19.2024", r"9.21.2024"]
colors = {"red" : r"\Red", "green" : r"\Green", "blue" : r"\Blue", "yellow" : r"\Yellow"}


# @param - color in format ["/Red, /Blue, /Green"]
# @param - date in format month.day.year
def get_vals(color, dates):
    time, counter_total = 0, 0
    vals = [0 for i in range(3)]
    averages = []
    # print(r"C:\Users\jacob\Documents\RVR Color Data\Red - 9.14.2024.csv")
    for date in dates:
        with open(r"C:\Users\jacob\Documents\RVR Color Data\Raw Data Files" + color + r" - " + date + r".csv", newline="") as file:
            reader = csv.reader(file, delimiter=",", quotechar="|")
            reader.__next__()
            counter = 0
            temp = [0 for i in range(3)]
            for line in reader:
                time += float(line[0]) 
                for i in range(3):
                    temp[i] += int(line[i + 1])
                    vals[i] += int(line[i + 1])

                '''
                red_val += int(line[1])
                green_val += int(line[2])
                blue_val += int(line[3])
                '''
                counter += 1
                counter_total += 1
            
            averages.append([temp_value / counter for temp_value in temp])
            
    
    for i in range(len(vals)):
        vals[i] /= counter_total
    
    '''
    red_val /= counter
    green_val /= counter
    blue_val /= counter
    '''
    
    # print("Red Average: ", red_val)
    # print("Green Average: ", green_val)
    # print("Blue Average: ", blue_val)
    
    return vals, averages

values = []
all_averages = {}
with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\Averages.csv", 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for color in colors:
        vals, averages = get_vals(colors[color], days)
        all_averages[color] = averages
        values.extend(vals)
        # print(averages)
    
    # print(values)
    # print(all_averages)
    writer.writerow(values)

differences = {}
for color in colors:
    differences[color] = [[0 for i in range(3)] for i in range(int(0.5 * len(all_averages[color]) * (len(all_averages[color]) - 1)))]
    counter = 0
    for i in range(len(all_averages[color])):
        for j in range(i + 1, len(all_averages[color])):
            for k in range(3):
                differences[color][counter][k] = all_averages[color][i][k] - all_averages[color][j][k]
            counter += 1


# print(differences)
with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\AveragesPerDay.json", 'w') as file:
    json.dump(all_averages, file)

with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\DifferencesPerDay.json", 'w') as file:
    json.dump(differences, file)

stat_differences = differences.copy()
# print(f"Stat-differences: {stat_differences.values()}")
for days in stat_differences.values():
    # print(f"days: {days} days[i]: {days[0]}")
    for i in range(len(days)):
        days[i] = [j for j in days[i] if j != 0.0]
        # print(days[i])
        days[i] = { 'mean' : statistics.fmean(days[i]), 'standard_deviation' : statistics.stdev(days[i]) }

with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\Statistics.json", 'w') as file:
    json.dump(stat_differences, file)
