import pickle


def load_mnist(start=None, end=None, ncols=None):
    with open('mnist.pkl', 'rb') as f:
        mnist = pickle.load(f)
    X, Y = mnist['X'], mnist['Y']
    mu, W = mnist['mu_whiten'], mnist['W_whiten']
    Y = Y[start:end] * 2 - 1
    X = (X[start:end] - mu) @ W[:, :ncols]
    return X, Y