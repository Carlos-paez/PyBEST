from datetime import datetime
for x in range (0,10):

    buscar=str(input("¿Desea buscar alguna creatura?\n"))
    if ("si" in buscar):
        lista=["El Silbon","La Sayona","El Griton","El Chivato","El Carreton","La Novia de la carretera","El Hachero","Las Brujas de Mérida", "Los Momoyes","Los Ceretones","Las Animas","Los Espantos de Carretera","El Chaure","La Serpiente de 7 cabezas","Los Canaimas","Los Chinamitos","El Carey","El Ganado fantasma","El Mapurangui","El Ahorcado"]
        print(lista)
        nombre=str(input("Ingrese el nombre de la creatura que desea buscar\n"))


        info={
            "Silbon":"El Silbón: No hay venezolano que no se paralice con su silbido maldito. Lo más siniestro de este espectro es que anuncia su presencia, pero igual no sirve de nada, porque si ya lo escuchaste –y peor aún, si crees que está muy lejos- estás condenado. Mide quizás unos tres metros y con sus piernas anormalmente largas anda en silenciosas zancadas entre el monte por la madrugada. Carga un fardo con los restos de quienes han muerto en sus manos. Su arma es un machete, que lo condenó a penar luego de matar a su padre. ¿Cómo silban los muertos sin boca?",
            "Sayona":"La Sayona: No se sabe si es una, o cientos. El mito que viene del siglo XIX habla de distintos tipos de mujeres que se aproximan a los hombres abusivos, cubiertas con un mantillo, y hablando de manera dulce y decorosa, para saltarles al cuello y dejarlos muertos en la cuneta. En Mérida es rubia y se llama La Dientona, y en Trujillo La Taconera. Tienen un código de justicia: no atentar contra las mujeres.",
            "Griton":"El Gritón: Si vas a bañarte a un pozo con tus amigos un día de semana sin mucha gente, y escuchas que una voz conocida grita tu nombre pero nadie ha movido sus labios, no respondas. El gritón es capaz de imitar la voz de cualquiera y de aprenderse sus nombres, para atraer a sus víctimas y desaparecerlas. La única descripción que se tiene de este espanto es que en su rostro no hay más que una descomunal boca de dientes podridos y lengua purulenta. Viste con saco y paja, y se camufla con el ambiente.",
            "Chivato":"Mitad hombre, mitad animal, persigue a los viajeros, asusta a los borrachos y acosa a las muchachas que caminan por la noche. Es uno de los mitos más antiguos y ha sido avistado en lugares donde se ha pactado con el maligno. Muchos dicen  haber visto al híbrido asolar Venezuela entre 2007 y 2009, en Ciudad Traki (Lecherías), La Cucaracha Racing Bar (Mérida), la avenida Concordia (Barquisimeto) y el dique de Guataparo (Valencia). Solo ha dejado rastro de pezuñas, sangre y humo. Lo asocian con un reguetón de Don Omar, porque en la prensa y en las redes lo han llamado El Señor de la Noche. ",
            "Carreton":"El Carretón: Su último avistamiento se reportó en redes sociales a finales del 2006 en Maracay. Es una enorme carreta cubierta por un halo amarillento y enfermo, que permea todo con un nauseabundo olor a cadáveres. Los más viejos dicen que esta carreta aparece a recoger los muertos cuando ha habido masacres, pero antes se usaba para cargar a los ahorcados luego de que se podrían por días bajo los árboles, pero sobre todo a las víctimas de las muchas epidemias que han caído en Venezuela, como de paludismo o cólera. Unos dicen que no va tirada por ningún animal y otros que al frente van dos caballos decapitados con las grupas zurcidas con alambre de púas.",
            "Novia":"La Novia de la carretera Caracas-La Guaira: Advertencia: no recojas ninguna mujer en la carretera vieja Caracas-La Guaira si pasas de noche. Si sientes una mirada en tu nuca desde el puesto de atrás y viajas solo, no mires por el retrovisor ya que el horror que encontrarás no te permitirá esquivar el camión que viene comiéndose el carril a toda velocidad. Algunos la han visto caminar con lentitud en su traje de novia por el borde de la carretera con los pies hacia adelante y el torso hacia atrás. No hace ruido, no llora, no habla: solo espera en su amargura que mueras en la carretera, como le ocurrió a ella el día de su boda.",
            "Hachero":"El Hachero: En los más profundos montes de Lara a veces se escucha el golpe de un hacha contra madera. Si el sonido se detiene en seco y se repite más débil a lo lejos como el quebrar de ramas es que ahí viene el hachero, listo para desmembrarte y alimentar a sus perros. Es un hombre descomunal, sin rostro, recubierto de musgo y de alimañas, blandiendo un hacha herrumbrada. El único modo de sobrevivir es no darle la espalda, pero ¿cómo no correr?",
            "Brujas":"Las Brujas de Mérida:Algo cae y camina sobre los techos luego de la hora del diablo. Son como pájaros gigantes que cazan incautos en los caminos. Mujeres emplumadas, de seis ojos, que en las pesadillas se sientan sobre pecho de su víctima y vierten brea de boca a boca. Los niños se pierden en los conucos, los campesinos no recuerdan cómo terminaron colgados de los árboles. No ayudes a mujeres parturientas cubiertas de polillas en los senderos. Cruza tijeras y haz círculos de sal alrededor de tu cama si escuchas pasos descalzos trotar alrededor de la casa.",
            "Momoyes":"Los Momoyes: Estos pequeños seres feéricos habitan cerca de las imperturbables lagunas de la cordillera trujillana. Son espíritus antiguos que protegen a la naturaleza. Van vestidos con ruanas de lana y anchos sombreros que los cubren del resplandor. Aunque tienen su propio lenguaje entienden idiomas humanos. Les gusta la fiesta y en San Juan suelen emborracharse cerca de las aldeas. Controlan los elementos y les gusta vengarse cuando te metes con ellos o perturbas las lagunas. Su último avistamiento fue en el 2013 cuando alguien en el páramo aseguró capturar uno y tenerlo en su casa. Las personas hicieron fila para verlo y un cura intercedió para que lo liberaran y se detuvieran los deslaves de esa semana, causados por los otros momoyes para que les devolvieran a su compañero. No se sabe qué pasó con él pero la noticia se reseñó en la radio y la prensa local. Hasta una banda de ska le hizo una canción, y grafittis de “liberen al duende” cubrieron la ciudad.",
            "Ceretones":"Los Ceretones: En Falcón, estos brujos se hacen invisibles o se transforman en pequeñas criaturas para acechar a las adolescentes. Dejan ofrendas en sus cuartos —un diente de leche, una estampita quemada, una moneda fundida— o hurgan en la basura de sus baños buscando rastros de sangre de menstruación, cabellos o uñas para usarlos en sus ritos. Al principio se limitan a observar a las niñas cuando duermen o a quitarles la ropa. Luego se aparecen en sus sueños como animales para abusar de ellas. Los padres no entienden porqué sus hijas empiezan a pasar varios días en su cuarto y no salen más. Al llamar a la puerta y forzar para abrirla, se dan cuenta que ni la muchacha ni el brujo están ahí.",
            "Animas":"En 1912, un año entero sin lluvia provocó una hambruna en Paraguaná que obligó a miles de personas a cruzar el istmo hasta Coro. En cuestión de días el desierto se llenó de cadáveres y el cielo de zamuros. No se sabe cuántas personas murieron ese año, pero a veces larga procesión de almas se ve caminar con sus fardos, sus bestias de carga y sus niños  entre los cujíes y los médanos. Sus huesos sin tumba están dispersos bajo la arena. Una pequeña capilla se irguió para conmemorar a las víctimas, que según los lugareños conceden milagros.",
            "Carretera":"Autobuses fantasma, carros envueltos en llamas azules, accidentes que resultan ser espejismos y viajantes que se desvanecen como briznas de polvo suelen ser vistos en todas las carreteras que llevan al Zulia, donde ha habido tantos terribles accidentes por culpa de choferes que se duermen al volante o que conducen ebrios. Son automóviles que aparecen y desaparecen luego de ser sobrepasados, luces que vienen de frente pero al final no hay nada, destellos en los túneles y tenebrosos pasajeros esperando en las paradas abandonadas, como advertencias de lo descuidadas y peligrosas que son las carreteras del país.",
            "Chaure":"De mal agüero en casi toda la costa venezolana, esta ave es muy bonita pero bastante inquietante por sus hábitos nocturnos. Según los más viejos presagia la muerte, el dolor o un parto. Su ulular se espanta con insultos. Si te sigue un chaure por la playa quizás no veas el día siguiente.",
            "Serpiente":"Cuenta la leyenda que bajo la Piedra del Medio, en el Orinoco, habita una serpiente de siete cabezas, cada una bajo distintos lugares de la vieja Ciudad Bolívar: si el monstruo se sacude, la ciudad se hundiría en el río. A comienzos del siglo XX algunos atribuían los naufragios del Orinoco a la gran serpiente. Fue avistada por última vez en 1985, cuando gente del puerto dijo haberla visto causar grandes olas en el río",
            "Canaimas":"Los niños pemones no salen a jugar cuando cae el sol, mucho menos cerca de un río, porque ciertas criaturas anfibias, de ojos enormes y manos ágiles y palmeadas, cazan en grupo, silbando para avisar a sus pares la ubicación de la presa. Arrastran todo lo que atrapan hasta el agua y allí lo devoran sin siquiera perturbar la superficie.",
            "Chinamitos":"Son niños de sombra que confunden a las personas, roban objetos de valor y asustan a los más pequeños proyectando sus siluetas. Sus risas juguetonas son un eco en las noches costeñas y sus ojos vacíos observan a los caminantes desde los árboles. Algunos habitan casas abandonadas",
            "Carey":"Esta monstruosa tortuga de mar hunde a los peñeros y los aleja de la costa, cuando los pescadores se obsesionan con atraparla al ver los destellos de su caparazón en la madrugada. Pero quienes la han capturado cuentan que, una vez en el bote, relamiéndose por la captura, se han percatado de que en su abdomen acorazado se siente el relieve de un rostro humano, como si tuviese un hombre atrapado dentro de su concha. Algunos dicen haber escuchado una voz llamarlos desde el interior del animal. Otros dicen que al devolverla horrorizados al agua, la carey gigante comenzó a destrozar la lancha. Otras leyendas dicen que quien la mata se convierte en tortuga.",
            "Ganado":"Por la recta de El Tigre a veces se mete el ganado que tiene el diablo, que hace que los carros se retrasen o pierdan el camino. Esas reses no mugen, sus cascos no se sienten, y si un conductor las rebasa, al mirar por el retrovisor ya no se ven. Si llegas a verlos a los ojos, verás que esos animales son ciegos: una película blanca y pastosa cubre sus retinas",
            "Mapurangui":"Este monstruo lo compartimos con Brasil. Se trata de una enorme y pesada bestia peluda que vive en lo profundo de la selva. La criptozoología especula que pueden ser megaterios que sobrevivieron a la extinción. Los indígenas lo respetan y veneran, y no permiten que nadie los cace",
            "Ahorcado":"Entre los árboles de cacao se ve una silueta en cuclillas, acechando cuando la luna está alta. El olor a carne pudriéndose alrededor es penetrante. Sientes que no te quitan la vista de encima y cuando se te olvidan las oraciones y piensas en correr, escuchas el restallar de una cuerda templándose desde una rama y el peso de un cuerpo cayendo, reventándose las vértebras del cuello y la tráquea. Con un nudo alrededor de la garganta cae enfrente de ti, y con horror ves que eres tú mismo sin vida, con los ojos reventados y la sangre brotando de tu boca. El ahorcado es un espanto que te enfrenta a tu propia muerte."
        }
        if ("Silbon" in nombre.title()):
            print(info.get ('Silbon'))
        elif ("Sayona" in nombre.title()):
            print(info.get ('Sayona'))
            """img.show()"""
        elif ("Griton" in nombre.title()):
            print(info.get ('Griton'))
        elif ("Chivato" in nombre.title()):
            print(info.get ('Chivato'))
        elif("Carreton" in nombre.title()):
            print(info.get ('Carreton'))
        elif ("Novia" in nombre.title()):
            print(info.get ('Novia'))
        elif ("Hachero" in nombre.title()):
            print(info.get ('Hachero'))
        elif ("Brujas" in nombre.title()):
            print(info.get ('Brujas'))
        elif ("Momoyes" in nombre.title()):
            print(info.get ('Momoyes'))
        elif ("Ceretones" in nombre.title()):
            print(info.get ('Ceretones'))
        elif ("Animas" in nombre.title()):
            print(info.get ('Animas'))
        elif ("Encantos" in nombre.title() or "Carretera" in nombre.title()):
            print(info.get('Carretera'))
        elif ("Chaure" in nombre.title()):
            print(info.get('Chaure'))
        elif ("Serpiente" in nombre.title()):
            print(info.get('Serpiente'))
        elif ("Canaimas" in nombre.title()):
            print(info.get('Canaimas'))
        elif ("Chinamitos" in nombre.title()):
            print(info.get('Chinamitos'))
        elif ("Carey" in nombre.title()):
            print(info.get('Carey'))
        elif ("Ganado" in nombre.title() or "Fantasma" in nombre.title()):
            print(info.get('Ganado'))
        elif ("Mapurangui" in nombre.title()):
            print(info.get('Mapurangui'))
        elif ("Ahorcado" in nombre.title()):
            print(info.get('Ahorcado'))

    else:
        print("Los unicos monstruos son los que la mente crea por aquello que ignora")
