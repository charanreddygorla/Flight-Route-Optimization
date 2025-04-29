import heapq
from graphviz import Digraph

def dijkstra(graph, start, end):
    queue = [(0, start, 0, [])]
    distances = {vertex: float('infinity') for vertex in graph}
    costs = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    costs[start] = 0
    shortest_path = []

    while queue:
        current_distance, current_vertex, current_cost, path = heapq.heappop(queue)

        if current_vertex == end:
            return current_distance, current_cost, path

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, (weight, cost, flight_number) in graph[current_vertex].items():
            distance = current_distance + weight
            total_cost = current_cost + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                costs[neighbor] = total_cost
                heapq.heappush(queue, (distance, neighbor, total_cost, path + [(current_vertex, neighbor, flight_number)]))
                shortest_path = path + [(current_vertex, neighbor, flight_number)]

    return float('infinity'), float('infinity'), []

def find_all_paths(graph, start, end, path=[], cost=0, flights=[]):
    path = path + [start]
    if start == end:
        return [(path, cost, flights)]
    if start not in graph:
        return []
    paths = []
    for node, (weight, node_cost, flight_number) in graph[start].items():
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path, cost + node_cost, flights + [(start, node, flight_number)])
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def generate_graph(graph, highlighted_path):
    dot = Digraph(comment='Flight Graph')
    
    for u, edges in graph.items():
        for v, (_, _, flight) in edges.items():
            dot.edge(u, v, label=flight)
    
    for u, v, flight in highlighted_path:
        dot.node(u, style='filled', fillcolor='lightblue')
        dot.node(v, style='filled', fillcolor='lightblue')
        dot.edge(u, v, label=flight, color='red', penwidth='2')
    
    return dot

def display_and_book_flight(path):
    for (u, v, flight) in path:
        print(f"{u} -> {v} via flight {flight}")
    
    print("\nSelect payment method:")
    print("1. UPI")
    print("2. Debit Card")
    print("3. Credit Card")
    payment_method = int(input("Enter the payment method number: ").strip())
    
    if payment_method == 1:
        upi_number = input("Enter your UPI number: ").strip()
        print(f"Payment method selected: UPI")
        print("Your flight is booked using UPI number:", upi_number)
    elif payment_method in [2, 3]:
        card_number = input("Enter your 16-digit card number: ").strip()
        expiry_date = input("Enter the expiry date (MM/YY): ").strip()
        cvv = input("Enter the CVV: ").strip()
        if len(card_number) == 16 and len(cvv) == 3:
            payment_methods = {2: "Debit Card", 3: "Credit Card"}
            print(f"Payment method selected: {payment_methods[payment_method]}")
            print("Your flight is booked using card number:", card_number)
        else:
            print("Invalid card number or CVV.")
    else:
        print("Invalid payment method selected.")

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        total_distance += graph[u][v][0]
    return total_distance

def calculate_total_cost(path, graph):
    total_cost = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        total_cost += graph[u][v][1]
    return total_cost

def print_all_path_details(all_paths, graph):
    for i, (path, cost, flights) in enumerate(all_paths):
        print(f"Path {i+1}: {' -> '.join(path)}")
        print(f"Total Distance: {calculate_total_distance(path, graph)}")
        print(f"Total Cost: {cost}")

graph = {
    'Coimbatore': {'Hyderabad': (2, 11673, 'AI101'), 'Banglore': (2, 4987, 'AI102'), 'Chennai': (1, 4060, 'AI103')},
    'Chennai': {'Vijayawada': (1.45, 3326, 'AI104'), 'Mumbai': (2.3, 3956, 'AI105')},
    'Banglore': {'Delhi': (2.45, 7856, 'AI106'), 'Hyderabad': (1.3, 4331, 'AI107'), 'Mumbai': (3, 9856, 'AI108')},
    'Hyderabad': {'Delhi': (2.15, 5264, 'AI109'), 'Vijayawada': (0.45, 4690, 'AI110'), 'Mumbai': (1.15, 3428, 'AI111')},
    'Delhi': {'Chennai': (3.15, 9469, 'AI112'), 'Coimbatore': (3, 14173, 'AI113')},
    'Mumbai': {'Delhi': (2.05, 5139, 'AI114'), 'Vijayawada': (2, 6512, 'AI115'), 'Coimbatore': (1.45, 7283, 'AI116')},
    'Vijayawada': {'Delhi': (2, 6661, 'AI117'), 'Coimbatore': (1.1, 6482, 'AI118')}
}

source = input("Enter the source vertex: ").strip()
destination = input("Enter the destination vertex: ").strip()

while True:
    print("\nMenu:")
    print("1. Display Fastest Flight and Book Flight")
    print("2. Display All Possibilities and Book Flight")
    print("3. Display the Graph")
    print("4. Exit")
    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        shortest_distance, shortest_cost, shortest_path = dijkstra(graph, source, destination)
        if shortest_distance == float('infinity'):
            print(f"No path found from {source} to {destination}")
        else:
            print(f"The shortest time from {source} to {destination} is {shortest_distance}")
            print(f"The total cost from {source} to {destination} is {shortest_cost}")
            print("The shortest path is:")
            display_and_book_flight(shortest_path)
    elif choice == 2:
        all_paths = find_all_paths(graph, source, destination)
        print(f"\nAll possible paths from {source} to {destination} are:")
        print_all_path_details(all_paths, graph)
        selected_path = int(input(f"Enter the path number you want to select (1-{len(all_paths)}): ").strip())
        if 1 <= selected_path <= len(all_paths):
            print("You have selected the following path:")
            for (u, v, flight) in all_paths[selected_path - 1][2]:
                print(f"{u} -> {v} via flight {flight}")
            display_and_book_flight(all_paths[selected_path - 1][2])
        else:
            print("Invalid path selection.")
    elif choice == 3:
        shortest_distance, shortest_cost, shortest_path = dijkstra(graph, source, destination)
        if shortest_distance == float('infinity'):
            print(f"No path found from {source} to {destination}")
        else:
            dot = generate_graph(graph, shortest_path)
            dot.render('highlighted_flight_graph', format='png', cleanup=True, view=True)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")