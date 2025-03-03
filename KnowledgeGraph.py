import networkx as nx
import matplotlib.pyplot as plt
import re
GRAPH = nx.DiGraph()

KNOWLEDGE_NODES = [
    ("Enseñanza del Habla", "Estrategias de Comunicación"),
    ("Enseñanza del Habla", "Actividades Prácticas"),
    ("Enseñanza del Habla", "Recursos Educativos"),
    ("Estrategias de Comunicación", "Refuerzo Positivo"),
    ("Estrategias de Comunicación", "Uso de Imágenes"),
    ("Estrategias de Comunicación", "Lenguaje de Señas"),
    ("Actividades Prácticas", "Juegos de Palabras"),
    ("Actividades Prácticas", "Canciones y Rimas"),
    ("Actividades Prácticas", "Cuentos Interactivos"),
    ("Recursos Educativos", "Aplicaciones Móviles"),
    ("Recursos Educativos", "Libros Especializados"),
    ("Recursos Educativos", "Videos Educativos"),
    ("Refuerzo Positivo", "Elogios Verbales"),
    ("Refuerzo Positivo", "Recompensas Simbólicas"),
    ("Uso de Imágenes", "Tarjetas de Vocabulario"),
    ("Uso de Imágenes", "Pictogramas"),
    ("Lenguaje de Señas", "Señas Básicas"),
    ("Lenguaje de Señas", "Señas Avanzadas"),
    ("Juegos de Palabras", "Memoramas"),
    ("Juegos de Palabras", "Rompecabezas de Letras"),
    ("Canciones y Rimas", "Ritmo y Melodía"),
    ("Canciones y Rimas", "Repetición de Palabras"),
    ("Cuentos Interactivos", "Preguntas y Respuestas"),
    ("Cuentos Interactivos", "Identificación de Personajes"),
    ("Aplicaciones Móviles", "Apps de Pronunciación"),
    ("Aplicaciones Móviles", "Apps de Vocabulario"),
    ("Libros Especializados", "Libros con Pictogramas"),
    ("Libros Especializados", "Libros de Cuentos"),
    ("Videos Educativos", "Videos de Pronunciación"),
    ("Videos Educativos", "Videos de Historias"),
    ("Aprendizaje de la Lectura", "Método Global"),
    ("Aprendizaje de la Lectura", "Método Fonológico"),
    ("Aprendizaje de la Lectura", "Estrategias Visuales"),
    ("Método Global", "Reconocimiento de palabras completas"),
    ("Método Global", "Uso de imágenes y pictogramas"),
    ("Método Fonológico", "Asociación letra-sonido"),
    ("Método Fonológico", "Repetición y práctica"),
    ("Estrategias Visuales", "Tarjetas con palabras e imágenes"),
    ("Estrategias Visuales", "Uso de colores y símbolos"),


    ("Cursos", "Cursos de Repetición"),
    ("Cursos", "Cursos de Pronunciación"),
    ("Cursos", "Cursos de Vocabulario"),

    # Detalles de los cursos
    ("Cursos de Repetición", "Retroalimentación IA"),
    ("Cursos de Repetición", "Métricas de Progreso"),
    ("Cursos de Repetición", "Ejercicios Adaptivos"),

    ("Retroalimentación IA", "Análisis de Pronunciación"),
    ("Retroalimentación IA", "Sugerencias de Mejora"),
    ("Retroalimentación IA", "Reportes de Desempeño"),

    ("Métricas de Progreso", "Precisión de Pronunciación"),
    ("Métricas de Progreso", "Velocidad de Respuesta"),
    ("Métricas de Progreso", "Nivel de Vocabulario"),
]

