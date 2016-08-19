import json
from sys import argv
file = open('access.log', 'r')
NameFile = ("log_", ".json")
NumberFile = 1
LineErr = 0
file1 = open(NameFile[0]+str(NumberFile)+NameFile[1], 'w')
iterator1 = 0
log = {}
for _line in file:
    if iterator1 > 100000:
        iterator1 = 0
        NumberFile += 1
        file1 = open(NameFile[0] + str(NumberFile) + NameFile[1], 'w')
    iterator1 += 1
    _line = _line.replace(',', ' ').split(' ')
    if len(_line) >= 11:
        log['IP'] = _line[0]
        if _line[1][:4].lower() == 'www.':
            _line[1] = _line[1][4:]
        log['DomainName'] = _line[1]
        log['HTTPRequest'] = _line[5]+_line[6]+_line[7]
        log['ResponseStatus'] = _line[8]
        log['Bite'] = _line[9]
        log['Visitor'] = _line[11]
        file1.write(json.dumps(log) + '\n')
    else:
        LineErr += 1
        print("№", LineErr, " Не смог получить: ", _line, "\n Линия: ", iterator1, "\n  В файле: ",
              NameFile[0] + str(NumberFile) + NameFile[1])
file1.close()
file.close()
print("Finish")
