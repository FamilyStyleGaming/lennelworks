from my_modules.my_helper_functions import printline

my_list = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Pluto']

for index, name in enumerate(my_list,start=1):
    file_name = "%s - Our Solar System - #%s.txt" % (name,index)
    #print (file_name)
    file_path = "../my_files/"+file_name
    #print(file_path)
    with open(file_path, 'w') as rf:
        rf.write('just a temp file of the solar system:\n'+file_name)