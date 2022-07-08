import re
class Circle:

    def __init__(self, color='blue', radius=5):
        self.color = color
        self.radius = radius

    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

class Rectangle:

    def __init__(self, color='red', width=0, height=0):
        self.color = color
        self.width = width
        self.height = height

class analysedText:
    
    def __init__ (self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]','', text)
        self.fmtText = text
        return self.fmtText

    
    def freqAll(self):
        self.splits = self.fmtText.split()        
        #self.fmtText.split()
        frequency = []
        unique_words = []
        for word in self.splits:
            if word not in unique_words:
                unique_words.append(word)

        for i in unique_words:
            frequency.append(self.splits.count(i))

        self.dic = {key:value for key, value in zip(unique_words, frequency)}
        return self.dic

    
    def freqOf(self,word):
        return self.splits.count(word)


# circle = Circle('red', 90)
# print(circle.color)
# print(circle.radius)
# circle.add_radius(5)
# print(circle.radius)
  
