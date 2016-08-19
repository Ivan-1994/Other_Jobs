import json
from sys import argv
a = 1

ListDom = []
log = []
ib = []
top5_bite = []
dictiter = 0
dicthttp = {}
list_ip = []
iter_ip = 0
while a < 2:
    file = open("log_"+str(a)+".json", 'r')
    a += 1
    for i in file:
        log = json.loads(i)
        if not log['DomainName'] in ListDom:
            ListDom.append(log['DomainName'])
        ib.append(i)
for i_dom in ListDom:
    print("\n", i_dom)
    for under_line in ib:
        under_log = json.loads(under_line)
        if under_log['DomainName'] == i_dom:
            try:
                top5_bite.append(int(under_log['Bite']))
            except ValueError:
                pass
            if not str(under_log['HTTPRequest']) in dicthttp:
                dicthttp[under_log['HTTPRequest']] = 1
            else:
                dicthttp[under_log['HTTPRequest']] += 1
            if not str(under_log['IP']) in list_ip:
                list_ip.append(under_log['IP'])
                iter_ip += 1
    print("\tТОП-5 самых популярных страниц:")
    #genexp = ((k, dicthttp[k]) for k in sorted(dicthttp, key=dicthttp.get, reverse=True))
    for key in sorted(dicthttp, key=dicthttp.get, reverse=True):
        if dictiter > 6:
            dictiter = 0
            break
        dictiter += 1
        print("\t\t",key)
    print("\tТОП-5 самых больший ответов сервера (в байтах): ")
    top5_bite = list(set(top5_bite))
    top5_bite = sorted(top5_bite, key=abs, reverse=True)
    try:
        while dictiter < 6:
            print("\t\t", top5_bite[dictiter])
            dictiter += 1
    except IndexError:
        pass
    print("\tКоличество уникальных посетителей (по IP):")
    print("\t\t", iter_ip)
    dictiter = 0
    top5_bite = []