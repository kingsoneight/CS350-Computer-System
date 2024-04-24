import matplotlib.pyplot as plt

# Sample data (replace with your own data)
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [6.56, 20.06, 6.54, 7.21, 6.58, 6.7, 6.63, 6.88, 6.61, 6.78]

# Create the plot
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Times "Mid" Repeats')
plt.ylabel('Runtime')
plt.title('Line Plot of Runtime vs. Times "Mid" Repeats')

# Show the plot
plt.show()
