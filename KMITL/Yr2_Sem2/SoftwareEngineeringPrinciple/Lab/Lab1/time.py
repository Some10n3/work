class time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second) + " hrs"
    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def get(self):
        return self.hour, self.minute, self.second

def __main__():
    t = time(10, 10, 10)
    print(t)
    t.set(11, 11, 11)
    print(t)
    print(t.get())

if __name__ == "__main__":
    __main__()