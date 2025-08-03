
import pickle
import numpy as np
import matplotlib.pyplot as plt

def plot_data_from_pickle(pickle_file='data.pickle', output_image='raw_data_plot.png'):
    """
    Loads data from a pickle file, and plots the mean of the first two channels against each other.

    Args:
        pickle_file (str): Path to the input pickle file.
        output_image (str): Path to save the output PNG image.
    """
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    # Remove the specified data point if it exists
    if "20250614_180011_test" in data:
        del data["20250614_180011_test"]

    # Extract the means of the first two channels and labels
    labels = list(data.keys())
    channel0_means = []
    channel1_means = []
    for key in labels:
        # data[key] is a dict {0: [...], 1: [...], 2: [...]}
        channel0_means.append(np.mean(data[key][0]))
        channel1_means.append(np.mean(data[key][1]))

    # Create a scatter plot
    plt.figure(figsize=(10, 8))
    plt.scatter(channel0_means, channel1_means)

    # Add labels to the points
    for i, label in enumerate(labels):
        plt.annotate(label, (channel0_means[i], channel1_means[i]))

    plt.xlabel('Mean of Channel 0')
    plt.ylabel('Mean of Channel 1')
    plt.title('Sensor Data (Mean of First Two Channels)')
    plt.grid(True)

    # Save the plot
    plt.savefig(output_image)
    print(f"Plot saved to {output_image}")

if __name__ == '__main__':
    plot_data_from_pickle()
