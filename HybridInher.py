class watch:
    def time(self):
        print("Yon can watch time")

class Camera(watch):
    def photo(self):
        print("You can Click Photo")

class Flash(watch):
    def light(self):
        print("You can now light up the darkness")


class phone(Flash):
    def call(self):
        print("You can call...")


p1=phone()
p1.call()
p1.light()
p1.time()

f1=Flash()
f1.light()
f1.time()

