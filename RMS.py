# Title: Python-based Simple RMS Implementation
# For the Homework 7 of course ECE8448
# Author: Dongning Ma

import numpy

print("RMS")
# Store the information of processes into a dictionary:
# "Process Name":[Execution Time, Period (Deadline), Priority]
processes = {
	"P1":[1, 5, 0],
	"P2":[1, 10, 1],
	"P3":[2, 20, 2],
	"P4":[10, 50, 3],
	"P5":[7, 100, 4]
	}

#processes_eg2 = {
#	"P1":[1, 3, 0],
#	"P2":[1, 4, 1],
#	"P3":[2, 5, 2],
#	}

#processes_eg1 = {
#	"P1":[1, 4, 0],
#	"P2":[2, 6, 1],
#	"P3":[3, 12, 2],
#	}
	
# Compute the least common multiple of periods.
lcperiod = 1
for period in processes.values():
	lcperiod = numpy.lcm(lcperiod, period[1])

# A integer list to record how many time of each process is still needed for
# finish executing it in this period.
# The order is based on the priority of the processes.
ToBeExecuted = [0 for number in range(len(processes))]

print("Time\tProcess")
for time in range(0, lcperiod):
# When the current time mod period is zero, it means a new task is arriving.
# Thus we refresh the ToBeExecuted accordingly.
	for p in processes:
		if (time % processes.get(p)[1]) == 0:
			ToBeExecuted[processes.get(p)[2]] = processes.get(p)[0]
# We always execute the process with highest priority and then lower ones.
# Once executed for a timer period (1 unit), the corresponding ToBeExecuted
# should self decrement by 1.
	for tbexec in range(0, len(ToBeExecuted)):
		if ToBeExecuted[tbexec] != 0:
			print(time, end="")
			print('\t', end="")
			print("P%d" % (tbexec + 1))
			ToBeExecuted[tbexec] = ToBeExecuted[tbexec] - 1
			break
