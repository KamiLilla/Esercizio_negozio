'''
Implementazione funzione per creare e scrivere su file di tipo .txt i costi sostenuti.
    ARGOMENTI:
        product= nome del prodotto
        qnt_added= quanitità acquistata dal negozio
        cost= costo di acquisto del prodotto
'''


def register_cost(product,qnt_added,cost):
    sale_registry={}
    total=qnt_added*cost
    
    sale_registry[product]={'costo':cost,'quantità':qnt_added,'totale':total}
    
    with open('total_costs_registry.txt','a') as costs:
        for product, data in sale_registry.items():
            line = f"{product}: {data['costo']} x {data['quantità']}= {data['totale']:.2f}\n"
            costs.write(line)


            
'''
Implementazione funzione di calcolo del totale dei costi sostenuti. Il calcolo avviene aprendo in sola lettura il registro (.txt) dei costi di acquisto di ogni prodotto in magazzino e sommandoli.
    ARGOMENTI:
        product_storage= dizionario contenente tutti i prodotti presenti in magazzino
    return:
        total_costs= costi totali sostenuti
'''
def total_costs(product_storage):
    total_costs=0
    with open ('total_costs_registry.txt','r') as costs:
        for cost in (costs.readlines()):
            get_total=cost.split('=')
            get_total=get_total[1].split('\n')
            item_cost=float(get_total[0])
            total_costs+=item_cost
   
    return total_costs