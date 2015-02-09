def MAC_List_Create(str,MAC_list):
    if str in MAC_list:
        return
    MAC_list.append(str)
    
def Write_MAC_To_File(MAC_list):
    FileHandle = open("SortedMAC",'wb')
    for item in MAC_list:
        print>>FileHandle,item
    FileHandle.close()
    return
    


infile = open("first.log","r")
outfile = open("newfile.txt","wb")

while 1:
     data = infile.readline()
     if len(data) == 0:
             break
     outfile.write(data[41:81])
     

infile.close()
outfile.close()

outfile = open("newfile.txt","r")
a = outfile.read()
length =len(a)

size = 40
i = 0
frequency = 0
unique_mac = 0
MAC_list = []
while (size<length):
    frequency = 0
    j=0
    k=40
#    print a[i:size]
    while (j<length):   
#        print "2nd loop"+a[j:k]
        if a[i:size] == a[j:k]:
            frequency+=1

        if frequency == 4:
            MAC_List_Create(a[i:size],MAC_list)
#            print MAC_list

            break
        j=k
        k=j+40
    
    i=size
    size=i+40
Write_MAC_To_File(MAC_list)
length = len(MAC_list)
print "No of unique MAC Address is %d, check the file SortedMAC for the list of devices."%length
