import heapq

# Graf kecamatan dan tempat wisata (jarak dalam kilometer)
graph = {
    # Kecamatan
    'Tegalsari': {'Wonokromo': 4, 'Genteng': 3, 'Sawahan': 3},
    'Wonokromo': {'Dukuh Pakis': 5, 'Tegalsari': 4, 'Wiyung': 6, 'Kebun Binatang Surabaya': 2},
    'Genteng': {'Tegalsari': 3, 'Gubeng': 4, 'Balai Kota Surabaya': 2, 'Simokerto': 5},
    'Dukuh Pakis': {'Wonokromo': 5, 'Wiyung': 3, 'Karang Pilang': 7},
    'Wiyung': {'Dukuh Pakis': 3, 'Wonokromo': 6, 'Karang Pilang': 4},
    'Sawahan': {'Tegalsari': 3, 'Genteng': 4, 'Simokerto': 5},
    'Gubeng': {'Genteng': 4, 'Balai Kota Surabaya': 3, 'Rungkut': 8},
    'Simokerto': {'Genteng': 5, 'Kenjeran': 7, 'Tambaksari': 6},
    'Rungkut': {'Gubeng': 8, 'Gunung Anyar': 5, 'Sukolilo': 7},
    'Karang Pilang': {'Wiyung': 4, 'Dukuh Pakis': 7, 'Jambangan': 3},
    'Jambangan': {'Karang Pilang': 3, 'Gayungan': 4},
    'Gayungan': {'Jambangan': 4, 'Wonokromo': 5},
    'Tambaksari': {'Simokerto': 6, 'Kenjeran': 4, 'Sukolilo': 3},
    'Kenjeran': {'Tambaksari': 4, 'Simokerto': 7, 'Pantai Kenjeran': 2},
    'Sukolilo': {'Tambaksari': 3, 'Rungkut': 7},
    'Gunung Anyar': {'Rungkut': 5},
    'Balai Kota Surabaya': {'Genteng': 2, 'Gubeng': 3},

    # Tempat Wisata
    'Kebun Binatang Surabaya': {'Wonokromo': 2, 'Taman Bungkul': 2},
    'Taman Bungkul': {'Kebun Binatang Surabaya': 2, 'Tunjungan Plaza': 5},
    'Tugu Pahlawan': {'Sawahan': 6, 'Museum House of Sampoerna': 3},
    'Museum House of Sampoerna': {'Tugu Pahlawan': 3, 'Sawahan': 5},
    'Pantai Kenjeran': {'Kenjeran': 2, 'Jembatan Suramadu': 3},
    'Jembatan Suramadu': {'Pantai Kenjeran': 3, 'Pelabuhan Tanjung Perak': 5},
    'Pelabuhan Tanjung Perak': {'Jembatan Suramadu': 5, 'Suramadu Park': 2},
    'Suramadu Park': {'Pelabuhan Tanjung Perak': 2, 'Galaxy Mall': 6},
    'Galaxy Mall': {'Suramadu Park': 6, 'Taman Hiburan Pantai Kenjeran': 4},
    'Taman Hiburan Pantai Kenjeran': {'Galaxy Mall': 4, 'Kenjeran': 2},
    'House of Sampoerna': {'Sawahan': 3, 'Balai Pemuda Surabaya': 4},
    'Balai Pemuda Surabaya': {'House of Sampoerna': 4, 'Museum Pendidikan': 3},
    'Museum Pendidikan': {'Balai Pemuda Surabaya': 3, 'Gubeng': 2},
    'Tunjungan Plaza': {'Taman Bungkul': 5, 'Pasar Atom': 7},
    'Pasar Atom': {'Tunjungan Plaza': 7, 'Pasar Genteng': 3},
    'Pasar Genteng': {'Pasar Atom': 3, 'Museum 10 Nopember': 4},
    'Museum 10 Nopember': {'Pasar Genteng': 4, 'Monumen Kapal Selam': 2},
    'Monumen Kapal Selam': {'Museum 10 Nopember': 2, 'Balai Kota Surabaya': 3},
    'Kenjeran Park': {'Kenjeran': 5, 'Klenteng Sanggar Agung': 3},
    'Klenteng Sanggar Agung': {'Kenjeran Park': 3, 'Museum Kanker': 4},
    'Museum Kanker': {'Klenteng Sanggar Agung': 4, 'Mall Ciputra World': 8},
    'Mall Ciputra World': {'Museum Kanker': 8, 'Pakuwon Mall': 5},
    'Pakuwon Mall': {'Mall Ciputra World': 5, 'Ciputra Waterpark': 6},
    'Ciputra Waterpark': {'Pakuwon Mall': 6}
}

