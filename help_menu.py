'''
Impementazione funzione per mostrare un menu di aiuto con tutti i comandi disponibili leggendoli dal file di testo 'commands.txt'.
'''

def help_commands():
    print('\nI comandi disponibili sono i seguenti:\n')
    with open('commands.txt') as commands_file:
        commands_file.seek(0)
        commands=commands_file.read()
        print(commands)