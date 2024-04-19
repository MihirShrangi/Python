class modifier:
    public=20
    _protected=30
    __private=40
    def show(self):
        print("The private is",modifier.__private)

ob=modifier()
# print("The public is:",ob.public)
# print("The protected is:",ob._protected)

ob.show()