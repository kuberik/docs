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

with Diagram(filename="play_lifecycle", show=False, edge_attr=edge_attr, direction="TB", outformat="png", graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("arrow-left", graph_attr={"bgcolor":"#00000000", "peripheries":"0", "label":""}):
        start_left = Blank()
        level1_left = Blank()
        level2_left = Blank()
        end_left = Blank()
        start_left >> level1_left >> level2_left >> end_left
        start_left >> Edge(style="none") >> end_left

    with Cluster("Scene A", graph_attr=graph_attr_scene):
        with Cluster("Frame A2", graph_attr=graph_attr_frame):
            frame_a2 = Job("Action A2")
        with Cluster("Frame A1", graph_attr=graph_attr_frame):
            frame_a1 = Job("Action A1")

    with Cluster("Scene B", graph_attr=graph_attr_scene):
        with Cluster("Frame B3", graph_attr=graph_attr_frame):
            frame_b3 = Job("Action B3")
        with Cluster("[Frame] Story B2", graph_attr=graph_attr_frame):
            with Cluster("Scene B2A", graph_attr=graph_attr_scene):
                with Cluster("Frame B2A1", graph_attr=graph_attr_frame):
                    frame_b2a1 = Job("Action B2A1")
            with Cluster("Scene B2B", graph_attr=graph_attr_scene):
                with Cluster("Frame B2B2", graph_attr=graph_attr_frame):
                    frame_b2b2 = Job("Action B2B2")
                with Cluster("Frame B2B1", graph_attr=graph_attr_frame):
                    frame_b2b1 = Job("Action B2B1")
        with Cluster("Frame B1", graph_attr=graph_attr_frame):
            frame_b1 = Job("Action B1")

    with Cluster("Scene C", graph_attr=graph_attr_scene):
        with Cluster("Frame C2", graph_attr=graph_attr_frame):
            frame_c2 = Job("Action C2")
        with Cluster("Frame C1", graph_attr=graph_attr_frame):
            frame_c1 = Job("Action C1")
        with Cluster("Frame C3", graph_attr=graph_attr_frame):
            frame_c3 = Job("Action C3")

    with Cluster("arrow-right", graph_attr={"bgcolor":"#00000000", "peripheries":"0", "label":""}):
        start_right = Blank()
        level1_right = Blank()
        level2_right = Blank()
        end_right = Blank()
        start_right >> Edge(style="none") >> end_right
        start_right >> level1_right >> level2_right >> end_right

    [frame_a1, frame_a2] >> frame_b2a1

    frame_b2a1 >> [frame_b2b1, frame_b2b2]
    frame_b1 - Edge(constraint="false") - [frame_b2a1, frame_b2b1, frame_b2b2]
    frame_b3 - Edge(constraint="false") - [frame_b2a1, frame_b2b1, frame_b2b2]

    [frame_b2b1, frame_b2b2] >> frame_c1
    [frame_b2b1, frame_b2b2] >> frame_c2
    [frame_b2b1, frame_b2b2] >> frame_c3

    # start - Edge(constraint="false") - [frame_a1]
    # start - Edge(constraint="false") - [frame_a1]
