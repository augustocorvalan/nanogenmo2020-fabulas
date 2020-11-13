def get_rules():
    return {
        "origin": [
          "#title#"
        ],
        "seed0": ["los chicos aprenden de #electronico#."],
        "seed1": ["los chicos aprendieron de #animales#"],
        "seed2": ["#animales# miran"],
        "seed3": ["#electronico# #verbos# los chicos."],
        "seed4": ["#electronico# cambian"],
        "seed5": ["#electronico# #verbos# #animales#"],
        "seed6": ["#electronico# cambian"],
        "seed7": ["#animales# miran"],
        "seed8": ["#animales# aprenden de #electronico#"],
        "seed9": ["los chicos aprendieron de #animales#"],
        "seed10": ["Los chicos cambian", "La tierra cambio", "#subjects# cambiaron"],
        "seed11": ["#subjects# no entendian todo los cambios"],
        "seed12": ["La tierra mira"],
        "seed13": ["#subjects# aprendieron de la tierra"],

        "title": [
          "Fabula #fabulaSubject#",
          "Fabula #fabulaSubject# y #fabulaSubject#",
          "Una Fabula #fabulaType#",
          "Una Fabula #fabulaType# #fabulaSubject#",
        ],
        "fabulaType":[
          "Corta",
          "Breve",
          "Muy Corta",
          "Brusca",
          "Pequeña"
        ],
        "fabulaSubject": [
          "de Ensenanza",
          "de Olvidanza",
          "de Desaprendizaje",
          "de Aprendizaje",
          "Teorética",
          "Inposible",
          "Fabulosa",
          "Repetida",
          "Recursiva",
          "de Sabiduria",
          "de Inteligencia",
          "de Conocimiento",
          "de Descubrir",
        ],
        "subjects": ["#electronico#", "lost chicos", "#animales#"],
        "verbos": ["aprenden de", "miran a"],
        "electronico": ["las televisiónes", "las radios", "los telefonos", "los libros", "los diarios", "las noticias", "los teatros", "las camaras", "las computadoras", "las películas", "los autos", "los hologramas"],
        "animales": ["los pajaros", "las abejas", "los escorpiones", "los gusanos", "los hongos", "los cuervos"]
    }
