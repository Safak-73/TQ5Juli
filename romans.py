def to_roman(n):

    if n<1 or n>3999:
        print('Ungueltige Eingabe. Die grenzen sind 1<n<3999.')
        return

    zeichen_mapping = {
            1000 : 'M',
            500 : 'D',
            100 : 'C',
            50 : 'L',
            10 : 'X',
            5 : 'V',
            1 : 'I'
    }
    
    print(f"Deine Zahl als Roemische Zahl {n} = ", end='')
    resultat = ''
    for key in zeichen_mapping.keys():
        while n >= key:
            resultat += zeichen_mapping[key]
            n -= key

    print(resultat)
    return resultat