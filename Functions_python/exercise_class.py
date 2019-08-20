class String:
    
    def __init__(self, text):
        self.text = text

    def get_list(self):
        return list(self.text)

    def get_tuple(self):
        return tuple(self.text)

a = String("text")
print(a.get_list())   
print(a.get_tuple()) 