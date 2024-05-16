import string
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def openfile():
    """用户选择文件，返回文件路径"""
    window = tk.Tk()
    window.withdraw()
    return filedialog.askopenfilename()


class Edge:
    def __init__(self, start, end, weight: int):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    """存储有向图的数据结构"""

    def __init__(self):
        self.edge_list = []  # 存储边的临接表
        self.vertex_dict = {}  # 顶点字符串-标号查找表

    def addEdge(self, start: str, end: str):
        """添加边，权重为1，如果边存在则权重+1"""
        v1 = self.vertex_dict.get(start, None)
        v2 = self.vertex_dict.get(end, None)
        # 创建顶点
        if v1 is None:
            v1 = len(self.vertex_dict)
            self.vertex_dict[start] = v1
            self.edge_list.append([])
        if v2 is None:
            v2 = len(self.vertex_dict)
            self.vertex_dict[end] = v2
            self.edge_list.append([])
        # 边存在
        for edge in self.edge_list[v1]:
            if edge.end == end:
                edge.weight += 1
                return
        # 边不存在
        self.edge_list[v1].append(Edge(start, end, 1))

    def getEdgeList(self, vertex: str):
        """
        获取从某个顶点出发的边列表，也可以用于判断顶点是否存在
        返回值为None则顶点不存在，否则返回Edge组成的列表
        """
        v = self.vertex_dict.get(vertex, None)
        if v is None:
            return None
        return self.edge_list[v]


class WordGraph:
    def __init__(self):
        self.graph = Graph()

    def generateGraph(self):
        """用户选择文件，根据文件生成图，保存在self.graph"""
        filepath = openfile()

        # 将句子去除标点并划分为token
        tokens = list()
        lines = open(filepath).readlines()
        for i in range(len(lines)):
            for piece in lines[i]:
                if piece in string.punctuation:
                    lines[i] = lines[i].replace(piece, " ")  # 遍历每个句子的每个字母，如果发现是标点（在string.punctuation）中就替换为空格
            tokens = tokens + lines[i].split()

        # token转小写
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        # 将token加入图
        for i in range(len(tokens) - 1):
            self.graph.addEdge(start=tokens[i], end=tokens[i + 1])

    def showDirectedGraph(self):
        """画self.graph"""
        g = nx.DiGraph()  # 有向图
        g.add_nodes_from(node for node in self.graph.vertex_dict.keys())
        for i in self.graph.vertex_dict.values():
            i_start_edges = self.graph.edge_list[int(i)]
            for node_end, j in self.graph.vertex_dict.items():
                for edge in i_start_edges:
                    if edge.end == node_end:
                        g.add_edge(edge.start, edge.end, weight=edge.weight)

        pos = nx.spring_layout(g, iterations=20)
        weights = nx.get_edge_attributes(g, "weight")
        nx.draw_networkx(g, pos)
        nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)

        plt.savefig("img.png")
        plt.show()

    def queryBridgeWords(self, word1: str, word2: str):
        """查询word1到word2之间的桥接词"""
        # 转小写
        word1 = word1.lower()
        word2 = word2.lower()

        if self.graph.getEdgeList(word1) is None:
            print("No word1 in graph")
            return -1

        if self.graph.getEdgeList(word2) is None:
            print("No word2 in graph")
            return -1

        bridge_words = list()
        for edge_1 in self.graph.getEdgeList(word1):
            word3 = edge_1.end
            for edge_3 in self.graph.getEdgeList(word3):
                if word2 == edge_3.end:
                    bridge_words.append(edge_1.end)

        if len(bridge_words) == 0:
            print("No bridge words from word1 to word2")
            return -1
        else:
            print(f"The bridge words from word1 to word2 are {bridge_words}")
            return bridge_words

    def generateNewText(self, inputText: str):
        pass

    def calcShortestPath(self, word1: str, word2: str):
        pass

    def randomWalk(self):
        pass


def main():
    f = WordGraph()
    f.generateGraph()
    f.showDirectedGraph()
    f.queryBridgeWords('new', 'To')


if __name__ == '__main__':
    main()
