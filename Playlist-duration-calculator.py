import os
import tkinter as tk
from tkinter import filedialog, messagebox
from mutagen import File

SUPPORTED_FORMATS = ('.mp3', '.flac', '.wav', '.ogg', '.m4a')

def get_audio_duration(folder):
    total_duration = 0.0

    for filename in os.listdir(folder):
        if filename.lower().endswith(SUPPORTED_FORMATS):
            file_path = os.path.join(folder, filename)
            try:
                audio = File(file_path)
                if audio and audio.info:
                    total_duration += audio.info.length
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    minutes, seconds = divmod(int(total_duration), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {seconds}s"

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        duration = get_audio_duration(folder)
        result_label.config(text=f"Total Duration:\n{duration}")

# GUI Setup
root = tk.Tk()
root.title("Audio Playlist Duration Checker")
root.geometry("400x200")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(expand=True)

label = tk.Label(frame, text="Select a folder with audio files", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(frame, text="Choose Folder", command=select_folder, font=("Arial", 12))
button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
