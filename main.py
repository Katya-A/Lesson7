import os
path = r'C:\Users\Alex\PycharmProjects\Lesson7\lesson'
projectname = 'my_project'
folders = \
    ['settings',
     'mainapp',
     'adminapp',
     'authapp']
fullPath = os.path.join(path, projectname)
if not os.path.exists(fullPath):
    os.mkdir(fullPath)
for f in folders:
    folders = os.path.join(fullPath, f)
    if not os.path.exists(folders):
        os.mkdir(folders)

