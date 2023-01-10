import os
import shutil
import os.path

# get nst files in current directory
def get_dir():
    list = []
    dir_list = os.listdir('./styles')
    for elem in dir_list:
        if '.bst' in elem:
            list.append(os.path.splitext(elem)[0])
    return list

# open dummy files and replace with styles
def search_and_replace(): 
    create_files()
    for counter in range(len(dir_list)):
        with open('test' + format(counter) + '.tex', 'r+') as file:
            datafile = file.read()
            datafile = datafile.replace('???' , dir_list[counter])
        with open('test' + format(counter) + '.tex', 'w+') as file:
            file.write(datafile)

# create copies of dummy file
def create_files():
    for i in range(len(dir_list)):
        shutil.copy('test.tex', 'test' + format(i) + '.tex')

# compile LaTeX
def compile_latex():
    for i in range(len(dir_list)):
        os.system("lualatex test"+format(i)+".tex")
        os.system("bibtex test"+format(i)+".aux")
        os.system("lualatex test"+format(i)+".tex")

# check if output file exists
#def file_exists():
#    for i in range(len(dir_list)):
#        file_exists = os.path.exists('test'+format(i)+'.pdf')
#        if not(file_exists):
###            raise Exception('Output file could not be found!')

# check if error in blg-file
def search_error():
    for i in range(len(dir_list)):
        with open('test' + format(i) +'.blg','r') as text_file:
            line_counter = 0
            lines = text_file.readlines()
            for line in lines:
                line_counter += 1
                if line.lower().__contains__('error') or line.lower().__contains__('illegal style-file'):
                    os.system('cat test' + format(i) + '.blg')
                    raise Exception('Error found! See test' + format(i) + '.blg on line ' + format(line_counter) + ' for more information!')
    print('No Error was found while compiling \nSuccessfully created ' + format(len(dir_list)) + ' .tex files!')

                    
# main
dir_list = get_dir()
search_and_replace()
compile_latex()
search_error()
# file_exists()
