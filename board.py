import pandas as pd
import networkx as nx


class GameMap:
    """
    A representation of the map on the game board as an undirected graph.
    Loads nodes from the cities.csv file and loads edges from the
        connections.csv file.
    Each node has a color, 4 values for the number of disease cubes of each
        color, a boolean for if it has a research station, and a boolean for if
        it has had an outbreak in this round.
    """
    def __init__(self):
        self.map = nx.Graph()

        nodes = []
        cities = pd.read_csv('cities.csv')
        for index in cities.index:
            nodes.append((cities.loc[index]['City'],
                         {'color': cities.loc[index]['Color'],
                          'disease0': 0,
                          'disease1': 0,
                          'disease2': 0,
                          'disease3': 0,
                          'has_research_station': False,
                          'has_outbreak': False}))
        self.map.add_nodes_from(nodes)

        edges = []
        connections = pd.read_csv('connections.csv')
        
