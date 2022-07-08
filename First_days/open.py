# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)
# from pathlib import Path
# p = Path('EQR.csv')
# print(p)

with open('todo.txt', 'r') as file:
    #filecontent = file.read()
    list_offile = file.readlines()
    #print(filecontent)
    print(list_offile)

with open('example.txt', 'w') as testwrite:
    testwrite.write('This is a test')
    
with open('example.txt', 'r') as check:
    print(check.read())
