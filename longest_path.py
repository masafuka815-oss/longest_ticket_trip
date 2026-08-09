import sys

adj = {}


for line in sys.stdin:
	line = line.strip()
	parts = line.split(",")

	a = int(parts[0].strip())
	b = int(parts[1].strip())
	c = float(parts[2].strip())

	

	if a not in adj:
		adj[a] = []
	if b not in adj:
		adj[b] = []

	adj[a].append((b,c))
	adj[b].append((a,c))

print(adj)