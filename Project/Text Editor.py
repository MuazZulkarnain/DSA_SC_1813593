from Text_Editor_Main import Buffer

def Option(editor):
    while True:
        print('\n===============================================================')
        print('Please choose what you want to do:')
        print('1: Insert New Line.')
        print('2: Insert new character.')
        print('3: Move Cursor Up.')
        print('4: Move Cursor Down.')
        print('5: Move Cursor Right.')
        print('6: Move Cursor Left.')
        print('7: Replace Current Line.')
        print('8: Replace Current Character')
        print('9: Delete Current Line.')
        print('10: Delete Current Character.')
        print('11: Display all.')
        print('12: Clear File.')
        print('13: Save File.')
        print('14: Exit.\n')

        if not editor.IsEmpty():
            print(f'''\nCurrent Line: {editor.GetCurrentLine()}Cursor at: {editor.GetCurrentChar()}\n''')

        option = input()
        try:
            int(option)
        except ValueError:
            print('Please enter option in number:\n')
            continue
        else:
            option = int(option)

        if option == 1:
            print('\nEnter the line you want to insert:')
            line = input()
            editor.InsertLine(line)
        elif option == 2:
            print('\nEnter the character you want to insert:')
            char = input()
            editor.InsertChar(char)
        elif option == 3:
            editor.MoveUp()
        elif option == 4:
            editor.MoveDown()
        elif option == 5:
            editor.MoveRight()
        elif option == 6:
            editor.MoveLeft()
        elif option == 7:
            print('Enter the new line:')
            line = input()
            editor.ReplaceLine(line)
        elif option == 8:
            print('Enter the new character:')
            char = input()
            editor.ReplaceChar(char)
        elif option == 9:
            editor.DeleteLine()
        elif option == 10:
            editor.DeleteChar()
        elif option == 11:
            print(editor)
        elif option == 12:
            editor.ClearFile()
        elif option == 13:
            editor.SaveFile()
        elif option == 14:
            break
        # elif option == 15:
        #     break
        else:
            print('Invalid option!')


def TextEditor():
    editor = Buffer()
    print('\n===============================================================')
    print('\t\tWelcome To My Text Editor')
    print('===============================================================\n')
    while True:
        print('Please choose what you want to do:')
        print('1: Create a new file.')
        print('2: Edit a file.')
        print('3: Exit.\n')

        response = input()

        try:
            int(response)
        except ValueError:
            print('\nPlease enter option in number.')
            continue
        else:
            response = int(response)

        if response == 1:
            print('\nPlease Enter the file name you want to create:')
            FileName = input()
            editor.CreateNewFile(FileName)
            print('\nNewFile Created!\n')

            Option(editor)

        elif response == 2:
            print('\nPlease Enter the file name you want to edit:')
            FileName = input()
            exitStatus = editor.EditFile(FileName)
            if exitStatus == -1:
                print(f'{FileName} file does not exits in directory!')
                continue

            Option(editor)

        elif response == 3:
            break

        else:
            print('Invalid option!')
    print('Thank You!')

TextEditor()