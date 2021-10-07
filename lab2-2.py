class Text:
    def __init__(self,text):
        self.text = text

    def countchar(self):
        return f'Chars {len(self.text)}'

    def countwords(self):
        count = 0 
        flag = 0
        for i in range(len(self.text)):
            if self.text[i] != ' ' and flag == 0:
                count += 1
                flag = 1
            else:
                if self.text[i] == ' ':
                    flag = 0
        return f'Words: {count}'

    def countsent(self):
        count = 0 
        flag = 0
        for i in range(len(self.text)):
            if self.text[i] != '.' and flag == 0:
                count += 1
                flag = 1
            else:
                if self.text[i] == '.':
                    flag = 0
        return f'Sentences: {count}'



f = open("text.txt", "r")
data =f.read()
f.close()

x = Text(data)

print(x.countwords())
print(x.countchar())
print(x.countsent())
