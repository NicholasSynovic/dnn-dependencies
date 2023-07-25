import unittest

import networkx as nx
import similarity


class metricsTesting(unittest.TestCase):
    def testComputeDensity(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.computeDensity(G)

        self.assertNotEqual(actual, (-1 * actual))
        self.assertNotEqual(actual, 0.5)
        self.assertEqual(actual, 0.00036878179081766563)

    def testCountNodes(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.countNodes(G)

        self.assertNotEqual(actual, 30)
        self.assertEqual(actual, 3104)
        self.assertNotEqual(actual, (-1 * actual))

    def testCountEdges(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.countEdges(G)

        self.assertNotEqual(actual, 3000)
        self.assertNotEqual(actual, (-1 * actual))
        self.assertEqual(actual, 3552)

    def testCountCommunities(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.countCommunities(G)

        self.assertNotEqual(actual, 40)
        self.assertNotEqual(actual, (-1 * actual))
        self.assertEqual(actual, 1170)

    def testComputeDegreeDistribution(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.computeDegreeDistribution(G)

        self.assertNotEqual(actual, {0: 30, 1: 20, 2: 90, 3: 20, 4: 122, 5: 20})
        self.assertNotEqual(actual, {key: -value for key, value in actual.items()})
        self.assertEqual(actual, {0: 1227, 1: 589, 2: 1069, 3: 74, 4: 122, 5: 23})

    def testComputeClusteringCoefficient(self):
        G: nx.DiGraph = nx.read_gexf(
            "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
        )
        actual = similarity.computeClusteringCoefficientDistribution(G)

        self.assertNotEqual(
            actual,
            {
                0: 3000,
                0.03333333333333333: 2,
                0.05: 90,
                0.08333333333333333: 25,
                0.5: 20,
            },
        )
        self.assertNotEqual(actual, {key: -value for key, value in actual.items()})
        self.assertEqual(
            actual,
            {
                0: 3029,
                0.03333333333333333: 1,
                0.05: 23,
                0.08333333333333333: 26,
                0.5: 25,
            },
        )
