import math

#routine to test a set of data returns number of punches in dataset
def testdata(mydata,cnt,meen):
    #init some values for the test
    lastz = 0 # last z value to just use the difference
    zbuf = [] # init the buffer to calc the average(low pass filter)
    punches = 0 # we start with no punches
    t = 0 # used to work out time between punches

    for fline in mydata:
        # iterate over all the data
        zbuf.append(int(fline)-lastz) # add the difference between data points to buffer to work out the average
        lastz = int(fline)  # get the new last line
        if len(zbuf)>meen:  # get rid of the first data point for the average
            zbuf.pop(0)
        temp = int(10*sum(zbuf)/len(zbuf)) # work out the average
        t +=1
        if ((temp > cnt) & (t>len(zbuf))):  # check if we are above the thrsh hold and make sure we have a delay between punches.
            t = 0 
            punches+=1
#    return punches   
    return punches/2-1  # seems to get the best results
#    return punches/2   # use this for divide by 2 punches

# just test the mystery sets
def testmystery(cnt,meen):
    filetor = open('MysteryDataSet-1.TXT','r')
    listofdata = []
    for fline in filetor:
        #itterate over the file
        tmp = fline.split(',')
        if len(tmp)>3:# only add if its not a problem, ignore problems
            # next line is just for z, one after that is total vector
            listofdata.append(tmp[3])
            #listofdata.append(math.sqrt(int(tmp[1])*int(tmp[1])+int(tmp[2])*int(tmp[2])+int(tmp[3])*int(tmp[3])))
    print testdata(listofdata,cnt,meen) # print answer
    # next section is the same as above for next file
    filetor = open('MysteryDataSet-2.TXT','r')
    listofdata = []
    for fline in filetor:
        tmp = fline.split(',')
        if len(tmp)>2:
            listofdata.append(tmp[3])
            #listofdata.append(math.sqrt(int(tmp[1])*int(tmp[1])+int(tmp[2])*int(tmp[2])+int(tmp[3])*int(tmp[3])))
    print testdata(listofdata,cnt,meen)

# load files to test against
filestoread = ['3-77hits.TXT','4-81hits.TXT','5-93hits.TXT','6-79hits.TXT']
whatwewant = [77,81,93,79]

#Create list of possibilities
ij = [] 
closedta = [] # this is the list of values close ish

# make a list of all possible values
for j in range(50,100):  #100:300
    for i in range(10,20): #0:20
        ij.append((i,j))    

# check all files, starting with the first one check all possiblilities
# Only use values that worked with first files with next ones to make checking faster
for f in range(4):
    # load the file
    filetor = open(filestoread[f],'r')
    listofdata = []
    # stick it in the list for checking
    for fline in filetor:
        tmp = fline.split(',')
        if len(tmp)>2:
            listofdata.append(tmp[3])
            #listofdata.append(math.sqrt(int(tmp[1])*int(tmp[1])+int(tmp[2])*int(tmp[2])+int(tmp[3])*int(tmp[3])))

    tempij = [] #temp ij for new list
    for dtaij in ij: #iterate over possibilities
        ans = testdata(listofdata,dtaij[0],dtaij[1]) # test the current values
        print (whatwewant[f],ans,dtaij) # print to see how far we are
        if abs(whatwewant[f]-ans)<3: # if our number of punches is close to the one we want put the values in the new list
            tempij.append(dtaij)
            closedta.append((f,whatwewant[f],dtaij[0],dtaij[1],ans)) # make a list of ones close enough
    ij = tempij #new list gets from old so that next file has less options
    print len(ij)

# check between options we have for the best ones
lowestval = 100 # set a bad goal
for dtaij in ij: 
    # iterate over options
    tot = 0 # start with no total of difference between wanted and actual
    vals = [] # get a blank list to put our answers in
    for dta in closedta:
        # go through the list and add up the ones with the same values to see how close we got for all files combined
        if (dta[2],dta[3]) == (dtaij[0],dtaij[1]):
            tot += abs(dta[1]-dta[4])
            vals.append((dta[1],dta[4]))
    if tot<=lowestval:
        # if we have a better solution to before we print the values
        lowestval = tot
        print (tot)
        print dtaij
        print vals
        testmystery(dtaij[0],dtaij[1])
# /2 and -1
#1
#(16, 76)
#[(77, 77), (81, 81), (93, 93), (79, 78)]
#153
#153

# if its not /2
#3
#(13, 156)
#[(77, 77), (81, 81), (93, 91), (79, 78)]
#151
#154

# /2
#2
#(17, 76)
#[(77, 78), (81, 82), (93, 93), (79, 79)]
#154
#153
#2
#(13, 79)
#[(77, 77), (81, 81), (93, 93), (79, 77)]
#149
#150


