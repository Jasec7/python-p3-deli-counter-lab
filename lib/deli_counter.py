katz_deli = []

def line(line):
    
    if line == []:
        print('The line is currently empty.')

    else:
        numbered_names = [f"{index}. {name}" for index, name in enumerate(line, start=1)]
        line_string = " ".join(numbered_names)
        print(f"The line is currently: {line_string}")
        



def take_a_number(line, name):

    line.append(name)
    position= len(line)
    print(f'Welcome, {name}. You are number {position} in line.')

    

    
def now_serving(line):
    if line == []:
        print("There is nobody waiting to be served!")

    else:
        called_person = line.pop(0)
        print(f'Currently serving {called_person}.')    