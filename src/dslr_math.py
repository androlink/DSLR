


class DslrExeption(Exception):
	def __init__(self, message):
		super(Exception, message)

def dslr_min_2(v1: float, v2: float):
	return v1 if v1 < v2 else v2


def dslr_min(l: list[float]) -> float:
	if len(l) < 1:
		raise DslrExeption("can't min empty list")
	m = l[0]
	for v in l:
		m = dslr_min_2(m, v)
	return m

def dslr_max_2(v1: float, v2: float):
	return v1 if v1 > v2 else v2


def dslr_max(l: list[float]) -> float:
	if len(l) < 1:
		raise DslrExeption("can't max empty list")
	m = l[0]
	for v in l:
		m = dslr_max_2(m, v)
	return m

def dslr_mean(l: list[float]) -> float:
	if len(l) < 1:
		raise DslrExeption("can't mean empty list")
	l_sum = sum(l)
	return l_sum / len(l)

def dslr_count(l: list[float], value: float) -> int:
	count = 0
	for v in l:
		if v == value:
			count += 1
	return count

def dslr_quartile(l: list, percent: float)-> float:
	l.sort();
	return l[round(len(l) * percent)]

def dslr_stddev(l:list[float]) -> float:
	mean = dslr_mean(l)
	s = sum([(x - mean) ** 2 for x in l])
	e = (1 / (len(l) - 1)) * s
	return e ** 0.5
	
def dslr_count_none(l: list[float]) -> int:
  count = 0
  for value in l:
    if value == None:
      count += 1
  return count

if __name__ == "__main__":
	assert 2 == dslr_mean([0, 1, 2, 3, 4]), "mean"
	assert 1 == dslr_count([0, 1, 2, 3, 4], 2), "count"
	assert -1 == dslr_min([-1, 0, 1, 2, 3, 4]), "min"
	assert 4 == dslr_max([-1, 0, 1, 2, 3, 4]), "max"
	assert 25 == dslr_quartile(list(range(0, 100)), 0.25), "quartile 25"
	assert 50 == dslr_quartile(list(range(0, 100)), 0.50), "quartile 50"
	assert 75 == dslr_quartile(list(range(0, 100)), 0.75), "quartile 75"
	assert  0.00001 > abs(5.2372293656638 - dslr_stddev([10, 12, 23, 23, 16, 23, 21, 16])), "stddev"
