from pytube import YouTube
import threading
import time
def download(url, download_path, audio_only=False):
    def on_progress(stream, chunk, bytes_remaining):
        nonlocal start_time
        bytes_downloaded = total_size - bytes_remaining
        download_speed = bytes_downloaded / (time.time() - start_time) if start_time else 0
        percentage_of_completion = int((bytes_downloaded / total_size) * 100)
        print(
            f"\rDownloaded {bytes_downloaded}/{total_size} ({percentage_of_completion}%) at {download_speed:.2f} bytes/s ",
            end="")
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(only_audio=audio_only).first() if audio_only else yt.streams.get_highest_resolution()
        total_size = stream.filesize
        # Print initial message before starting download thread
        print(f"Starting download. File size is {total_size} bytes.")
        start_time = time.time()
        stream.download(output_path=download_path)
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
def main():
    url = input("Enter the YouTube video URL: ")
    path = input("Enter the download path: ")
    audio_only = input("Download audio only? (yes/no): ").lower() == "yes"
    # Create and start the download thread
    download_thread = threading.Thread(target=lambda: download(url, path, audio_only))
    download_thread.start()
    download_thread.join()  # Wait for the download thread to finish
if __name__ == "__main__":
    main()