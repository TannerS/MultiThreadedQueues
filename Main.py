# http://stackoverflow.com/questions/2846653/how-to-use-threading-in-python
# http://stackoverflow.com/questions/16199793/python-3-3-simple-threading-event-example
# https://www.tutorialspoint.com/python3/python_multithreading.htm
# http://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished

import threading
import queue
from QueuedCharCount import QueuedCharCount
from QueuedFileRead import QueuedFileRead

def main():
    file_queue = queue.Queue(0)
    text_queue = queue.Queue(0)
    count_dic = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    file_thread = QueuedFileRead(100, "File Thread", file_queue, text_queue)
    char_thread = QueuedCharCount(200, "Text Thread", text_queue, count_dic)
    print("Started file parsing thread")
    file_thread.start()
    print("Start text counting thread")
    char_thread.start()


    while True:
        response = input("Enter a command -> read <file name>, print, and quit: ").replace('\n', '')
        response = response.strip().split()

        if 0 < len(response):
            if response[0] == "read":
                if 1 < len(response):
                    file = open(response[1], 'r')
                    file_queue.put(file)
            elif response[0] == "print":
                print ("Skipping ' ' and \\n.....")
                for key, value in count_dic.items():
                    print(key + ": " + str(value))
            elif response[0] == "quit":
                break
            else:
                print("Unknown command: " + str(response))




if __name__ == '__main__':
    main()