job = input('INFORME O JOB : ').upper().strip()


def busca():
    contador = 0 
    novo = open("LISTA_DE_JOBS.txt", 'w') 
    with open('COMPL03.txt', 'r') as data:
        
        linhas = data.readlines()

        for linha in linhas:
            
            if linha.find(job) != -1:
                contador += 1
                
                novo.writelines(linha)
                
            #print(F'Encontrado : {word} .')
            #print('Nº da Linha :', lines.index(line))
                

        print(f'Total de JOBS gravados : {contador}')
        novo.close()
        data.close()               
busca()        

def grava():
    data = busca()
    fp = open("LISTA_DE_JOBS.txt", 'w')
    for d in data[0]:   
        fp.writelines(d)
    print(f'Nova Lista Gravada com {data[1]} JOBS .')
    fp.close()

