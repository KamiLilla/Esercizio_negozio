import os

'''
Implementazione funzione di trasferimento degli elementi registrati nel file di magazzino (.txt) all'interno del dizionario modificabile contenente tutti i prodotti in magazzino. 
    ARGOMENTI:
        file->'storehouse.txt'= file di testo contenente elementi in magazzino (aggiornato)
    return:
        storehouse= dizionario modificabile contenente tutti i prodotti presenti in magazzino 
'''

def get_items(file='storehouse.txt'):
    storehouse={}

    if os.path.getsize(file) == 0:
        print ('Magazzino vuoto!')
    
    else:
        with open (file,'r') as store:
            for line in store:
                product, quantity, purchase_price, sale_price = line.strip().split(';')
                storehouse[product.strip()] = {'quantità': int(quantity),'prezzo di acquisto': float(purchase_price),'prezzo di vendita': float(sale_price)}
    return storehouse
            

        
'''
Implementazione funzione di registrazione degli elementi del dizionario di magazzino all'interno del file di testo (storehouse.txt) riferito al magazzino stesso.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino 
        file->'storehouse.txt'= file di testo contenente elementi in magazzino (aggiornato)      
'''

def register_items(product_storage,file='storehouse.txt'):
    with open(file,'w+') as sales:
        for product, data in product_storage.items():
            line = f"{product};{data['quantità']};{data['prezzo di acquisto']};{data['prezzo di vendita']}\n"
            sales.write(line)
            

            
'''
Implementazione funzione di stampa dei prodotti presenti in magazzino.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino 
'''

def list_products(product_storage):
    print("%10s %10s %5s" % ('PRODOTTO','QUANTITA','PREZZO (in euro)'))
   
    for product, data in product_storage.items():        
        print(f'{product:10s}\t{data["quantità"]}\t{data["prezzo di vendita"]:.2f}')
    

    
    
'''
Implementazione funzione di eliminazione del prodotto dal magazzino (dizionario) in caso di esaurimento scorte.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino
        item= nome del prodotto da eliminare dal dizionario
'''
def delete_item(product_storage,item):
    if product_storage[item]['quantità']==0:
        del product_storage[item]
   
            
        
        