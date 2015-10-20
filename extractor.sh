#!/usr/bin/env bash
#author vcoder
#used to extrat the listed features and run pkt_anlysis.py

tshark -T fields -n -r  pcap/*.pcap -T fields -e frame.time_relative -e ip.src -e ip.dst -e ip.proto -E separator=, >> csv/output.csv

python pkts_analysis.py
