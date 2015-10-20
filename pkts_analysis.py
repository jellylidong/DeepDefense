__author__ = 's3lab_ld'
import numpy as np
import pandas as pd

print "loading..."
pkts=pd.read_csv("csv/output.csv", header = None)


print "processing..."
res = open("results/attack_analysis.txt", 'w')
start_time = float(pkts.ix[0][0])
paketPerSec = []
srcList = {}
dstList = {}
count = 0
numOfPackets = 0

for i in pkts.index:
    numOfPackets = numOfPackets + 1
    arrival_time = float(pkts.ix[i][0])
    src_ip = pkts.ix[i][1]
    dst_ip = pkts.ix[i][2]

    if (arrival_time - start_time) <= 1.0:
        count = count + 1
    else:
        paketPerSec.append(count)
        count = 1
        start_time = float(pkts.ix[i][0])

    if srcList.has_key(src_ip):
        val = srcList[src_ip] + 1
        srcList[src_ip] = val
    else:
        srcList[src_ip] = 1

    if dstList.has_key(dst_ip):
        val = dstList[dst_ip] + 1
        dstList[dst_ip] = val
    else:
        dstList[dst_ip] = 1

    if numOfPackets%1000000 == 0:
        print numOfPackets, " packets processed"


import matplotlib.pyplot as plt
#import Image
plt.plot(paketPerSec)
plt.ylabel('Packets/Sec')
plt.savefig('results/attack.png')
#Image.open('attack.png').save('attack.jpg','JPEG')
#plt.show()

ip_src_only = {}
ip_dst_only = {}
ip_cmm_of_src   = {}
ip_cmm_of_dst   = {}


for key in srcList.keys():
    if not dstList.has_key(key):
        ip_src_only[key] = srcList[key]
    else:
        ip_cmm_of_src[key] = srcList[key]

for key in dstList.keys():
    if not srcList.has_key(key):
        ip_dst_only[key] = dstList[key]
    else:
        ip_cmm_of_dst[key] = dstList[key]

print "the whole pcap file contains" , len(paketPerSec) , "seconds data"
print "the whole pcap file contains" , numOfPackets , " packet"

print "number of destinations: " , len(dstList.keys())
print "destination and its times:\n", dstList.items()

print "number of sources: " , len(srcList.keys())
print "source and its times:\n", srcList.items()

print "ip_dst_only: ", ip_dst_only
print "ip_src_only: ", ip_src_only
print "ip_cmm_of_dst: ", ip_cmm_of_dst
print "ip_cmm_of_src: ", ip_cmm_of_src


res.write("the whole pcap file contains " + str(len(paketPerSec)) + " seconds data" + "\n")
res.write("the whole pcap file contains " + str(numOfPackets) + " packets" + "\n")
res.write("number of destinations: " + str(len(dstList.keys()))+ "\n")
res.write("number of sources: " + str(len(srcList.keys())) + "\n")
res.write("destination and its times:\n"+ str(dstList.items())+ "\n")
res.write("source and its times:\n"+ str(srcList.items())+ "\n")

res.write("ip_dst_only: "+ str(ip_dst_only)+ "\n")
res.write("ip_src_only: "+ str(ip_src_only) + "\n")
res.write("ip_cmm_of_dst: "+ str(ip_cmm_of_dst)+ "\n")
res.write("ip_cmm_of_src: "+ str(ip_cmm_of_src)+ "\n")

res.close()
print "done"

####Write paketPerSec ################
pps = open("results/paketPerSec.csv", "w")
for i in paketPerSec:
        pps.write(str(i) + "\n")
pps.close()

####Write unique source IP############
srcip = open("results/unqieSrcIP.csv", "w")
for key, val in srcList.iteritems():
        srcip.write(str(key)+","+str(val)+"\n")
srcip.close()

#####Write unique dest IP#############
dstip = open("results/uniqueDstIP.csv", "w")
for key, val in srcList.iteritems():
        dstip.write(str(key)+","+str(val)+"\n")
dstip.close()

######Write cmm  src IP###############
cmmsrc = open("results/cmm_src_ip.csv", "w")
for key, val in ip_cmm_of_src.iteritems():
        cmmsrc.write(str(key)+","+str(val)+"\n")
cmmsrc.close()

######Write cmm dst  IP###############
cmmdst = open("results/cmm_dst_ip.csv", "w")
for key, val in ip_cmm_of_dst.iteritems():
        cmmdst.write(str(key)+","+str(val)+"\n")
cmmdst.close()

#######Write src only IP##############
srconly = open("results/only_src_ip.csv", "w")
for key, val in ip_src_only.iteritems():
        srconly.write(str(key)+","+str(val)+"\n")
srconly.close()

#######Write src only IP##############
dstonly = open("results/only_dst_ip.csv", "w")
for key, val in ip_dst_only.iteritems():
        dstonly.write(str(key)+","+str(val)+"\n")
dstonly.close()
