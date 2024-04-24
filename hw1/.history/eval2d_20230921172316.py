import subprocess
import matplotlib.pyplot as plt

a_values = list(range(1, 13))

a_parameters = [1,2,3,4,5,6,7,8,9,10,11,12]
server_utilization = [7,15,24,31,39,47,55,63,71,79,86,94]



plt.plot(a_parameters, server_utilization, marker='o')
plt.xlabel('Arrival Rate')
plt.ylabel('Server Utilization (%)')
plt.title('Server Utilization vs. Arrival Rate')
plt.show()
