import shutil
import os


path = r"C:\Users\jacob\Documents\RVR Color Data"
color_list = ["red", "green", "blue", "yellow"]


date = ""
while True:
    date = input("Date: ")
    confirm = input(f"You entered '{date}'. Are you sure? (y/n) ").lower()
    if confirm != "y":
        continue
    break


used_colors = []
number_of_colors_used = 0
while number_of_colors_used < 4:
    code = input("Ready for next file to be grabbed? ").lower().strip()

    if code == "code green":
        used_colors.append("green")
        number_of_colors_used += 1
        print("Totally got green color ")
        continue

    try:
        file = [file for file in os.listdir(path + r"\Sphero Files")][0]
    except:
        print("Error grabbing Sphero file ")
        continue

    color = input("Color: ").lower()
    if color not in color_list:
        print("Invalid input\nMust enter 'red', 'green', 'blue', or 'yellow' ")
        continue
    if color in used_colors:
        print("That color has already been assigned ")
        continue
    
    used_colors.append(color)
    number_of_colors_used += 1
    color = color.capitalize()
    
    shutil.move(os.path.join(path + r"\Sphero Files", file), os.path.join(path + r"\Raw Data Files", color + " - " + date + ".csv"))

        

    
