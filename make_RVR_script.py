from avg_colors import get_vals

colors = [r"\Red", r"\Green", r"\Blue", r"\Yellow"]


def make_color(color):
    values = averages[color][0]
    ans = "{r:"
    ans += str(values[0])
    ans += ",g:"
    ans += str(values[1])
    ans += ",b:"
    ans += str(values[2])
    ans += "}"
    return ans


while True:
    try:
        day = [input("Date: ")]
        averages = {}
        for color in colors:
            ignored, averages[color] = get_vals(color, day)
        break
    except FileNotFoundError:
        print("There was a file not found error")
        continue

safety = False
if input("Safe mode? ").lower() == "yes":
    safety = True

RVRCode = ""
if not safety:
    with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\RVRCodeForPython.lab", 'r') as file:
        RVRCode = file.readline()
else:
    with open(r"C:\Users\jacob\Documents\RVR Color Data\Informational Files\SafeRVRCodeForPython.lab", 'r') as file:
        RVRCode = file.readline()

RVRCode = RVRCode[RVRCode.find("// Code here") + 12 : RVRCode.find("// Code end here")]


with open("RVRScriptFromPython.lab", 'w') as file:
    # Header
    file.write('{"identifier":"3cbc8719-b072-4f4f-84c4-3b4aa38d4b9a","name":"AVR Python Test","summary":"","data":"14;')
    
    # Colors
    file.write(f'const RED = {make_color(colors[0])};const GREEN = {make_color(colors[1])};const BLUE = {make_color(colors[2])};const YELLOW = {make_color(colors[3])};const TOLERANCE = 30;')
    
    # Main code
    file.write(RVRCode)
    
    # Footer
    file.write('","modified_on":"2024-09-21T12:36:10.4375000-05:00","program_type":"text","robots":[{"id":18}]}')