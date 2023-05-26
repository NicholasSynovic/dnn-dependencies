#!/bin/bash

wget https://gexf.net/1.2/gexf.xsd
wget https://gexf.net/1.2/data.xsd
wget https://gexf.net/1.2/dynamics.xsd
wget https://gexf.net/1.2/hierarchy.xsd
wget https://gexf.net/1.2/phylogenics.xsd
wget https://gexf.net/1.2/viz.xsd

xmllint --noout --schema gexf.xsd $1
