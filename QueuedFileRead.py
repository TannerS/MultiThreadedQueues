import queue
import threading

class QueuedFileRead (threading.Thread):
    id = None
    name = None
    file_queue = None
    text_queue = None

    def __init__(self, id, name, file_queue, text_queue):
        # http://stackoverflow.com/questions/31851514/how-does-thread-init-self-in-a-class-work
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.file_queue = file_queue
        self.text_queue = text_queue

    def run(self):
        # i = 0
        while True:
            # https://docs.python.org/3/library/queue.html
            file = self.file_queue.get(block=True, timeout=None)
            file_content = file.read()
            # i += 1
            # print("PUT FILE: " + str(i))
            self.text_queue.put(file_content)
            # print("PUT FILE END " + str(i))