print("gracias por usar my Bestiario ATT: Caros Páez")

from datetime import datetime
"""from PIL import Image
img = image.open('')"""
print(datetime.now())
for x in range (0,10):

    buscar=str(input("¿Desea buscar alguna creatura?\n"))
    if ("si" in buscar):
        lista=["El Silbon","La Sayona","El Griton","El Chivato","El Carreton","La Novia de la carretera","El Hachero","Las Brujas de Mérida", "Los Momoyes","Los Ceretones","Las Animas","Los Espantos de Carretera","El Chaure","La Serpiente de 7 cabezas","Los Canaimas","Los Chinamitos","El Carey","El Ganado fantasma","El Mapurangui","El Ahorcado"]
        print(lista)
        nombre=str(input("Ingrese el nombre de la creatura que desea buscar\n"))


        info={
            "Silbon":"El Silbón: No hay venezolano que no se paralice con su silbido maldito. Lo más siniestro de este espectro es que anuncia su presencia, pero igual no sirve de nada, porque si ya lo escuchaste –y peor aún, si crees que está muy lejos- estás condenado. Mide quizás unos tres metros y con sus piernas anormalmente largas anda en silenciosas zancadas entre el monte por la madrugada. Carga un fardo con los restos de quienes han muerto en sus manos. Su arma es un machete, que lo condenó a penar luego de matar a su padre. ¿Cómo silban los muertos sin boca?",
            "Sayona":"La Sayona: No se sabe si es una, o cientos. El mito que viene del siglo XIX habla de distintos tipos de mujeres que se aproximan a los hombres abusivos, cubiertas con un mantillo, y hablando de manera dulce y decorosa, para saltarles al cuello y dejarlos muertos en la cuneta. En Mérida es rubia y se llama La Dientona, y en Trujillo La Taconera. Tienen un código de justicia: no atentar contra las mujeres.",
            "Griton":"El Gritón: Si vas a bañarte a un pozo con tus amigos un día de semana sin mucha gente, y escuchas que una voz conocida grita tu nombre pero nadie ha movido sus labios, no respondas. El gritón es capaz de imitar la voz de cualquiera y de aprenderse sus nombres, para atraer a sus víctimas y desaparecerlas. La única descripción que se tiene de este espanto es que en su rostro no hay más que una descomunal boca de dientes podridos y lengua purulenta. Viste con saco y paja, y se camufla con el ambiente.",
            "Chivato":"Mitad hombre, mitad animal, persigue a los viajeros, asusta a los borrachos y acosa a las muchachas que caminan por la noche. Es uno de los mitos más antiguos y ha sido avistado en lugares donde se ha pactado con el maligno. Muchos dicen  haber visto al híbrido asolar Venezuela entre 2007 y 2009, en Ciudad Traki (Lecherías), La Cucaracha Racing Bar (Mérida), la avenida Concordia (Barquisimeto) y el dique de Guataparo (Valencia). Solo ha dejado rastro de pezuñas, sangre y humo. Lo asocian con un reguetón de Don Omar, porque en la prensa y en las redes lo han llamado El Señor de la Noche. ",
            "Carreton":"El Carretón: Su último avistamiento se reportó en redes sociales a finales del 2006 en Maracay. Es una enorme carreta cubierta por un halo amarillento y enfermo, que permea todo con un nauseabundo olor a cadáveres. Los más viejos dicen que esta carreta aparece a recoger los muertos cuando ha habido masacres, pero antes se usaba para cargar a los ahorcados luego de que se podrían por días bajo los árboles, pero sobre todo a las víctimas de las muchas epidemias que han caído en Venezuela, como de paludismo o cólera. Unos dicen que no va tirada por ningún animal y otros que al frente van dos caballos decapitados con las grupas zurcidas con alambre de púas.",
            "Novia":"La Novia de la carretera Caracas-La Guaira: Advertencia: no recojas ninguna mujer en la carretera vieja Caracas-La Guaira si pasas de noche. Si sientes una mirada en tu nuca desde el puesto de atrás y viajas solo, no mires por el retrovisor ya que el horror que encontrarás no te permitirá esquivar el camión que viene comiéndose el carril a toda velocidad. Algunos la han visto caminar con lentitud en su traje de novia por el borde de la carretera con los pies hacia adelante y el torso hacia atrás. No hace ruido, no llora, no habla: solo espera en su amargura que mueras en la carretera, como le ocurrió a ella el día de su boda.",
            "Hachero":"El Hachero: En los más profundos montes de Lara a veces se escucha el golpe de un hacha contra madera. Si el sonido se detiene en seco y se repite más débil a lo lejos como el quebrar de ramas es que ahí viene el hachero, listo para desmembrarte y alimentar a sus perros. Es un hombre descomunal, sin rostro, recubierto de musgo y de alimañas, blandiendo un hacha herrumbrada. El único modo de sobrevivir es no darle la espalda, pero ¿cómo no correr?",
            "Brujas":"Las Brujas de Mérida:Algo cae y camina sobre los techos luego de la hora del diablo. Son como pájaros gigantes que cazan incautos en los caminos. Mujeres emplumadas, de seis ojos, que en las pesadillas se sientan sobre pecho de su víctima y vierten brea de boca a boca. Los niños se pierden en los conucos, los campesinos no recuerdan cómo terminaron colgados de los árboles. No ayudes a mujeres parturientas cubiertas de polillas en los senderos. Cruza tijeras y haz círculos de sal alrededor de tu cama si escuchas pasos descalzos trotar alrededor de la casa.",
            "Momoyes":"Los Momoyes: Estos pequeños seres feéricos habitan cerca de las imperturbables lagunas de la cordillera trujillana. Son espíritus antiguos que protegen a la naturaleza. Van vestidos con ruanas de lana y anchos sombreros que los cubren del resplandor. Aunque tienen su propio lenguaje entienden idiomas humanos. Les gusta la fiesta y en San Juan suelen emborracharse cerca de las aldeas. Controlan los elementos y les gusta vengarse cuando te metes con ellos o perturbas las lagunas. Su último avistamiento fue en el 2013 cuando alguien en el páramo aseguró capturar uno y tenerlo en su casa. Las personas hicieron fila para verlo y un cura intercedió para que lo liberaran y se detuvieran los deslaves de esa semana, causados por los otros momoyes para que les devolvieran a su compañero. No se sabe qué pasó con él pero la noticia se reseñó en la radio y la prensa local. Hasta una banda de ska le hizo una canción, y grafittis de “liberen al duende” cubrieron la ciudad.",
            "Ceretones":"Los Ceretones: En Falcón, estos brujos se hacen invisibles o se transforman en pequeñas criaturas para acechar a las adolescentes. Dejan ofrendas en sus cuartos —un diente de leche, una estampita quemada, una moneda fundida— o hurgan en la basura de sus baños buscando rastros de sangre de menstruación, cabellos o uñas para usarlos en sus ritos. Al principio se limitan a observar a las niñas cuando duermen o a quitarles la ropa. Luego se aparecen en sus sueños como animales para abusar de ellas. Los padres no entienden porqué sus hijas empiezan a pasar varios días en su cuarto y no salen más. Al llamar a la puerta y forzar para abrirla, se dan cuenta que ni la muchacha ni el brujo están ahí.",
            "Animas":"En 1912, un año entero sin lluvia provocó una hambruna en Paraguaná que obligó a miles de personas a cruzar el istmo hasta Coro. En cuestión de días el desierto se llenó de cadáveres y el cielo de zamuros. No se sabe cuántas personas murieron ese año, pero a veces larga procesión de almas se ve caminar con sus fardos, sus bestias de carga y sus niños  entre los cujíes y los médanos. Sus huesos sin tumba están dispersos bajo la arena. Una pequeña capilla se irguió para conmemorar a las víctimas, que según los lugareños conceden milagros.",
            "Carretera":"Autobuses fantasma, carros envueltos en llamas azules, accidentes que resultan ser espejismos y viajantes que se desvanecen como briznas de polvo suelen ser vistos en todas las carreteras que llevan al Zulia, donde ha habido tantos terribles accidentes por culpa de choferes que se duermen al volante o que conducen ebrios. Son automóviles que aparecen y desaparecen luego de ser sobrepasados, luces que vienen de frente pero al final no hay nada, destellos en los túneles y tenebrosos pasajeros esperando en las paradas abandonadas, como advertencias de lo descuidadas y peligrosas que son las carreteras del país.",
            "Chaure":"De mal agüero en casi toda la costa venezolana, esta ave es muy bonita pero bastante inquietante por sus hábitos nocturnos. Según los más viejos presagia la muerte, el dolor o un parto. Su ulular se espanta con insultos. Si te sigue un chaure por la playa quizás no veas el día siguiente.",
            "Serpiente":"Cuenta la leyenda que bajo la Piedra del Medio, en el Orinoco, habita una serpiente de siete cabezas, cada una bajo distintos lugares de la vieja Ciudad Bolívar: si el monstruo se sacude, la ciudad se hundiría en el río. A comienzos del siglo XX algunos atribuían los naufragios del Orinoco a la gran serpiente. Fue avistada por última vez en 1985, cuando gente del puerto dijo haberla visto causar grandes olas en el río",
            "Canaimas":"Los niños pemones no salen a jugar cuando cae el sol, mucho menos cerca de un río, porque ciertas criaturas anfibias, de ojos enormes y manos ágiles y palmeadas, cazan en grupo, silbando para avisar a sus pares la ubicación de la presa. Arrastran todo lo que atrapan hasta el agua y allí lo devoran sin siquiera perturbar la superficie.",
            "Chinamitos":"Son niños de sombra que confunden a las personas, roban objetos de valor y asustan a los más pequeños proyectando sus siluetas. Sus risas juguetonas son un eco en las noches costeñas y sus ojos vacíos observan a los caminantes desde los árboles. Algunos habitan casas abandonadas",
            "Carey":"Esta monstruosa tortuga de mar hunde a los peñeros y los aleja de la costa, cuando los pescadores se obsesionan con atraparla al ver los destellos de su caparazón en la madrugada. Pero quienes la han capturado cuentan que, una vez en el bote, relamiéndose por la captura, se han percatado de que en su abdomen acorazado se siente el relieve de un rostro humano, como si tuviese un hombre atrapado dentro de su concha. Algunos dicen haber escuchado una voz llamarlos desde el interior del animal. Otros dicen que al devolverla horrorizados al agua, la carey gigante comenzó a destrozar la lancha. Otras leyendas dicen que quien la mata se convierte en tortuga.",
            "Ganado":"Por la recta de El Tigre a veces se mete el ganado que tiene el diablo, que hace que los carros se retrasen o pierdan el camino. Esas reses no mugen, sus cascos no se sienten, y si un conductor las rebasa, al mirar por el retrovisor ya no se ven. Si llegas a verlos a los ojos, verás que esos animales son ciegos: una película blanca y pastosa cubre sus retinas",
            "Mapurangui":"Este monstruo lo compartimos con Brasil. Se trata de una enorme y pesada bestia peluda que vive en lo profundo de la selva. La criptozoología especula que pueden ser megaterios que sobrevivieron a la extinción. Los indígenas lo respetan y veneran, y no permiten que nadie los cace",
            "Ahorcado":"Entre los árboles de cacao se ve una silueta en cuclillas, acechando cuando la luna está alta. El olor a carne pudriéndose alrededor es penetrante. Sientes que no te quitan la vista de encima y cuando se te olvidan las oraciones y piensas en correr, escuchas el restallar de una cuerda templándose desde una rama y el peso de un cuerpo cayendo, reventándose las vértebras del cuello y la tráquea. Con un nudo alrededor de la garganta cae enfrente de ti, y con horror ves que eres tú mismo sin vida, con los ojos reventados y la sangre brotando de tu boca. El ahorcado es un espanto que te enfrenta a tu propia muerte."
        }
        if ("Silbon" in nombre.title()):
            print(info.get ('Silbon'))
        elif ("Sayona" in nombre.title()):
            print(info.get ('Sayona'))
            """img.show()"""
        elif ("Griton" in nombre.title()):
            print(info.get ('Griton'))
        elif ("Chivato" in nombre.title()):
            print(info.get ('Chivato'))
        elif("Carreton" in nombre.title()):
            print(info.get ('Carreton'))
        elif ("Novia" in nombre.title()):
            print(info.get ('Novia'))
        elif ("Hachero" in nombre.title()):
            print(info.get ('Hachero'))
        elif ("Brujas" in nombre.title()):
            print(info.get ('Brujas'))
        elif ("Momoyes" in nombre.title()):
            print(info.get ('Momoyes'))
        elif ("Ceretones" in nombre.title()):
            print(info.get ('Ceretones'))
        elif ("Animas" in nombre.title()):
            print(info.get ('Animas'))
        elif ("Encantos" in nombre.title() or "Carretera" in nombre.title()):
            print(info.get('Carretera'))
        elif ("Chaure" in nombre.title()):
            print(info.get('Chaure'))
        elif ("Serpiente" in nombre.title()):
            print(info.get('Serpiente'))
        elif ("Canaimas" in nombre.title()):
            print(info.get('Canaimas'))
        elif ("Chinamitos" in nombre.title()):
            print(info.get('Chinamitos'))
        elif ("Carey" in nombre.title()):
            print(info.get('Carey'))
        elif ("Ganado" in nombre.title() or "Fantasma" in nombre.title()):
            print(info.get('Ganado'))
        elif ("Mapurangui" in nombre.title()):
            print(info.get('Mapurangui'))
        elif ("Ahorcado" in nombre.title()):
            print(info.get('Ahorcado'))

    else:
        print("Los unicos monstruos son los que la mente crea por aquello que ignora")
print("gracias por usar my Bestiario ATT: Carlos Páez")