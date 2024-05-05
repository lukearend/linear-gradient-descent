# linear-gradient-descent

This repository investigates gradient descent in linear networks as described in the paper [Exact solutions to the nonlinear dynamics of learning in deep linear neural networks](https://arxiv.org/abs/1312.6120) by Andrew Saxe, James McClelland, and Surya Ganguli.

Everything is in the self-contained notebook [linear-gradient-descent.ipynb](https://github.com/lukearend/linear-gradient-descent/blob/main/linear-gradient-descent.ipynb), which

1. explains and implements gradient descent for the linear network,
2. trains a linear network to solve a classification task, and
3. investigates a learning regime called _dynamical isometry_.

To run the notebook yourself,

1. clone this repo: `git clone ...`
2. run `make env` at the top level to build a python environment with the packages listed in `requirements.txt`
3. run `make notebook` to start a local Jupyter notebook server
4. browse to `main.ipynb` and open it