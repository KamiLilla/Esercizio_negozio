from storehouse_admin import delete_item,list_products

'''
Implementazione funzione per acuisire in inptu il prodotto da vendere.
    return:
        item= nome del prodotto da vendere
        quantity= quantità da vendere
'''

def sell_item():
    item=input('Nome del prodotto: ')
    quantity=int(input('Quantità: '))
    return (item,quantity)


'''
Implementazione funzione di creazione del carrello di prodotti da vendere. Si acquisiscono in input i prodotti e qnt da vendere e se ne verifica la disponibiltà. Se sono disponibili si registra la vendita.
La funzione alla fine stampa una lista di prodotti venduti e il totale da pagare.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino

'''
def sale(product_storage):
    
    item,quantity=sell_item()
    
    check=check_availability(item,quantity,product_storage)
    if check is True:
        first_sale=add_sale(product_storage,item,quantity)
        first_choice=input('Aggiungere un altro prodotto? (si/no):')
        
        if first_choice=='no':
            total_first_sale=calculate_tot_sale(first_sale)
            
            print('VENDITA REGISTRATA:')
            print(first_sale[0])
            print(f'Totale:{total_first_sale:.2f}')
            first_sale.clear()
        
        else:
            other_choice=''
            while other_choice!= 'no':
                item,quantity=sell_item()
                check=check_availability(item,quantity,product_storage)
                if check is True:
                    sales_list=add_sale(product_storage,item, quantity)
                    other_choice=input('Aggiungere un altro prodotto? (si/no):') 
                else:
                    other_choice=input('Aggiungere un altro prodotto? (si/no):') 
                    
            if other_choice=='no': 
                total_sale=calculate_tot_sale(first_sale)
                print('VENDITA REGISTRATA:')
                for sale in sales_list:
                    print(sale)
                print(f'Totale: {total_sale:.2f}')
                sales_list.clear()
        
        
        
'''
Implementazione funzione di registrazione in file .txt (registro vendite) tutte le vendite effettuate.
    ARGOMENTI:
        product= nome del prodotto venduto
        qnt_sold= quanitità venduta
        price= prezzo da pagare
'''
        


def register_sale(product,qnt_sold,price):
    sale_registry={}
    total=qnt_sold*price
    
    sale_registry[product]={'prezzo':price,'quantità':qnt_sold,'totale':total}
    
    with open('total_sales_registry.txt','a') as sales:
        for product, data in sale_registry.items():
            line = f"{product}: {data['prezzo']} x {data['quantità']}= {data['totale']:.2f}\n"
            sales.write(line)
    

'''
Implementazione funzione di gestione della vendita. Crea una lista temporanea che corrisponde al carrello per gli acquisti e aggiorna di volta in volta la quantità dei prodotti in magazzino (dizionario) eliminandoli se necessario.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino
        item= nome del prodotto da vendere
        quantity= quantità del prodotto da vendere
        sale_list=[] -> lista vuota per creazione del carrello temporaneo
    return:
        sale_list= insieme dei prodotti e qnt da vendere selezionate dall'utente

'''
        
        
def add_sale(product_storage,item,quantity,sale_list=[]):
    
        product_storage[item]['quantità']-=quantity
            
        item_price=product_storage[item]['prezzo di vendita']
        
        register_sale(item,quantity,item_price)
        
        sale_string=f'{quantity}X{item}:{item_price}'
        sale_list.append(sale_string) 
        
        delete_item(product_storage,item)
           
        return sale_list


'''
Implementazione funzione di calcolo del totale venduto tra gli articoli nel carrello temporaneo.
    ARGOMENTI:
        sale_list= lista contente gli articoli selezionati dall'utente
    return:
        summ_sales= totale venduto calcolato tra gli articoli nel carrello 
'''
    
    
def calculate_tot_sale(sale_list):
    summ_sales=0
    for sale in sale_list:
        get_quantity= sale.split('X')
        quantity=int(get_quantity[0])
        get_sale_price=get_quantity[1].split(':')
        sale_price=float(get_sale_price[1])
        total_sale=quantity*sale_price
        summ_sales+=total_sale
    
    return summ_sales



'''
Implementazione funzione di verifica della presenza in magazzino degli articoli selezionati dall'utente.
    ARGOMENTI:
        item= nome del prodotto di cui verificare la presenza in magazzino
        quanitity= quanitità da vendere del prodotto selezionato (verificare la presenza)
        product_storage= izionario contenente tutti i prodotti presenti in magazzino
    return:
        True= booleano; il prodotto è presente in magazzino per la quanitità voluta
        False= boolenano; il prodotto non è presente
'''

def check_availability(item,quantity,product_storage):
    if item in product_storage and quantity<=product_storage[item]['quantità']:
        return True
    else:
        print('\nPRODOTTO INESISTENTE!\nI prodotti in magazzino sono i seguenti:\n')
        list_products(product_storage)
        return False

        
        
    
    
    