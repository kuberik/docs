#!/usr/bin/env python3
from diagrams import Diagram, Edge, Cluster
from diagrams.k8s.compute import Job, Pod
from diagrams.custom import Custom
from diagrams.generic.blank import Blank


edge_attr = {
    "color": "#1cbfa9",
    "style": "invis",
}

node_attr = {
    "fontcolor": "#e9e9e9"
}

graph_attr = {
    "bgcolor": "#00000000",
    "fontcolor": "#e9e9e9",
    "pad": "0",
}

graph_attr_scene = {
    "color": "#e9e9e9",
    "style": "none",
    "bgcolor": "#24f2d744",
}
graph_attr_frame = {
    "style": "none",
    "bgcolor": "#24f2d744",
    "color": "#e9e9e9",
}

with Diagram(filename="play_components", show=False, edge_attr=edge_attr, direction="TB", outformat="png", graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("Play", graph_attr=graph_attr_scene):
        with Cluster("Screenplays", graph_attr=graph_attr_scene):
            with Cluster("Scenes", graph_attr=graph_attr_scene):
                with Cluster("Frames", graph_attr=graph_attr_frame):
                    frame_a2 = Job("Action")
