import os
import psutil
from pocketsphinx import LiveSpeech

# Initialize psutil for process monitoring
process = psutil.Process(os.getpid())

speech = LiveSpeech(
    lm=False,
    kws="./keywords.list",
)

for phrase in speech:
    if "hello assistant" in str(phrase):
        print("Trigger phrase detected!")
        # Add additional actions here

    # Monitor and print CPU and memory usage
    cpu_usage = process.cpu_percent()
    memory_usage = process.memory_info().rss  # in bytes
    print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage / (1024 * 1024)} MB")
