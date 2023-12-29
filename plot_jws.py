

from matplotlib import pyplot
import numpy as np
import re


def get_microprocessor_data_from(filename):
	xs = []
	ys = []
	with open(filename, 'r') as file_cores:
		lines = file_cores.readlines()
	
		matcher = re.compile("([0-9\.]+)\s+([0-9\.]+)")
		for line in lines:
		
			matches = matcher.match(line)
			if matches is not None:
				groups = matches.groups()
				xs.append(float(groups[0]))
				ys.append(float(groups[1]))
	
	return np.array(xs), np.array(ys)
		


dat_cores = get_microprocessor_data_from("50yrs/cores.dat")
dat_freq = get_microprocessor_data_from("50yrs/frequency.dat")
dat_transistors = get_microprocessor_data_from("50yrs/transistors.dat")
dat_watts = get_microprocessor_data_from("50yrs/watts.dat")


print(dat_freq)
pyplot.plot(*dat_transistors, '.')
pyplot.plot(*dat_freq, '.')
pyplot.yscale('log')
pyplot.show()

# Conclusion: Moore's law looks to be on track still, despite everything.