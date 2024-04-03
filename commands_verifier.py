from help_menu import help_commands

'''
Implementazione funzione di verifica dei comandi inseriti dall'utente.
    ARGOMENTI:
        command= input dell'utente
        command_list= lista di comandi acccettati
    return:
        help_commands()-> stampa la legenda dei comandi disponibili in caso di inserimento errato
            
'''



def verify_command(command,commands_list=['aggiungi','elenca','vendita','profitti','aiuto','chiudi']
):
    if command not in commands_list:
        print('Comando non valito')
        return help_commands()
    else:
        return True
    
    