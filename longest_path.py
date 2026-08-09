import sys
import time

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

total_weight = 0
for station in adj:
	for (to, dist) in adj[station]:
		total_weight += dist
total_weight = total_weight/2


best_distance = 0
best_path = [next(iter(adj))]

start_time = time.time()
TIME_LIMIT = 30
timed_out = False


def walk(current, visited, path, current_distance):
	global best_distance, best_path, timed_out

	if timed_out:
		return

	if time.time() - start_time > TIME_LIMIT:
		timed_out = True
		return

	remaining = total_weight - current_distance
	if current_distance + remaining <= best_distance:
		return

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
		if timed_out:
			break
		visited = {start}
		path = [start]
		walk(start, visited, path, 0)

str_path = [str(x) for x in best_path]
output = "\r\n".join(str_path) + "\r\n"
print(output, end="")