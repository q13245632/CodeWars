# 自己的解法
class FileMaster():
    def __init__(self, filepath):
    	self.filepath = filepath
        #Your code here
    def extension(self):
    	arr = self.filepath.split(".")
    	return arr[1]
        #Your code here
    def filename(self):
    	arr = self.filepath.split(".")
    	path = arr[0].split("/")
    	return path[len(path)-1]
        #Your code here
    def dirpath(self):
    	arr = self.filepath.split(".")
    	path = arr[0].split("/")
    	return "/".join(path[:-1]) + "/"

# 思路
class FileMaster():
    def __init__(self, filepath):
        lk = filepath.rfind('.')
        ls = filepath.rfind('/')
        self.ext = filepath[lk+1:]
        self.file = filepath[ls+1:lk]
        self.path = filepath[:ls+1]
    def extension(self):
        return self.ext
    def filename(self):
        return self.file
        
    def dirpath(self):
        return self.path