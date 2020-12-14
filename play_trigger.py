#!/usr/bin/env python3
from diagrams import Diagram, Edge, Cluster
from diagrams.k8s.compute import Job, Pod
from diagrams.custom import Custom
from diagrams.k8s.others import CRD


graph_attr = {
    "bgcolor": "#00000000",
    "fontcolor": "#e9e9e9",
    "style": "none",
    "pad": "0",
}
node_attr = {
    "fontcolor": "#e9e9e9",
}
edge_attr = {
    "fontcolor": "#e9e9e9",
    "color": "#1cbfa9",
}

kuberik_icon = "logo.png"
with Diagram(filename="play_trigger", show=False, edge_attr=edge_attr, outformat="png", graph_attr=graph_attr, node_attr=node_attr):
    with Cluster("Screening", graph_attr=graph_attr):
        screener_controller = Pod("Screener Controller")
        screener = CRD("Screener")

    events = CRD("Events")
    screener << Edge(label="configure", **edge_attr) - screener_controller
    screener_controller - Edge(label="") >> events

    movie = CRD("Movie")
    # "\n" fixes padding issues
    engine = Custom("Engine\n", kuberik_icon)
    movie << Edge(constraint="false") - engine
    [events, events, events] << engine

    with Cluster("Pipeline execution", graph_attr=graph_attr):
        play = CRD("Play")
        actions = [Job("Action"), Job("Action"), Job("Action")]

    engine >> [play, play, play]
    movie - Edge(style="dotted") >> play
    play - Edge(style="dotted") >> actions
