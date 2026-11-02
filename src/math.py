
class DslrExeption(Exception):
	def __init__(self, message)
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

def dslr_quartile(l: list, percent: float):
	l = list(l)
	l.sort();
	return l[round(len(l) * percent)]

if __name__ == "__main__":
	pass
