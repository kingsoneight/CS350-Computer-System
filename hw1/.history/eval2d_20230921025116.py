import subprocess
import matplotlib.pyplot as plt

a_values = list(range(1, 13))

a_parameters = []
server_utilization = []

for a in a_values:
    # Run the server and client with the current -a value
    command = ["/usr/bin/time", "-v", "./server", "2222", "&", "../client", "-a", str(a), "-s", "12", "-n", "500", "2222"]
    result = subprocess.run(" ".join(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Extract the server utilization from the result
    lines = result.stderr.split("\n")
    for line in lines:
        if "User time (seconds):" in line:
            utilization = float(line.split(":")[1].strip())
    
    # Store the -a value and server utilization
    a_parameters.append(a)
    server_utilization.append(utilization)

plt.plot(a_parameters, server_utilization, marker='o')
plt.xlabel('Arrival Rate (-a)')
plt.ylabel('Server Utilization')
plt.title('Server Utilization vs. Arrival Rate (-a)')
plt.grid(True)
plt.show()
