#!/usr/bin/env bash
#author vcoder
#sued to extract unique paris or ones

tshark -r pcap/*.pcap -T fields -e ip.src |sort -n |uniq -c |sort -n >> csv/uniqSrcIP.csv
tshark -r pcap/*.pcap-T fields -e ip.dst |sort -n |uniq -c |sort -n >> csv/uniqDstIP.csv
tshark -r pcap/*.pcap -T fields -e ip.src -e ip.dst |sort -n |uniq -c |sort -n  >> csv/uniq_Src_Dst.csv
