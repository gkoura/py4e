#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below

handle = open("mbox-short.txt.txt") #open file

counts=dict()

for line in handle:
    if line.startswith ("From"):
        if line.startswith ("From:"):
            continue
        emails=line.split()
        #print (emails)
        time = emails [5]
        #print (time)
        hour =time [0:2]
        #print (hour)
        counts [hour]=counts.get(hour,0)+1
        
print (counts)

for (k,v) in sorted(counts.items()):
    print (k,v)


