import math, time
class Test():
    def __init__(self) -> None:
        self.cant1 = 0
        self.cant2 = 0
        self.cant3 = 0
        self.r = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 35, 40, 42, 50, 51, 68, 71, 80, 89, 100, 121, 140, 141, 146, 150, 168]

    def vn_function(self, n):
        if n <= 0:
            return 0 
        if n == 1:
            return self.r[1]
        v = self.r[n]
        for i in range(1, math.ceil(n/2) + 1):
            self.cant1+=1
            c = self.vn_function(n - i) + self.vn_function(i)
            if c > v: v = c
        return v

    def opt(self, n):
        if n==0: return 0
        max = 0
        for i in range(1, n+1):
            v = self.r[i] + self.opt(n-i)
            self.cant2 += 1
            if v > max:
                max = v
        return max
    
    def dp(self, n, m):
        if m[n] != None: return m[n]
        max = 0
        for i in range(1, n+1):
            v = self.r[i] + self.dp(n-i, m)
            self.cant3 += 1
            if v > max:
                max = v
        m[n] = max
        return m[n]
    
    def call_dp(self, n):
        m = [None]*(n+1)
        m[0] = 0
        return self.dp(n, m)

if __name__ == "__main__":
    test = Test()
    #print([test.vn_function(i) for i in range(1,11)])
    #print([test.opt(i) for i in range(1,11)])
    print(len(test.r))
    print(test.vn_function(len(test.r) -1))
    print(test.opt(len(test.r) -1))
    print(test.call_dp(len(test.r) -1))
    
    print(test.cant1)
    print(test.cant2)
    print(test.cant3)