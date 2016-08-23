#
# Radix Sort
# author: Valentin Lehuger
#
# Complexity:
#       average: O(nk)
#       best: O(nk)
#       worst: O(nk)
#
#       space: O(n + k)


def max_digit_number(l):
	max_ = max(map(abs, l))
	count = 0
	while max_ != 0:
		max_ /= 10
		count += 1
	return count

def fill_radius(l, base_idx):
	radius = [0] * 9
	for j in range(len(l)):
		radius[l[j] / 10**(base_idx - 1) % 10] += 1
	return radius

def cumulative_sum(ar):
	for idx in range(1, len(ar)):
		ar[idx] += ar[idx - 1]
	return ar

def fill_result_array(ar1, radius, ar2, base_idx):
	for j in range(len(ar1) - 1, -1, -1):
		ar2[radius[ar1[j] / 10**(base_idx-1) % 10] - 1] = ar1[j]
		radius[ar1[j] / 10**(base_idx-1) % 10] -= 1
	return ar2

def radixSort(l):
	l2 = [0] * len(l)
	count = max_digit_number(l)
	for i in range(1, count + 1):
		radius = fill_radius(l, i)
		radius = cumulative_sum(radius)
		l2 = fill_result_array(l, radius, l2, i)
		l, l2 = l2, l
	return l
