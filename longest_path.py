import sys

for line in sys.stdin:
	line = line.strip()
	parts = line.split(",")

	a = int(parts[0].strip())
	b = int(parts[1].strip())
	c = float(parts[2].strip())

	print((a,b,c))