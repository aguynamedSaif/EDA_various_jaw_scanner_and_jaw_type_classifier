import os
import numpy as np
from stl import mesh

def calculate_rms(file1, file2):
    try:
        # Load the STL files
        mesh1 = mesh.Mesh.from_file(file1)
        mesh2 = mesh.Mesh.from_file(file2)

        # Extract the vertices from the STL files
        vertices1 = np.asarray(mesh1.vectors).reshape(-1, 3)
        vertices2 = np.asarray(mesh2.vectors).reshape(-1, 3)

        # Align the number of vertices
        num_vertices = min(vertices1.shape[0], vertices2.shape[0])
        vertices1 = vertices1[:num_vertices, :]
        vertices2 = vertices2[:num_vertices, :]

        # Calculate the squared differences between the vertices
        differences = vertices1 - vertices2
        squared_diff = np.sum(differences ** 2, axis=1)

        # Calculate the RMS value
        rms = np.sqrt(np.mean(squared_diff))

        return rms
    except Exception as e:
        print("Error:", e)
        return None


# Specify the paths to the folders containing the STL files
folder1_path = r'Processed'
folder2_path = r'Unprocessed'

# Get the list of files in both folders
folder1_files = os.listdir(folder1_path)
folder2_files = os.listdir(folder2_path)

# Iterate over the common files in both folders
common_files = set(folder1_files) & set(folder2_files)
for filename in common_files:
    file1_path = os.path.join(folder1_path, filename)
    file2_path = os.path.join(folder2_path, filename)

    # Calculate the RMS between the two STL files
    rms_value = calculate_rms(file1_path, file2_path)

    if rms_value is not None:
        print("RMS between", filename, ":", rms_value)
