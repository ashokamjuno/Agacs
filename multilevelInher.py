# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
D:\WinPython\settings\.spyder2\.temp.py
"""
class person:
    def __init__(self,sname,rno,subject):
        self.stname=sname
        self.rollno=rno
        self.subj=subject
    def printData(self):
        print "Student Name: ",self.stname
        print "Roll Number: ", self.rollno
        print "Subject : ", self.subj
class mark(person):
    def __init__(self,sname, rno, subject, mark1,mark2,mark3):
        person.__init__(self,sname, rno, subject)
        self.m1=mark1
        self.m2=mark2
        self.m3=mark3
    def printMark(self):
        self.printData()
        print "C Programming : ",self.m1
        print "Computer Fundamentals : ", self.m2
        print "C Programming Lab : ", self.m3
class mSheet(mark):
    def __init__(self, sname, rno, subject, mark1, mark2, mark3):
        mark.__init__(self, sname, rno, subject, mark1, mark2, mark3)
    def printResult(self):
        self.printMark()
        print "Total : ",self.m1+self.m2+self.m3
        print "Average : ", (self.m1+self.m2+self.m3)/3, "%"
        if (self.m1>=35 and self.m2>=35 and self.m3>=35):
            print "Reslut : Pass"
        else:
            print "Result : Fail"
ms=mSheet('john', 156, 'CS',56, 45, 35)
ms.printResult()



        
