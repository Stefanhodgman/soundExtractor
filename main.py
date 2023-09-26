from tkinter import filedialog, Tk
from moviepy.editor import VideoFileClip
import os

# Function to convert MP4 to MP3
def convert_mp4_to_mp3(video_path, mp3_folder):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_filename = os.path.join(mp3_folder, os.path.basename(video_path).replace(".mp4", ".mp3"))
    audio.write_audiofile(audio_filename)
    video.close()
    audio.close()

# Initialize Tkinter
root = Tk()
root.withdraw()  # Hide the main window

# Ask user to select folder
folder_selected = filedialog.askdirectory(title="Select Folder containing the MP4 files (All files in all subfolders will be used")

# Create MP3 folder in the root directory if it doesn't exist
mp3_folder = os.path.join(folder_selected, "MP3")
if not os.path.exists(mp3_folder):
    os.mkdir(mp3_folder)

# Walk through the folder and subfolders to find MP4 files
for dirpath, _, filenames in os.walk(folder_selected):
    for filename in filenames:
        if filename.endswith(".mp4"):
            video_path = os.path.join(dirpath, filename)
            convert_mp4_to_mp3(video_path, mp3_folder)

print("Conversion Completed!")
