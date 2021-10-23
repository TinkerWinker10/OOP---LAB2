class Text:
    def __init__(self,file_name):
        self.file = file_name

    def count_words(self):
        """
        Method which count ammount of chars in file
        This function open file, if it exists, otherwise raise FileNotFoundError and exit
        After that, in for line cycle count ammount of chars in file, incrementing counter. After, close file
        and return counter
        
        """
        count = 0
        try: 
            data = open(self.file, 'r')
        except FileNotFoundError:
            raise 
        for line in data: 
            count +=len(line.split())
        data.close()
        return count

    def count_char(self):
        """
        Method which count ammount of words in file
        This function open file, if it exists, otherwise raise FileNotFoundError and exit
        After that, in for line cycle count ammount of words in file incrementing the counter. After, close file
        and return counter
        
        """
        count = 0 
        try: 
            data = open(self.file, 'r')
        except FileNotFoundError:
            pass
        for line in data: 
            count +=len(line)
        data.close()
        return count

    def count_sentence(self):
        """
        Method which count ammount of chars in file
        This function open file, if it exists, otherwise raise FileNotFoundError and exit
        After that, in for line cycle read file and increment counter when stop signs 
        occurs
        """
        count = 0
        sign = ('.','?','!','.\n', '...')
        try: 
            data = open(self.file, 'r')
        except FileNotFoundError:
            pass
        for line in data: 
            for i in sign:
                count +=line.count(i)   
        data.close()
        return count
        


if __name__ == '__main__':
    x = Text("text.txt")
    print(f'Chars: {x.count_char()} \nWords: {x.count_words()} \nSentence: {x.count_sentence()}')
    




