#!/usr/bin/env python3

import argparse
import sys
import os
import nmap
import time
from datetime import datetime
import jefftadashi_utils as jtu

def main(argv):

    parser = argparse.ArgumentParser()
    #parser.add_argument("-f", "--file", help="Input a file with IP's")
    parser.add_argument("-i", "--input", nargs='+', help="Input simple space-separated IP or CIDR list")
    args = parser.parse_args()

    if not os.geteuid()==0:
        print (jtu.color.red + "ERROR: Script not running as sudo/root. ICMP pings (nmap) will not work as fully intended. Exiting..." +  jtu.color.end)
        quit()

    # Global variables
    ping_ip_str = ''

    # If -i defined, build string from arg-created list of IP/CIDRS
    for i in args.input:
        ping_ip_str = ping_ip_str + " " + i

    # down-time-dict - "10.1.1.1":"timedate object"  format
    down_time_dict = {}

    while True:
        down_time_dict = run_ping(ping_ip_str, down_time_dict)
        #print (down_time_dict)
        time.sleep(8)

def run_ping(ip_string, down_time_dict):
    # input: ip_string,  and down-time-dict
    # output: list of IP's that were down previously, and timestamp?


    # Get current timestamp before scan
    now_time = datetime.now()  #really it's datetime.dateime.now if importing just datetime
    time_st = now_time.strftime('%Y-%m-%d %H:%M:%S')

    nm = nmap.PortScanner()
    nm.scan(hosts=ip_string, arguments='-n -sn -PE -T3 -v ') # hosts must be space-delimited string
    # -n to skip reverse DNS lookup
    # -sn to skip all TCP/port checks
    # -PE to invoke standard ICMP echo check
    # -T4 for timing. Set to T5 for faster, etc. T1-T5 as options.
    # -v needed for ping down

    ip_total_count = 0
    ip_up_count = 0
    ip_down_list = []

    for n_ip in nm.all_hosts():
        ip_total_count = ip_total_count + 1
        #print (nm[n_ip])
        #print (n_ip + " is " + nm[n_ip].state())
        if nm[n_ip].state() == "up":
            ip_up_count = ip_up_count + 1
            down_time_dict.pop(n_ip, None) #remove IP entry from down_ip_dict, if it was there
        else:
            ip_down_list.append(n_ip)
            if n_ip not in down_time_dict: # add initial time entry of first down, only if not existing
                down_time_dict[n_ip] = now_time

    

    print (time_st + jtu.color.green + " - Up/Total = " + str(ip_up_count) + "/" + str(ip_total_count) + jtu.color.end)
    #print (jtu.color.red + "DOWN IP's: " + jtu.color.end + str(ip_down_list))
    

    #next, iterate down_time_dict and print all differences:
        # duration = time.now - down_time_dict[ip]
        #print('.', end='') # example of no newline

    return down_time_dict

if __name__== "__main__":
    main(sys.argv[1:])
