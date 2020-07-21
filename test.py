#####!/usr/bing/env python
#from _future_ import print_function

my_str = "adj"
print(my_str)

try:
	ip_addr = raw_input("Enter an IP address: ")
except ImportError:
	ip_addr = input("Enter aaa IP address: ")

print(ip_addr)

