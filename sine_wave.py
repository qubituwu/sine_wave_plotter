import matplotlib.pyplot as plt
import numpy as np

# Generate values for x-axis with a different frequency
x = np.linspace(0, 2 * np.pi, 1000)  # Adjust the range according to your desired frequency

# Generate sine wave values for y-axis
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y = sin(x)')
plt.title('Modified Sine Wave with Different Frequency')
plt.grid(True)
plt.show()
