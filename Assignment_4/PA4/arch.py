#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# ALSO, PROVIDE ANSWERS TO THE FOLLOWING TWO QUESTIONS.
#
# Which network architecture achieves the lowest training set error?
#
# The network architecture that achieves the lowest training set error appears to
# be the 2 Hidden Layers. With more layers, there is a less .
#
# Which network architecture tends to exhibit the best testing set accuracy?
#
# The network architecture that tends to exhibit the best testing set accuracy is
# the Training Model with One Hidden Layer. I initially thought it was the Training
# Model with Two Hidden Layers because there is a total of 28 units used in the hidden
# layer, but the other model has only 20 units. I believe using less units in total
# allows for greater accuracy judging by the results when running the program at least
# 20 times.
#
# Arvind Kumar 12/1/2023
#

# PyTorch - Deep Learning Models
import torch.nn as nn
import torch.nn.functional as F


# Number of input features ...
input_size = 4
# Number of output classes ...
output_size = 3


class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layer = nn.Linear(in_features=input_size, out_features=output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        y_hat = self.my_layer(x)
        return y_hat


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        hide_layer = 20
        self.my_layer = nn.Linear(in_features=input_size, out_features=hide_layer)
        self.my_layer2 = nn.Linear(in_features=hide_layer, out_features=output_size)


    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        my_layer_act = F.relu(self.my_layer(x))
        y_hat = self.my_layer2(my_layer_act)
        # my_layer_act = self.my_layer(x)
        # y_hat = F.relu(self.my_layer(my_layer_act))
        return y_hat


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        hide_layer = 16
        hide_layer2 = 12
        self.my_layer = nn.Linear(in_features=input_size, out_features=hide_layer)
        self.my_layer2 = nn.Linear(in_features=hide_layer, out_features=hide_layer2)
        self.my_layer3 = nn.Linear(in_features=hide_layer2, out_features=output_size)


    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        my_layer_act = F.relu(self.my_layer(x))
        my_layer_act2 = F.relu(self.my_layer2(my_layer_act))
        y_hat = self.my_layer3(my_layer_act2)
        return y_hat
