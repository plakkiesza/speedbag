
import sys

class smpl():
    def __init__(self, m='0',x1='0',y1='0',z1='0\n'):
        self.msec = m
        self.x = x1
        self.y = y1
        self.z = z1
    def tofile(self):
        return (self.msec+','+self.x+','+self.y+','+self.z)
    def getmsec(self):
        return int(self.msec)
    def setmsec(self,m):
        self.msec = m
    def incmsec(self):
        self.msec=str(int(self.msec)+1)

filer = open('6-79hits.TXT', 'r')
filew = open('6-79hits.csv', 'w')

lasts = smpl()

for line in filer:
    sample = line.split(',')
    #assume its a delay will never be the first one
    if (len(sample)>2):
        #assume the first one is an int of msec
        dummy = int(sample[0])+1 # if its not an int then it should fail
        while (int(sample[0])>lasts.getmsec()):
            lasts.incmsec()
            filew.write(lasts.tofile())
            print (lasts.tofile())
        lasts.incmsec()
        msec = lasts.getmsec()
        lasts = smpl(str(msec),sample[1],sample[2],sample[3])
        filew.write(lasts.tofile())
        print(lasts.tofile())


