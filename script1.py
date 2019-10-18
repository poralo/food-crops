#! /usr/bin/env python3
# -*- coding: utf-8 -*-

fd = open('FeedGrains.csv',"r")

L01 = []
L02 = []
L03 = []
L04 = []
L04 = []
L05 = []
L06 = []
L07 = []
L08 = []
L09 = []
L010 = []

for line in fd:
    data = line.split(",")
    L01.append(data[0])
    L02.append(data[1])
    L03.append(data[2])
    L04.append(data[3])
    L05.append(data[4])
    L06.append(data[5])
    L07.append(data[6])
    L08.append(data[7])
    L09.append(data[8])

print(L09)
fd.close()

