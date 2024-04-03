from sales_admin import*
from commands_verifier import verify_command
from costs_admin import register_cost


'''
Implementazione classe per la creazione di oggeti di tipo 'Product'. I prodotti li aggiunge l'utente in input grazie alle funzioni 'new_product' e 'add'.

'''
class Product:
   
    def __init__(self,name,qnt,sale_price,cost):
        self.name=name
        self.quantity=qnt
        self.sale_price=sale_price
        self.cost=cost
    
    
    '''
    Aggiunge il prodotto acquisito da input utente all'interno del dizionario contente tutti i prodotti in negozio (magazzino)
        ARGOMENTI:
            product_storage= dizionario contenente tutti i prodotti presenti in magazzino
    '''

    
    def add(self,product_storage):
        if self.name not in product_storage:
            product_storage[self.name]= {'quantità':self.quantity,'prezzo di vendita':self.sale_price,'prezzo di acquisto':self.cost}
        
        else:
            product_storage[self.name]['quantità']+=self.quantity
        
        print( f'AGGIUNTO: {self.quantity} X {self.name}')
       
    
'''
Funzione che permette di acquisite da input utente un prodotto acquistato dal negozio e creare un oggetto di tipo Product. Si registra subito il costo del prodotto all'interno del file 'total_costs_registry.txt'.
    return:
        Product= oggetto appartenente alla classe Product
'''
            
def new_product():
    name=input('Nome del prodotto: ')
    quantity=int(input('Quantità: '))
    cost=float(input('Prezzo di acquisto: '))
    sale_price=float(input('Prezzo di vendita: '))
   
    register_cost(name,quantity,cost)
        
    return Product(name,quantity,sale_price,cost)



        
        
        
   
            
    

        