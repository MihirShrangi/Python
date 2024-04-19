class FilesOne:
    def __init__(self,Name,Mode):
        self.f1=open(Name,Mode)
    def __del__(self):
        self.f1.close()
    def wrt(self,mat):
        self.f1.write(mat)
        print("File is Created Sucessfully....")

    def rd(self):
        data=self.f1.read()
        return data