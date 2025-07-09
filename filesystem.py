class FileSystem:
    def __init__(self):
        self.files = {}

    def create(self, filename, content=""):
        self.files[filename] = content

    def read(self, filename):
        return self.files.get(filename, "File not found")


fs = FileSystem()
fs.create("hello.txt", "Hello, OS!")
print(fs.read("hello.txt"))
