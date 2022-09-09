#4A
n = 2
cout = "YES" if ((n%2) == 0) else "NO"
#print (cout)

#71A - Way Too Long Words
def trata_palavras(n):
    if not n.isalpha():
        return ""
        
    if len(n) <= 10:
        return n
    
    primeira_letra = n[:1]
    ultima_letra = n[-1:]
    
    return primeira_letra + str(len(n)-2) + ultima_letra

def loop_input():
    continua = True
    while continua:
        try:
            n = input()
            resultado = trata_palavras(n)
            if resultado:
                print(resultado)
            loop_input()
        except:
            continua = False

loop_input()            


#print (trata_palavras('word') == 'word')
#print (trata_palavras('localization') == 'l10n')
#print (trata_palavras('pneumonoultramicroscopicsilicovolcanoconiosis') == 'p43s')
    
