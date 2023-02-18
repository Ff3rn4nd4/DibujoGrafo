#librerias
import networkx as nx
import matplotlib.pyplot as plt

#crear el grafo vacio
G = nx.Graph()

#anadiendo nodos y ponderandolos 
G.add_edge("1", "2", weight=70)
G.add_edge("1", "3", weight=15)
G.add_edge("1", "4", weight=60)
G.add_edge("2", "1", weight=70)
G.add_edge("2", "5", weight=3)
G.add_edge("2", "6", weight=90)
G.add_edge("2", "7", weight=35)
G.add_edge("2", "8", weight=21)
G.add_edge("3", "1", weight=15)
G.add_edge("3", "9", weight=3)
G.add_edge("3", "10", weight=10)
G.add_edge("4", "1", weight=60)
G.add_edge("4", "11", weight=18)
G.add_edge("4", "12", weight=30)
G.add_edge("4", "13", weight=21)
G.add_edge("4", "14", weight=15)
G.add_edge("5", "2", weight=3)
G.add_edge("5", "15", weight=10)
G.add_edge("6", "2", weight=90)
G.add_edge("6", "16", weight=36)
G.add_edge("6", "17", weight=16)
G.add_edge("7", "2", weight=35)
G.add_edge("7", "26", weight=37)
G.add_edge("7", "27", weight=21)
G.add_edge("7", "28", weight=14)
G.add_edge("7", "29", weight=12)
G.add_edge("8", "2", weight=21)
G.add_edge("8", "39", weight=16)
G.add_edge("8", "40", weight=30)
G.add_edge("8", "42", weight=80)
G.add_edge("9", "3", weight=3)
G.add_edge("9", "48", weight=90)
G.add_edge("10", "3", weight=10)
G.add_edge("11", "4", weight=18)
G.add_edge("12", "4", weight=30)
G.add_edge("13", "4", weight=21)
G.add_edge("14", "4", weight=15)
G.add_edge("15", "5", weight=10)
G.add_edge("15", "16", weight=18)
G.add_edge("15", "17", weight=48)
G.add_edge("16", "15", weight=16)
G.add_edge("17", "15", weight=5)
G.add_edge("18", "6", weight=37)
G.add_edge("18", "20", weight=21)
G.add_edge("18", "21", weight=14)
G.add_edge("18", "22", weight=12)
G.add_edge("19", "6", weight=16)
G.add_edge("19", "23", weight=5)
G.add_edge("19", "23", weight=30)
G.add_edge("19", "24", weight=15)
G.add_edge("20", "18", weight=14)
G.add_edge("21", "18", weight=14)
G.add_edge("22", "18", weight=12)
G.add_edge("23", "19", weight=50)
G.add_edge("24", "19", weight=30)
G.add_edge("25", "29", weight=15)
G.add_edge("26", "30", weight=18)
G.add_edge("27", "7", weight=21)
G.add_edge("27", "31", weight=30)
G.add_edge("27", "32", weight=15)
G.add_edge("27", "33", weight=18)
G.add_edge("28", "7", weight=14)
G.add_edge("28", "34", weight=15)
G.add_edge("28", "35", weight=18)
G.add_edge("29", "7", weight=12)
G.add_edge("29", "37", weight=10)
G.add_edge("29", "38", weight=80)
G.add_edge("30", "26", weight=18)
G.add_edge("31", "27", weight=30)
G.add_edge("32", "27", weight=15)
G.add_edge("33", "27", weight=18)
G.add_edge("34", "28", weight=15)
G.add_edge("35", "28", weight=10)
G.add_edge("36", "29", weight=10)
G.add_edge("37", "29", weight=80)
G.add_edge("38", "8", weight=16)
G.add_edge("38", "41", weight=10)
G.add_edge("38", "42", weight=50)
G.add_edge("39", "7", weight=21)
G.add_edge("39", "8", weight=30)
G.add_edge("39", "43", weight=18)
G.add_edge("39", "44", weight=21)
G.add_edge("39", "43", weight=15)
G.add_edge("40", "8", weight=80)
G.add_edge("40", "46", weight=10)
G.add_edge("40", "47", weight=12)
G.add_edge("41", "38", weight=10)
G.add_edge("42", "38", weight=50)
G.add_edge("43", "39", weight=18)
G.add_edge("44", "39", weight=21)
G.add_edge("45", "39", weight=15)
G.add_edge("46", "40", weight=10)
G.add_edge("47", "40", weight=12)
G.add_edge("48", "9", weight=90)


#generando el grafo de una manera especifica 
pos = nx.spring_layout(G, seed=51)

#modificando nodos (tamano y color)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

#modificando aristas 
nx.draw_networkx_edges(G, pos, width=1)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#muestra en pantalla el grafo
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()