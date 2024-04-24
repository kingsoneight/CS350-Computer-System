import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [23.03, 39.94, 55.44, 71.43, 88.27,
            103.39, 119.82, 136.73, 152.19, 192.06]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')

# Show the plot
plt.show()
