# Title: Python-based Simple EDF Implementation
import numpy

print("EDF")
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
# The order is based on the process name.
ToBeExecuted = [0 for number in range(len(processes))]
print("Time\tProcess")
for time in range(0, lcperiod):
# When the current time mod period is zero, it means a new task is arriving.
# Thus we refresh the ToBeExecuted accordingly.
	for p in processes:
		if (time % processes.get(p)[1]) == 0:
			ToBeExecuted[processes.get(p)[2]] = processes.get(p)[0]
# This is bad, should use +inf instead.
	ToNextDeadline = [999 for number in range(len(processes))]
	isIdle = 1
	for tbexec in range(0, len(ToBeExecuted)):
# We should not idle if there are unfinished tasks.
		if ToBeExecuted[tbexec] != 0:
			ToNextDeadline[tbexec] = processes.get("P" + str(tbexec + 1))[1] - (time % processes.get("P" + str(tbexec + 1))[1])
			isIdle = 0
# No task, idle.
	if isIdle == 1:
		continue
# We should execute the process that has the nearest deadline ahead.
	whichshouldrun = ToNextDeadline.index(min(ToNextDeadline))
	print(time, end='')
	print('\t',end='')
	print("P" + str(whichshouldrun + 1))
	ToBeExecuted[whichshouldrun] = ToBeExecuted[whichshouldrun] - 1
