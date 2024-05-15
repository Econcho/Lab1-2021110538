import string
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


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

    def showDirectedGraph(self):
        """用户选择文件，根据文件生成图并打印"""
        # 选择文件
        window = tk.Tk()
        window.withdraw()
        filepath = filedialog.askopenfilename()

        # 将句子去除标点并划分为token
        lines = open(filepath).readlines()
        for i in range(len(lines)):
            for piece in lines[i]:
                if piece in string.punctuation:
                    lines[i] = lines[i].replace(piece, " ")  # 遍历每个句子的每个字母，如果发现是标点（在string.punctuation）中就替换为空格
            lines[i] = lines[i].split()

        # 将token加入图
        g = nx.Graph()
        for line in lines:
            for i in range(len(line) - 1):
                self.graph.addEdge(start=line[i], end=line[i + 1])

        # 画图并保存
        g = nx.DiGraph()
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
        pass  # 深度为2的DFS/BFS即可

    def generateNewText(self, inputText: str):
        pass

    def calcShortestPath(self, word1: str, word2: str):
        pass

    def randomWalk(self):
        pass


def main():
    f = WordGraph()
    f.showDirectedGraph()


if __name__ == '__main__':
    main()
