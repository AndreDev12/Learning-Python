from datetime import timedelta, datetime

# def arrival_time(hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime("Arrival: %A %H:%M")

# print(arrival_time(0)) # fecha actual

# Combinación de argumentos y argumentos de palabra clave
def arrival_time(destination, hours = 51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon"))
print(arrival_time("Orbit", 0.13))