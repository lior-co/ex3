# ex3

*** ReadMe by Lior Cohen - EX3 ***

== DiGraphp.py ==
=Node=
__init__(node_id: int, pos: tuple = None)
-Use x and y for the position.
-Use out_e dict for all thr out edge from this node.

__reper__
-String to thr graph.

=Edge=
__init__(id1: int, id2: int, weight: float)
-Edge by the @id1 (key of source) and @id2 (key of destination).
-whight of thr edge

__reper__
-To String to thr edge.

=DiGraph=
__init__
-Have all v ind dict.

__repr__
-To string to graph.

v_size
-Return number of v (nodes).

e_size
-Return number of edges.

get_all_v
-Return dict of all v in graph.
