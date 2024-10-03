import os
import shutil
import random

# 1. Modification of the directories

name_os = os.name
print('------------------------------------------------------------------------------')
print(f'Welcome to {name_os} || Information routes and modified directorys ')
print('------------------------------------------------------------------------------')

print('Information your system: ')

print(os.environ)
shell = os.environ['SHELL']
name_user = os.environ['USER']
system_os =os.environ['XDG_SESSION_DESKTOP']

print(f"""
Terminal : {shell[5:]}
User : {name_user}
System operative : {system_os}
""")

print('------------------------------------------------------------------------------')

print("""
Options:

1 = Renombrar directorios masivamente  = (pasar nombre de carpeta que contiene los archivos)
2 = Mover directorios masivamente = (pasar nombre de directorio de origen y el de cambio)
3 = ELiminar directorios masivamente = (pasar nombre de directorio)

""")

action = int(input())


if action == 1:
    pass
    print('------------------------------------------------------------------------------')
    print("""
        Options:

        1 --> Documents
        2 --> Downloads
        3 --> Desktop
        4 --> Music
        5 --> Pictures
        6 --> videos

    """)


options = int(input())
path = '/home/devsouls'
match options:
    case 1:
        directory = 'Documents'
        path = os.path.join(path,directory)
    case 2:
        directory = 'Downloads'
        path =os.path.join(path, directory)
    case 3:
        directory = 'Desktop'
        path =os.path.join(path, directory)
    case 4:
        directory = 'Music'
        path = os.path.join(path, directory)
    case 5:
        directory = 'Pictures'
        path = os.path.join(path, directory)
    case 6:
        directory = 'Videos'
        path = os.path.join(path, directory)
    case _:
        print('Invalid option')


os.system('clear') # clear all in linux

for file in os.listdir(path):
    if os.path.isdir(file):
        fd=file
        num = random.randint(1,10000)
        os.rename(file, file+num)
        print(file)





# 2. Modification of filesystem
