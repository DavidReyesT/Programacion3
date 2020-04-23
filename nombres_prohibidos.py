nchile = {
"Aquiles Brinco",
"Aquiles Baeza Parada",
"Armando Casas",
"Débora Melo",
"Elsa Pato",
"Elsa Pito",
"Elsa Podiondo",
"Elba Zurita",
"Luz Roja",
"Marcia Ana",
"Rosamel Fierro",
"Susana Orio",
"Zacaria Flores del Campo",
"Aquiles Castro",
"Keca Galindo",
"Elma Montt",
"Sole Dolio",
"Debora Cabezas Parada",
"Lucho Pay",
"Armando Mocha",
"Paloma Maria Parada",
"lma Marcela Goza de Alegria",
"Guillermo Nigote",
"Elvis Tek",
"Sevelinda Parada",
"Jose Luis Lamata Feliz",
"Aquiles Bailo",
"Alan Brito Delgado",
"Benito Camelo",
"Dolores del Ano",
"Elsa Capunta",
"Elmer Curio",
"Elba Lazo",
"Elsa Pallo",
"Mary Conazo",
"Mario Neta",
"Soila Cerda",
"Zampa Teste",
"Elsa Polindo",
"Pato Carlos Bustos de la Vaca",
"Jorge Nitales",
"Elva Gina",
"Esteban Dido",
"Elba Calao",
"Jose Lamata Feliz",
"Rosa Malcacho",
"Yola Prieto",
"Rosa Meza Cabeza",
"Elvio Lao",
"Elver Gallina Parada",
"Miren Amiano",
"Rosamel Forrito"
}

npanama = {
"Aquiles Brinco",
"Aquiles Baeza",
"Armando Casas",
"Debora Melo",
"Elsa Pato",
"Elsa Pito",
"Elba Zurita",
"Luz Rojas",
"Marcia Ana",
"Rosa Melbate",
"Susana Oria",
"Aquiles Castro",
"Keca Galindo",
"Elvis Tek",
"Alan Brito",
"Dolores Delano",
"Benito Camelo",
"Elmer Curio",
"Elba Lazo",
"Elsa Pallo",
"Mary Conazo",
"Mario Neta",
"Esteban Dido",
"Elva Gina",
"Elba Calao",
"Rosa Malcacho",
"Yola Prieto",
"Elvio Lao",
"Elver Galinda",
"Jorge Nitales"
}

todos_los_nombres = nchile | npanama  

nombre = input("BIENVENIDO. Por favor introdzca el nombre: ")
nombre = nombre.title()

if nombre in nchile:
    print("{} es un nombre PROHIBIDO".format(nombre))
else:
    print("{} NO es un nombre prohibido".format(nombre))




