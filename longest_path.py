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

def walk(current, visited, path):
	for (to,dist) in adj[current]:
		if to not in visited:
			visited.add(to)
			path.append(to)
			walk(to, visited , path)

			visited.remove(to)
			path.pop()
			
	print(path)


start = 1
visited = {start}
path = [start]
walk(start, visited, path)