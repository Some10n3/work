class Time:
    def __init__(self, H, M, S):
        self.H = H
        self.M = M
        self.S = S

        assert H <= 23 and H >= 0, "Incorrect Hour Input"
        assert M <= 59 and M >= 0, "Incorrect Minute Input"
        assert S <= 59 and S >= 0, "Incorrect Second Input"

    def get_hour(self):
        return self.H

    def set_hour(self, H):
        self.H = H
    
    def get_minute(self):
        return self.M
    
    def set_minute(self, M):
        self.M = M
    
    def get_second(self):
        return self.S
    
    def set_second(self, S):
        self.S = S
    
    def print(self):
        print("{:02d}:{:02d}:{:02d} Hrs.".format(self.H, self.M, self.S))

if __name__ == "__main__":
    time1 = Time(9, 30, 0)
    time1.print()