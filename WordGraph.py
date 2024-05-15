
class Edge:
    def __init__(self, start, end, weight:int):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    """存储有向图的数据结构"""
    def __init__(self):
        self.edge_list = [] # 存储边的临接表
        self.vertex_dict = {} # 顶点字符串-标号查找表
    def addEdge(self, start:str, end:str):
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
            if  edge.end == end:
                edge.weight += 1
                return
        # 边不存在
        self.edge_list[v1].append(Edge(start, end, 1))
    def getEdgeList(self, vertex:str):
        """
        获取从某个顶点出发的边列表，也可以用于判断顶点是否存在
        返回值为None则顶点不存在，否则返回Edge组成的列表
        """
        v = self.vertex_dict.get(vertex, None)
        if v is None:
            return None
        return self.edge_list[v]

class WordGraph:
    def __init__(self, inputText:str):
        self.graph = Graph()
    def showDirectedGraph(self):
        pass # 用传说networkx库
    def queryBridgeWords(self, word1:str, word2:str):
        pass # 深度为2的DFS/BFS即可
    def generateNewText(self, inputText:str):
        pass
    def calcShortestPath(self, word1:str, word2:str):
        pass
    def randomWalk(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
