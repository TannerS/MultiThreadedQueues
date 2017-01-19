import queue
import threading

class QueuedCharCount (threading.Thread):
    id = None
    name = None
    text_queue = None
    count_dic = None

    def __init__(self, id, name, text_queue, count_dic):
        # http://stackoverflow.com/questions/31851514/how-does-thread-init-self-in-a-class-work
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.text_queue = text_queue
        self.count_dic = count_dic

    def run(self):
        # i = 0
        while True:
            # i += 1
            # print("GET READ FILE: " + str(i))
            queue_str = self.text_queue.get(block=True, timeout=None)
            # print("GET READ FILE END: " + str(i))
            for letter in queue_str:
                if (letter != ' ') and (letter != '\n'):
                    self.count_dic[letter] += 1

