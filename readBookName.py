import os

class BookNameContainer:
    
    def __init__(self):
        self.mBookContainer = []
        self.currentIndex = self.readBookNames()

    def readBookNames(self):
        with open(os.path.dirname(__file__) + "\\book_items.csv", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
               self.mBookContainer.append(line.strip())
            return int(self.mBookContainer[0])

    def getNextBookName(self):
        if(len(self.mBookContainer) - 1 > self.currentIndex):
            bookName = self.mBookContainer[self.currentIndex]
            if self.currentIndex > 1:
                self.saveHnadledBookIndex(self.currentIndex)
            self.currentIndex =  self.currentIndex + 1
            return bookName
        return "null"
    
    def saveHnadledBookIndex(self, index):
       self.mBookContainer[0] = str(index)
       with open("book_items.csv","w", encoding="utf-8") as f:
            for line in self.mBookContainer:
                f.write(line + "\n")
            f.close()