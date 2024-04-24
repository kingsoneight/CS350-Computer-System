import matplotlib.pyplot as plt

# Sample data (replace with your own data)

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [23.03, 39.94, 55.44, 71.43, 88.27,
            103.39, 119.82, 136.73, 152.48, 168.26]

x_values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values2 = [14.11, 20.36, 26.87, 33.4, 39.64,
             45.26, 52.66, 57.3, 65.12, 71]

x_values3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values3 = [6.57, 15, 24.81, 30.58, 36.32,
             41.26, 47.9, 61, 80, 103.8]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-', label="Part 1")
plt.plot(x_values2, y_values2, marker='o', linestyle='-', label="Part 2")
plt.plot(x_values3, y_values3, marker='o', linestyle='-', label="Part 3")

print([x_values3[i]-x_values2[i] for i in list(range(10))])
# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')
plt.legend()

# Show the plot
plt.show()
