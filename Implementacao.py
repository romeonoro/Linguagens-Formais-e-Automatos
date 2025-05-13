def afd_termina_com_101(palavra):
    estado = 'q0'
    
    for simbolo in palavra:
        if estado == 'q0':
            if simbolo == '0':
                estado = 'q0'
            elif simbolo == '1':
                estado = 'q1'
        elif estado == 'q1':
            if simbolo == '0':
                estado = 'q2'
            elif simbolo == '1':
                estado = 'q1'
        elif estado == 'q2':
            if simbolo == '0':
                estado = 'q0'
            elif simbolo == '1':
                estado = 'q3'
        elif estado == 'q3':
            if simbolo == '0':
                estado = 'q2'
            elif simbolo == '1':
                estado = 'q1'
    
    return estado == 'q3'


# Testes
palavras = ['101', '1101', '000101', '1010', '111', '10', '1']
for w in palavras:
    resultado = afd_termina_com_101(w)
    print(f'{w}: {"Aceita" if resultado else "Rejeita"}')
