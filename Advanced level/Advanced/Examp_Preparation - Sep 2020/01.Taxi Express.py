from collections import deque

taxi_clients = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = sum(taxi_clients)

while taxi_clients and taxis:
        current_client = taxi_clients[0]
        current_taxi = taxis[-1]
        if current_client <= current_taxi:
            taxi_clients.popleft()
            taxis.pop()
        else:
            taxis.pop()

if taxi_clients == deque([]):
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in taxi_clients])}")