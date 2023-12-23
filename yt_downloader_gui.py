import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pytube import YouTube
import threading
import time
def download(url, download_path, audio_only, progress_callback):
    try:
        yt = YouTube(url, on_progress_callback=progress_callback)
        stream = yt.streams.filter(only_audio=audio_only).first() if audio_only else yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def start_download():
    url = url_entry.get()
    download_path = path_entry.get()
    audio_only = var_audio_only.get()

    if not url or not download_path:
        messagebox.showwarning("Warning", "Please enter a YouTube URL and select a download path.")
        return
    progress_var.set(0)
    download_thread = threading.Thread(target=lambda: download(url, download_path, audio_only, on_progress))
    download_thread.start()
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = int((bytes_downloaded / total_size) * 100)
    progress_var.set(percentage_of_completion)
    root.update_idletasks()  # Update the GUI to reflect changes in  progress bar
def browse_path():
    download_directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, download_directory)
root = tk.Tk()
root.title("YouTube Downloader by kumaran R")
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)
path_label = tk.Label(root, text="Select Download Path:")
path_label.grid(row=1, column=0, sticky='e', padx=5, pady=5)
path_entry = tk.Entry(root, width=40)
path_entry.grid(row=1, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_path)
browse_button.grid(row=1, column=2, padx=5, pady=5)
var_audio_only = tk.BooleanVar()
audio_only_checkbutton = tk.Checkbutton(root, text="Download audio only", variable=var_audio_only)
audio_only_checkbutton.grid(row=2, column=1, sticky='w', padx=5, pady=5)
download_button = tk.Button(root, text="Start Download", command=start_download)
download_button.grid(row=3, column=1, pady=10)
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, length=300, variable=progress_var, maximum=100)
progress_bar.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
root.grid_columnconfigure(1, weight=1)
root.mainloop()