import os, shutil

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

# main
dir_list = get_dir()
search_and_replace()
compile_latex()
