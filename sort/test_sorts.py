from quicksort import quickSort
from mergesort import mergeSort
from radixsort import radixSort

TEST_CASES = {
	"tests" : [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 5, 4, 1],
        [21, 43, 42, 25, 14, 41],
        [13, 115, 24, 33, 21, 12]
	],
	"expected": [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 4, 4, 5],
        [14, 21, 25, 41, 42, 43],
        [12, 13, 21, 24, 33, 115]
	]
}

SORT_FUNCTIONS = {
	# "quickSort": quickSort,
	"radixSort": radixSort,
	"mergeSort": mergeSort
}

for sort_name, sort_function in SORT_FUNCTIONS.iteritems():
	for test, expected in zip(TEST_CASES["tests"], TEST_CASES["expected"]):
		assert sort_function(test) == expected
