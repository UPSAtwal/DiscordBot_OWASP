class Config:
    def __init__(self, filename):
        self.configpath = filename
        self.config = {}
        with open(self.configpath, "r") as file:
            for i in file.readlines():
                i = i.split("=")
                self.config[i[0]] = i[1].strip()

    def update(self, key, value):
        self.config[key] = value
        with open(self.configpath, 'w') as file:
            for i, j in self.config.items():
                file.write(f'{i}={j}\n')
    
    def val(self, key):
        return self.config[key]