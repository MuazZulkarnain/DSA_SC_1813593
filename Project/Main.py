from cursor import Cursor

class Buffer:
    def __init__(self):
        self.List = Cursor()
        self.FileName = None  # Current file
        self.i = -1  # Char pointer

    def __ConvertChars(self, line):
        chars_lst = []
        for char in line:
            chars_lst.append(char)
        return chars_lst

    def SetFileName(self, filename):
        self.FileName = filename

    def GetLineSize(self):
        return len(self.List.getCurrent())

    def GetCurrentLine(self):
        if not self.IsEmpty():
            line = ''.join(self.List.getCurrent())
            return line
        return 'File is Empty!'

    def GetCurrentChar(self):
        if not self.GetLineSize() == 0:
            return self.GetCurrentLine()[self.i]
        return 'File is Empty!'

    def EditFile(self, filename):
        self.__init__()
        self.SetFileName(filename)

        lines_lst = []
        try:
            with open(self.FileName, 'r') as f:
                lines_lst = f.readlines()

        except FileNotFoundError:
            return -1

        if len(lines_lst) > 0:
            for line in lines_lst:
                self.InsertLine(line)
        return 0

    def CreateNewFile(self, filename):
        with open(filename, 'w') as f: pass
        self.EditFile(filename)

    def InsertLine(self, line):
        chars = self.__ConvertChars(line + '\n')
        self.List.insertAfter(chars)

    def InsertChar(self, char):
        if self.IsEmpty():
            self.List.insertAfter([char])
            self.i += 1
        else:
            self.List.getCurrent().insert(self.i + 1, char)
            self.i += 1

    def MoveUp(self):
        if self.List.hasPrevious():
            self.List.previous()
        else:
            print('There is no line above!')

    def MoveDown(self):
        if self.List.hasNext():
            self.List.next()
        else:
            print('That\'s the end of file!')

    def MoveRight(self):
        if not self.IsEmpty() and self.GetLineSize() != 0:
            if self.i == -1 or self.i == 0:
                self.MoveDown()
                self.i = 0
            else:
                self.i += 1
        else:
            print('List/Line is empty!')

    def MoveLeft(self):
        if not self.IsEmpty() and self.GetLineSize() != 0:
            if self.i == (0 - self.GetLineSize()):
                self.MoveUp()
                self.i = -1
            else:
                self.i -= 1
        else:
            print('List/Line is empty!')

    def DeleteLine(self):
        if not self.IsEmpty():
            return self.List.remove()
        print('List is empty!')

    def DeleteChar(self):
        if not self.IsEmpty() and self.GetCurrentLine() != 0:
            return self.List.getCurrent().remove(self.i)
        print('List/Line is empty!')

    def ReplaceLine(self, newLine):
        if not self.IsEmpty():
            self.List.getCurrent().setData(newLine)
            return
        print('List is empty!')

    def ReplaceChar(self, newchar):
        if not self.IsEmpty() and self.GetCurrentLine() !=0:
            self.List.getCurrent()[self.i] = newchar
            return self.List
        print('List/Line is empty!')

    def ClearFile(self):
        self.CreateNewFile(self.FileName)

    def SaveFile(self):
        with open(self.FileName, 'w+') as f:
            if not self.IsEmpty():
                for line in self.List:
                    f.write(''.join(line))
        print('File Save Successfully!')

    def IsEmpty(self):
        return self.List.isEmpty()

    def __len__(self):
        return len(self.List)

    def __str__(self):
        if self.IsEmpty():
            return 'File is empty!'
        lines = ''
        for line in self.List:
            lines += ''.join(line)
        return lines
