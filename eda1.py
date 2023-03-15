import cv2
import os
import csv
# Define the directory to search in
directory = '/media/shahidul/store1/t1/Isolated_Gloss_Renamed_Audioless'

# Use a list comprehension to find all .mp4 files in the directory and its subdirectories
mp4_files = [
    os.path.join(root, file) for root, dirs, files in os.walk(directory)
    for file in files if file.endswith('.mp4')
]

# write a csv file with the file name and the number of frames
with open('frame_counts1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['File Name', 'Folder_Name', 'File', 'Number of Frames'])
    # Loop through each mp4 file and get the number of frames
    for mp4_file in mp4_files:
        # Use OpenCV to read the video file
        cap = cv2.VideoCapture(mp4_file)
        if not cap.isOpened():
            print(f"Error opening video file: {mp4_file}")
            continue

        # Get the total number of frames in the video
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        data = mp4_file.split('/')
        file_name = data[-1]
        folder_name = data[-2]

        # Write the file name and number of frames to the csv file
        writer.writerow([mp4_file, folder_name, file_name, num_frames])

        # Release the VideoCapture object
        cap.release()
