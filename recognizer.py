import os
import psutil
from pocketsphinx import LiveSpeech

# Initialize psutil for process monitoring
process = psutil.Process(os.getpid())

speech = LiveSpeech(
    lm=False,
    kws="./keywords.list",
)

conversation_active = False


def init_conversation(conversation_active):
    if conversation_active:
        print("Conversation already ongoing!")
        return False
    # code for starting conversation here (record audio, etc.)
    print("Conversation started!")
    return True


for phrase in speech:
    if "hello assistant" in str(phrase):
        print("Trigger phrase detected!")

        if not conversation_active:
            if init_conversation(conversation_active):
                conversation_active = True
                continue

        # Add additional actions here

    if "done now" in str(phrase):
        print("Conversation ended!")
        conversation_active = False
        continue
    # Monitor and print CPU and memory usage
    cpu_usage = process.cpu_percent()
    memory_usage = process.memory_info().rss  # in bytes
    print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage / (1024 * 1024)} MB")
