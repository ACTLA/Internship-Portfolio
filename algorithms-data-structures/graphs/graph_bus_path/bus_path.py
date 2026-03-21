import heapq

def find_fastest_path(n_stops, routes, start_stop, end_stop):
    adj = {}
    stop_to_routes = {}
    for r_idx, route in enumerate(routes):
        for stop in route:
            if stop not in stop_to_routes:
                stop_to_routes[stop] = []
            stop_to_routes[stop].append(r_idx)
            curr_node = (stop, r_idx)
            if curr_node not in adj: adj[curr_node] = []
            
    for r_idx, route in enumerate(routes):
        for i in range(len(route) - 1):
            u, v = route[i], route[i+1]
            adj[(u, r_idx)].append(((v, r_idx), 1))
            adj[(v, r_idx)].append(((u, r_idx), 1))
            
    for stop, r_indices in stop_to_routes.items():
        for i in range(len(r_indices)):
            for j in range(i + 1, len(r_indices)):
                r1, r2 = r_indices[i], r_indices[j]
                adj[(stop, r1)].append(((stop, r2), 3))
                adj[(stop, r2)].append(((stop, r1), 3))

    pq = []
    distances = {}
    predecessors = {}
    
    if start_stop not in stop_to_routes:
        return None, None
        
    for r_idx in stop_to_routes[start_stop]:
        node = (start_stop, r_idx)
        distances[node] = 0
        heapq.heappush(pq, (0, node))
        
    min_total_dist = float('inf')
    best_end_node = None

    while pq:
        d, (curr_stop, curr_route) = heapq.heappop(pq)
        
        if d > distances.get((curr_stop, curr_route), float('inf')):
            continue
            
        if curr_stop == end_stop:
            if d < min_total_dist:
                min_total_dist = d
                best_end_node = (curr_stop, curr_route)
            
        if (curr_stop, curr_route) in adj:
            for neighbor, weight in adj[(curr_stop, curr_route)]:
                new_dist = d + weight
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = (curr_stop, curr_route) # Запоминаем путь
                    heapq.heappush(pq, (new_dist, neighbor))
                    
    path = []
    if best_end_node:
        curr = best_end_node
        while curr in predecessors:
            path.append(curr)
            curr = predecessors[curr]
        path.append(curr)
        path.reverse()
        
    return (min_total_dist, path) if min_total_dist != float('inf') else (None, None)

if __name__ == "__main__":
    print("Задание 4: Поиск кратчайшего пути между остановками")
    try:
        n = int(input("Введите количество остановок: "))
        r = int(input("Введите количество маршрутов: "))
        
        all_routes = []
        for i in range(r):
            route_input = input(f"Введите остановки маршрута {i+1} через пробел: ")
            all_routes.append([int(x) for x in route_input.split()])
            
        start = int(input("Введите начальную остановку (I): "))
        end = int(input("Введите конечную остановку (J): "))
        
        dist, path = find_fastest_path(n, all_routes, start, end)
        
        if dist is not None:
            print(f"\nМинимальное время в пути: {dist}")
            # Форматированный вывод пути
            path_str = ""
            for i, (stop, r_idx) in enumerate(path):
                if i > 0:
                    prev_stop, prev_route = path[i-1]
                    if prev_stop == stop:
                        path_str += f" --[Пересадка на м-т {r_idx+1}]--> "
                    else:
                        path_str += " -> "
                path_str += f"Ост. {stop} (м-т {r_idx+1})"
            print(f"Путь: {path_str}")
        else:
            print("\nПуть между указанными остановками не найден.")
            
    except ValueError:
        print("Ошибка: вводите только целые числа.")