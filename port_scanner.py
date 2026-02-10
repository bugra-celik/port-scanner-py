import socket

target = input("Enter target IP: ")

print("Scanning target:", target)
print("Scanning ports 1-100...\n")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.25)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is open")
    
    s.close()

print("\nScan complete.")