GRAPH.add_edges_from(KNOWLEDGE_NODES)
plt.figure(figsize=(16, 12), dpi=300)  # Larger size and higher resolution
nx.draw(
    GRAPH,
    with_labels=True,
    node_size=500,  # Increased node size
    node_color="skyblue",
    font_size=8,  # Adjusted font size
    font_weight="bold",
    arrows=True,  # Show direction of relationships
    edge_color="gray",
    width=1,
    arrowsize=10
)
plt.title("Grafo de Conocimiento - Enseñanza del Habla", fontsize=16, pad=20)
plt.tight_layout()  # Adjust layout to prevent label clipping
plt.show()

def responder_pregunta(pregunta):
    pregunta = pregunta.lower()
    pregunta = pregunta.replace("¿", "").replace("?", "")  # Remove question marks

    # Using regex for "qué es" or "que es"
    patron_que_es = re.compile(r"qu[eé]\s+es\s+(.+)")
    match = patron_que_es.search(pregunta)
    if match:
        for nodo in GRAPH.nodes:
            if nodo.lower() in pregunta:  # Check if node name is mentioned
                subtemas = list(GRAPH.successors(nodo))
                predecesores = list(GRAPH.predecessors(nodo))
                if subtemas and predecesores:
                    return f"{nodo} es un concepto que forma parte de {', '.join(predecesores)} y incluye: {', '.join(subtemas)}."
                elif subtemas:
                    return f"{nodo} es un área que incluye los siguientes conceptos: {', '.join(subtemas)}."
                elif predecesores:
                    return f"{nodo} es un concepto específico dentro de {', '.join(predecesores)}."
                else:
                    return f"{nodo} es un concepto final en nuestro sistema de enseñanza."

    # Using regex for "cómo" or "como"
    patron_que_es = re.compile(r"c[oó]mo\s+(.+)")
    match = patron_que_es.search(pregunta)
    # Pregunta: ¿Cómo?
    if match:
        for nodo in GRAPH.nodes:
            if nodo.lower() in pregunta:  # Check if node name is mentioned
                subtemas = list(GRAPH.successors(nodo))
                if subtemas:
                    return f"Para trabajar con {nodo}, puedes utilizar: {', '.join(subtemas)}."

    # Buscar temas relacionados
    if "relacionado" in pregunta or "similar" in pregunta:
        for nodo in GRAPH.nodes:
            if nodo.lower() in pregunta:
                relacionados = set(GRAPH.successors(nodo)) | set(GRAPH.predecessors(nodo))
                if relacionados:
                    return f"Los conceptos relacionados con {nodo} son: {', '.join(relacionados)}."

    # Búsqueda por palabras clave
    palabras_clave = {
        "actividad": "Las actividades disponibles incluyen: Juegos de Palabras, Canciones y Rimas, y Cuentos Interactivos.",
        "recurso": "Los recursos educativos incluyen: Aplicaciones Móviles, Libros Especializados y Videos Educativos.",
        "estrategia": "Las estrategias de comunicación incluyen: Refuerzo Positivo, Uso de Imágenes y Lenguaje de Señas.",
        "ejercicio": "Ofrecemos ejercicios adaptivos con retroalimentación de IA y métricas de progreso.",
        "ayuda": "Puedo informarte sobre actividades, recursos, estrategias y ejercicios disponibles."
    }

    for palabra, respuesta in palabras_clave.items():
        if palabra in pregunta:
            return respuesta


    # Consulta de ruta de aprendizaje
    if "aprender" in pregunta or "comenzar" in pregunta:
        ruta = list(nx.dfs_preorder_nodes(GRAPH, "Enseñanza del Habla"))[:5]
        return f"Te sugiero comenzar con: {' → '.join(ruta)}"

    # Mantener saludos existentes
    if "hola" in pregunta:
        return "¡Hola! Puedo ayudarte con información sobre enseñanza del habla, actividades, recursos y estrategias."

    if "adiós" in pregunta:
        return "¡Hasta luego! Espero que la información haya sido útil."

    return "No tengo información específica sobre esa pregunta. Prueba preguntando sobre actividades, recursos o estrategias específicas."