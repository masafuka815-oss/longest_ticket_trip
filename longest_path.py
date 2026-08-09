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


best_distance = 0
best_path = 0


def walk(current, visited, path, current_distance):
	global best_distance, best_path
	
	for (to,dist) in adj[current]:
		if to not in visited:
			visited.add(to)
			path.append(to)
			walk(to, visited , path, current_distance + dist)

			visited.remove(to)
			path.pop()


	if current_distance > best_distance:
		best_distance = current_distance
		best_path = path[:]


for start in adj.keys():
		visited = {start}
		path = [start]
		walk(start, visited, path, 0)

print(best_path, best_distance)