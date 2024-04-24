import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [6.57, 6.62, 24.81, 30.58, 36.32,
            41.26, 47.9, 135.73, 152.19, 103.8]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')

# Show the plot
plt.show()
