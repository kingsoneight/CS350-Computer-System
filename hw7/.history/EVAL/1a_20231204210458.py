import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [22.9, 38.9, 55.14, 71.43, 87.27,
            103.39, 129.82, 135.73, 152.19, 192.06]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')

# Show the plot
plt.show()
