class Mngr:
    def __init__(self):
        self.a = []
    
    def add_p(self, n, t):
        self.a.append({"n": n, "t": t})

    def f_p(self, n):
        for p in self.a:
            if p["n"] == n:
                return p["t"]
        return None

def main():
    m = Mngr()
    m.add_p("Alex", "Manager")
    m.add_p("Chris", "Developer")
    
    print(m.f_p("Alex"))  # Outputs: Manager
    print(m.f_p("Jordan"))  # Outputs: None

if __name__ == "__main__":
    main()
