# Given a protobuf Graph model, print out each layer within the model using Tensorflow

import tensorflow

# Path to the .pb file
pb_path: str = "../models/chessbot.pb"

with tensorflow.io.gfile.GFile(pb_path, "rb") as f:
    graph_def = tensorflow.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

# Extract the subgraph from the graph_def
subgraph = tensorflow.graph_util.extract_sub_graph(graph_def, ["output_tensor_name"])

# Print the names of the nodes in the subgraph
for node in subgraph.node:
    print(node.name)
