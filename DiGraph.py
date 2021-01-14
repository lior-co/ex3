from GraphInterface import GraphInterface


class Node:
    def __init__(self, node_id: int, pos: tuple = None):
        self.node_id = node_id
        self.info = ""
        self.tag = False
        self.weight = 0
        self.pos = pos
        self.x = 0
        self.y = 0
        # self.z = 0
        if pos is not None:
            xy = list(pos)
            self.x = xy[0]
            self.y = xy[1]
            # self.z = xyz[2]
        self.out_e = {}
        self.out_size = 0
        # self.in_e = {}
        self.in_size = 0
        self.p = None  # parent

    def __repr__(self):
        return '{self.node_id}: |edges out| {self.out_size} |edges in| {self.in_size}'.format(self=self)


class Edge:
    def __init__(self, id1: int, id2: int, weight: float):
        self.id1 = id1
        self.id2 = id2
        self.weight = weight

    def __repr__(self):
        return '|id1| {self.id1} |id2| {self.id2} |weight| {self.weight}'.format(self=self)


class DiGraph(GraphInterface):

    def __init__(self):
        super(DiGraph, self).__init__()
        self.v = {}
        self.e_sum = 0
        self.v_sum = 0
        self.mc = 0

    def __repr__(self):
        return 'Graph: |V|={self.v_sum} , |E|={self.e_sum}'.format(self=self)

    def v_size(self) -> int:
        return len(self.v)

    def e_size(self) -> int:
        return self.e_sum

    def get_all_v(self) -> dict:
        return self.v

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.v.keys():
            return {}  # None
        in_ = {}
        for i in self.v.keys():
            if id1 in self.v[i].out_e.keys():
                in_new_ = {i: self.v[i].out_e[id1].weight}
                in_.update(in_new_)
        return in_

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.v.keys():
            return {}  # None
        out_ = {}
        for i in self.v[id1].out_e.keys():
            out_new_ = {i: self.v[id1].out_e[i].weight}  # {key: weight}
            out_.update(out_new_)
        return out_

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1 in self.v.keys()) and (id2 in self.v.keys()) and (id1 is not id2):
            e = Edge(id1, id2, weight)  # new edge
            e_new = {id2: e}  # new dict with out_e with key of id2
            self.v[id1].out_e.update(e_new)  # add out_e to id1 dict
            self.v[id1].out_size += 1
            self.v[id2].in_size += 1
            # e_new = {id1: e.__dict__}  # new dict with out_e with key of id2
            # self.v[id2]['in_e'].update(e_new)  # add in_e to id2 dict
            self.mc += 1
            self.e_sum += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        n = Node(node_id, pos)  # new node
        n_new = {node_id: n}  # new dict with n
        self.v.update(n_new)  # add n to v dict
        self.mc += 1
        self.v_sum += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.v.keys():
            del self.v[node_id]  # remove this node_id from v dict
            self.v_sum -= 1
            self.mc += 1
            for i in self.v.keys():
                # remove this node_id from out_e dict in this node i dic
                # (remove the edges that connect to this node_id)
                if node_id in self.v[i].out_e.keys():
                    del self.v[i].out_e
                    # self.mc += 1
                    self.e_sum -= 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 in self.v.keys()) and (node_id2 in self.v.keys()) and (node_id1 is not node_id2) and \
                (node_id2 in self.v[node_id1].out_e.keys()):
            del self.v[node_id1].out_e[node_id2]  # remove edge from node_id dict
            self.v[node_id1].out_size -= 1
            self.v[node_id2].in_size -= 1
            self.mc += 1
            self.e_sum -= 1
            return True
        return False
