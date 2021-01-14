from typing import List
import matplotlib.pyplot as plt
import json
import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, dig: DiGraph = None):
        if dig is None:
            self.g = DiGraph()
        else:
            self.g = dig

    def __repr__(self):
        return self.g.__repr__()

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        # {"Edges":[{"src":0,"w":0,"dest":0},...
        # "Nodes": [{"pos": "0,0,0", "id": 0},...}
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
                # print(data['Edges'])
                # print(data['Nodes'])
                for i in data['Nodes']:
                    if 'pos' not in data['Nodes']:
                        self.g.add_node(i['id'])
                    else:
                        self.g.add_node(i['id'], (i['pos']))
                for i in data['Edges']:
                    self.g.add_edge(i['src'], i['dest'], i['w'])
                return True
        except():
            print("An exception occurred")
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as json_file:
                data = {'Edges': [], 'Nodes': []}
                for i in self.g.v.keys():
                    if self.g.v[i].pos is None:
                        data['Nodes'].append({"id": i})
                    else:
                        data['Nodes'].append({"pos": self.g.v[i].pos, "id": i})
                    for j in self.g.v[i].out_e:
                        data['Edges'].append({"src": i, "w": self.g.v[i].out_e[j].weight, "dest": j})

                json.dump(data, json_file)

                return True
        except():
            print("An exception occurred")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if (id1 is id2) and (id1 in self.g.v.keys()) and (id2 in self.g.v.keys()):
            return 0, [id1]
        if (id1 in self.g.v.keys()) and (id2 in self.g.v.keys()):
            self.dijkstra(id1)
            if self.g.v[id2].p is None:  # id1 and id2 not connected
                return 0, []  # None shortest_path
            path = []
            x_ = id2
            while x_ != id1:
                if x_ is None:
                    return float('inf'), None
                path.append(x_)
                temp_ = x_
                x_ = self.g.v[temp_].p
            path.append(x_)  # add id1
            path.reverse()
            return self.g.v[id2].weight, path
        return 0, []  # None shortest_path

    def connected_component(self, id1: int) -> list:
        if id1 not in self.g.v.keys():
            return []
        tarjan = self.connected_components()
        for i in range(len(tarjan)):
            if id1 in tarjan[i]:
                return tarjan[i]

    def connected_components(self) -> List[list]:
        # visited node by weight = 0
        # non visited node by weight = flot(inf)
        # on stack by tag (True / False)
        self.reset_graph()
        stack = []
        low_link = {}
        ids = {}
        ans = []
        idd = [-1]  # count id

        def dfs(at: int):
            self.g.v[at].weight = 0  # visited
            stack.append(at)  # add to stack
            idd[0] += 1
            low_link[at] = idd[0]
            ids[at] = idd[0]
            self.g.v[at].tag = True
            for j in self.g.v[at].out_e:
                if self.g.v[j].weight != 0:  # non visited
                    dfs(j)
                if self.g.v[j].tag:
                    low_link[at] = min(low_link[at], low_link[j])
            if ids[at] == low_link[at]:
                new_ans = []
                while True:
                    z = stack.pop()
                    self.g.v[z].tag = False
                    low_link[at] = z
                    new_ans.append(z)
                    if z == at:
                        new_ans.reverse()
                        ans.append(new_ans)
                        break

        for i in self.g.v.keys():
            if self.g.v[i].weight != 0:  # non visited
                dfs(i)
        return ans

    def plot_graph(self) -> None:
        for i in self.g.v.keys():
            for j in self.g.v[i].out_e:
                dx = self.g.v[j].x - self.g.v[i].x  # x1 - x0
                dy = self.g.v[j].y - self.g.v[i].y  # y1 - y0
                plt.arrow(self.g.v[i].x, self.g.v[i].y, dx, dy, width=0.005, length_includes_head=True, head_width=0.3, head_length=0.5, overhang=0.5)
            plt.text(self.g.v[i].x, self.g.v[i].y, s=i, size=20, color='r')    # number of node
            plt.plot(self.g.v[i].x, self.g.v[i].y, 'o')    # node
        plt.show()
        return None

    def reset_graph(self):
        for n in self.g.v:
            self.g.v[n].info = ""  # reset info as ""
            self.g.v[n].tag = False  # reset all tag as False
            self.g.v[n].weight = float('inf')  # reset all node weight as infinity

    def dijkstra(self, id1: int):
        if id1 not in self.g.v.keys():
            return
        self.reset_graph()
        pq = [id1]  # "PriorityQueue"
        self.g.v[id1].weight = 0  # weight of id1 set as 0
        self.g.v[id1].tag = 0
        min_w = 0  # for "PriorityQueue"
        while len(pq) != 0:
            if len(pq) > 1:  # for "PriorityQueue" choose the node with min weight
                for r in range(len(pq) - 1):
                    if self.g.v[pq[r]].weight < self.g.v[pq[r + 1]].weight:
                        min_w = r
                    else:
                        min_w = r + 1
            else:
                min_w = 0
            current = pq.pop(min_w)  # current node (parent)
            if self.g.v[current].info == "":
                self.g.v[current].info = "yes"  # set info as visited
                for i in self.g.v[current].out_e.keys():
                    weight_new_ = self.g.v[current].weight + self.g.v[current].out_e[i].weight
                    if weight_new_ < self.g.v[i].weight:
                        self.g.v[i].weight = weight_new_  # set the smaller weight
                        self.g.v[i].p = self.g.v[current].node_id  # current node id parent of node i
                        pq.append(i)  # add node_id i to "PriorityQueue"
