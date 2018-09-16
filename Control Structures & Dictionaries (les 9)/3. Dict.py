cijfers = {'student 1': '8.5', 'student 2': '9.2', 'student 3': '7.8', 'student 4': '1.3', 'student 5': '9.3', 'student 6': '10.0', 'student 7': '6.5', 'student 8': '9.6',}
for i in cijfers.items():
    if float(i[1]) >= 9:
        print(str(i[0]) + ' heeft een ' + str(i[1]) + ' gehaald.')
