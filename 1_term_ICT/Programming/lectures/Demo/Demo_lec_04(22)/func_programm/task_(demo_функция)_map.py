# -*- coding: utf-8 -*-
"""
Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX Однако, в оборудовании Cisco
MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
список result.
"""

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

print("Исходный:\n", mac)

def fun_format3(macitem, ch = '.'):
    return macitem.replace(":", ch)


mlist = list(map(fun_format3, mac, '_.;:' ))
print("Преобразованный:\n", mlist)


mlist = list(map(lambda m : m.replace(":", '.'), mac))
print("Преобразованный:\n", mlist)
             
