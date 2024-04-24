import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [14.11, 20.36, 26.87, 33.4, 39.64,
            45.26, 52.66, 57.3, 65.12, 71]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')

# Show the plot
plt.show()
