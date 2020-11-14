
class Node:
    def __init__(self,dataval = None,):
        self.dataval = dataval
        self.nextval = None

class linkList:
    def __init__(self):
        self.headval = None

    def convert(self,inplist):
        self.headval = Node(inplist[0])
        temp = self.headval
        for item in inplist[1:len(inplist)]:
            self.newNode(item,temp)
            temp = temp.nextval

    def access(self,index):
        n = self.headval
        count = -1
        while True:
            count+=1
            if count == index:
                break
            if n.nextval is None:
                break
            n = n.nextval
        if n.nextval is None:
            return None
        return n.dataval

    def prntList(self,startNode,endNode):
        count = 0
        prntVal = self.headval
        while count<startNode:
            prntVal = prntVal.nextval
            count+=1
        while count<=endNode:
            print(prntVal.dataVal)
            if count == endNode: return
            prntVal = prntVal.nextval
            if prntVal is None: return print("Re-enter values please")
            count+=1
   
    def newNode(self,newval,jumpNode=None,newHead = False):
        newNode = Node(newval)
        if newHead:
            newNode.nextval = self.headval
            self.headval = newNode
            return newNode
        if jumpNode is None:
            print("There is no such node there")
            return newNode
        if jumpNode.nextval is None:
            jumpNode.nextval = newNode
            return newNode
        newNode.nextval = jumpNode.nextval
        jumpNode.nextval = newNode
        return newNode

    def removeNode(self,value):
        tmp = self.headval
        if tmp != None:
            if self.headval.dataval == value:
                self.headval = self.headval.nextval
                tmp = None
                return
        while tmp is not None:
            if tmp.dataval == value:
                break
            prevTmp = tmp
            tmp = tmp.nextval
        if tmp is None:
            return print("value is not in list")
        prevTmp.nextval = tmp.nextval
        tmp = None




