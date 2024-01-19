import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio
import os

# Parameters
n_frames = 30  # Number of frames in the GIF
n_max_points = 100  # Maximum number of data points

# Generate data
np.random.seed(42)
data = np.random.normal(size=(n_max_points, 2))

# Directory for temporary image files
os.makedirs('temp_images', exist_ok=True)

# Create each frame
filenames = []
for i in range(1, n_frames + 1):
    n_points = int(i * n_max_points / n_frames)
    current_data = data[:n_points, :]

    # Create figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Scatter plot of data points
    axs[0].scatter(current_data[:, 0], current_data[:, 1])
    axs[0].set_title(f"Data Points (n={n_points})")
    
    # KDE plot
    if n_points > 1:  # KDE requires at least 2 points
        sns.kdeplot(x=current_data[:, 0], y=current_data[:, 1], ax=axs[1])
    axs[1].set_title("Kernel Density Estimation")

    # Save the plot as an image
    filename = f'temp_images/frame_{i:03d}.png'
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

# Create GIF
with imageio.get_writer('data_kde_animation.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        os.remove(filename)  # Optionally remove the temporary file

# Clean up directory
os.rmdir('temp_images')

