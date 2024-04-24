import subprocess
import matplotlib.pyplot as plt

a_values = list(range(1, 13))

a_parameters = [1,10]
server_utilization = [7,79,]



plt.plot(a_parameters, server_utilization, marker='o')
plt.xlabel('Arrival Rate')
plt.ylabel('Server Utilization')
plt.title('Server Utilization vs. Arrival Rate (-a)')
plt.show()