# Heuristic untuk tiap node (masukkan sesuai perkiraan jarak sebenarnya dari setiap node ke tujuan)
heuristic = {
    'Tegalsari': 6, 'Wonokromo': 5, 'Dukuh Pakis': 7, 'Wiyung': 10,
    'Sawahan': 7, 'Genteng': 5, 'Gubeng': 4, 'Simokerto': 9, 'Rungkut': 12,
    'Karang Pilang': 11, 'Jambangan': 9, 'Gayungan': 8, 'Tambaksari': 6,
    'Kenjeran': 15, 'Sukolilo': 10, 'Gunung Anyar': 14, 'Balai Kota Surabaya': 3,

    # Tempat Wisata
    'Kebun Binatang Surabaya': 10, 'Taman Bungkul': 8, 'Tugu Pahlawan': 15,
    'Museum House of Sampoerna': 12, 'Pantai Kenjeran': 20,
    'Jembatan Suramadu': 18, 'Pelabuhan Tanjung Perak': 12,
    'Suramadu Park': 18, 'Galaxy Mall': 12, 'Taman Hiburan Pantai Kenjeran': 25,
    'House of Sampoerna': 13, 'Balai Pemuda Surabaya': 10, 'Museum Pendidikan': 8,
    'Tunjungan Plaza': 9, 'Pasar Atom': 11, 'Pasar Genteng': 10,
    'Museum 10 Nopember': 13, 'Monumen Kapal Selam': 14, 'Kenjeran Park': 18,
    'Klenteng Sanggar Agung': 15, 'Museum Kanker': 10, 'Mall Ciputra World': 7,
    'Pakuwon Mall': 8, 'Ciputra Waterpark': 12
}

# Kecepatan rata-rata kendaraan (km/jam)
vehicle_speed = {
    'mobil': 40,
    'motor': 60,
    'jalan kaki': 5  # Mengganti sepeda dengan jalan kaki
}

# A* search function to find the best route
def a_star_search(graph, heuristic, start, goal, vehicle):
    # The open list stores nodes to explore, sorted by f_cost (f = g + h)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, 0, start))  # (f_cost, g_cost, time_cost, node)
    
    # Dictionaries to store the best g_cost, time_cost, and parents
    parents = {start: None}
    g_costs = {start: 0}
    time_costs = {start: 0}

    # Prepare to return the results
    path = []
    total_cost = 0
    total_time = 0
    
    # Iterate through nodes in the open list
    while open_list:
        _, current_g, current_time, current_node = heapq.heappop(open_list)
        
        if current_node == goal:  # If we reached the destination
            node = current_node
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            total_cost = current_g
            total_time = current_time
            break

        # Explore neighbors
        for neighbor, distance in graph[current_node].items():
            new_g = current_g + distance
            new_time = current_time + (distance / vehicle_speed[vehicle]) * 60  # Convert to minutes
            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                time_costs[neighbor] = new_time
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, new_g, new_time, neighbor))
                parents[neighbor] = current_node

    if path:
        return path, total_cost, total_time
    else:
        print("Path not found!")
        return None, 0, 0


# Main function to handle the user input and call the A* search
def get_trip_details():
    start = input("Masukkan titik awal keberangkatan: ")
    goal1 = input("Masukkan titik tujuan pertama: ")
    goal2 = input("Masukkan titik tujuan kedua (opsional): ")
    goal3 = input("Masukkan titik tujuan ketiga (opsional): ")
    goals = [goal for goal in [goal1, goal2, goal3] if goal]

    return_point = input("Masukkan titik akhir kepulangan: ")
    vehicle = input("Pilih moda transportasi (mobil/motor/jalan kaki): ").lower()

    if vehicle not in vehicle_speed:
        print("Jenis kendaraan tidak valid!")
        return None, 0, 0, None

    # Initialize variables to keep track of the route
    all_paths = []
    total_cost = 0
    total_time = 0

    # Start from the initial point and compute the route for each goal sequentially
    current_location = start

    for goal in goals:
        path, cost, time = a_star_search(graph, heuristic, current_location, goal, vehicle)
        if path:
            all_paths.append((path, cost, time))
            total_cost += cost
            total_time += time
            current_location = goal  # Update current location to the last goal reached
        else:
            print(f"Rute menuju {goal} tidak ditemukan.")
            return None, 0, 0

    # Finally, calculate the route to the return point from the last goal
    return_path, return_cost, return_time = a_star_search(graph, heuristic, current_location, return_point, vehicle)
    if return_path:
        all_paths.append((return_path, return_cost, return_time))
        total_cost += return_cost
        total_time += return_time
    else:
        print(f"Rute menuju titik kepulangan {return_point} tidak ditemukan.")
        return None, 0, 0

    return all_paths, total_cost, total_time


# Display the results
def display_results(paths, total_cost, total_time):
    if paths:
        print("\nRute terbaik:")
        for i, (path, cost, time) in enumerate(paths, start=1):
            print(f"Tujuan {i}: {path}")
            print(f"  Jarak: {cost} km")
            print(f"  Waktu: {time} menit")
        print(f"\nTotal jarak: {total_cost} km")
        print(f"Total waktu: {total_time} menit")
    else:
        print("Tidak ada rute yang ditemukan!")


# Get trip details from the user and display results
paths, total_cost, total_time = get_trip_details()
display_results(paths, total_cost, total_time)

