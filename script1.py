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
L10 = []
L11 = []
L12 = []
L13 = []
L14 = []
L15 = []
L16 = []
L17 = []
L18 = []
L19 = []

def open():
    for line in fd:
        data = line.split(",")
        L01.append(data[0])
        L02.append(data[1])
        L03.append(data[2])
        L04.append(data[3])
        L05.append(data[4])
        L06.append(data[5])
        L07.append(data[6])
        L09.append(data[8])
        L10.append(data[9])
        L11.append(data[10])
        L12.append(data[11])
        L13.append(data[12])
        L14.append(data[13])
        L15.append(data[14])
        L16.append(data[15])
        L17.append(data[16])
        L18.append(data[17])
        L19.append(data[18])
    return L01
    return L02

print(open())

fd.close()
