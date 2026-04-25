import time
from pynput.keyboard import Key, Controller
import keyboard as kb

keyboard = Controller()

# ------------------------------------- Your song notes ---------------------------------------
song = "ADD YOUR SONG NOTES HERE"
# ---------------------------------------------------------------------------------------------
delay = 0.2

print("Starting in 5 seconds... switch to Roblox!")
time.sleep(5)

print("Playing... Press ESC to stop.")

notes = song

for note in notes:
    if kb.is_pressed('esc'):
        print("Script stopped.")
        break

    if not note.strip():
        continue

    try:
        if note.startswith('[') and note.endswith(']'):
            for char in note[1:-1]:
                keyboard.press(char)
            for char in note[1:-1]:
                keyboard.release(char)
        else:
            keyboard.press(note)
            keyboard.release(note)
        time.sleep(delay)
    except ValueError:
        print(f"Skipping invalid key: {note}")
