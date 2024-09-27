import os
import shutil

# os.listdir('.')

name_os = os.name
print('------------------------------------------------------------------------------')
print(f'Welcome to {name_os} || Information routes and modified directorys and files')
print('------------------------------------------------------------------------------')

print('Information your system: ')

shell = os.environ['SHELL']
name_user = os.environ['USER']
system_os =os.environ['XDG_SESSION_DESKTOP']
shell_execution = os.environ['TERMINAL_EMULATOR']

print(f"""
Terminal : {shell[5:]}
User : {name_user}
System operative : {system_os}
Terminal execution : {shell_execution}
""")

print('------------------------------------------------------------------------------')

# print("""
# Options:
#
# 1 = Renombrar archivos masivamente  = (pasar nombre de carpeta que contiene los archivos)
# 2 = Mover archivos masivamente = (pasar nombre de directorio de origen y el de cambio)
# 3 = ELiminar archivos masivamente = (pasar nombre de directorio)
#
# """)

action = int(input())


if action==1:
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


# print(path)
for file in os.listdir(path):
    print(file)

# fd = "GFG.txt"
# file = open(fd, 'r')
# text = file.read()
# print(text)
# # os.close(file)

# fd = "GFG.txt"
# os.rename(fd,'New.txt')

