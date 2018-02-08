import numpy as np

def _sigmoid(X):
    '''Compute the sigmoid function '''
    return 1.0 / (1.0 + np.exp(-1.0 * X))

def _threshold(X,threshold=.5):
    '''Threshold at 0.5 for classification'''
    return (X > threshold).astype(int)

def _softmax(x):
    '''Softmax (e^x)/sum(e^x)'''
    # subracting np.argmax(x) prevents under/over flow
    # expand_dims fixes dimension issue
    return np.exp(x - np.argmax(x))/np.expand_dims(np.sum(np.exp(x - np.argmax(x)),axis=1),axis=1)

def logistic_regression(X,theta=None):
    '''
    Logistic Regression

        X: input, expected shape ~ (num samples, num attributes)
        theta: parameters, expected shape ~ (num attributes,)
    '''
    # generate parameters theta if not specified
    if not theta:
        # theta ~ U[-1,1]
        theta = np.random.uniform(-1,1,size=X.shape[1])

    return _threshold(_sigmoid(np.dot(X, theta)))

def multi_layer_perceptron(X,H=10,output_layer=1,W1=None,W2=None):
    '''
    Multi Layer Perceptron with a single hidden layer

        X: input, expected shape ~ (num samples, num attributes)
        H: number of hidden units
        output_layer: number of output units (1 -> sigmoid, 2+ -> softmax)
        W1: layer 1 weights
        W2: layer 2 weights
    '''
    if not W1 and not W2:
        W1 = np.random.uniform(-1e-3,1e-3,size=(X.shape[1],H))
        b1 = np.ones((1,H))
        W2 = np.random.uniform(-1e-3,1e-3,size=(H,output_layer))
        b2 = np.ones((1,output_layer))
    #
    hidden_layer = np.maximum(0, np.dot(X, W1) + b1)
    scores = np.dot(hidden_layer, W2) + b2
    if output_layer == 1:
        return _threshold(_sigmoid(scores))

    return np.argmax(_softmax(scores),axis=1)

# example data ~ 20 samples, 3 attributes
x = np.random.uniform(2,4,size=(20,3))
# logistic regression example
print logistic_regression(x)
# mlp example
print multi_layer_perceptron(x,output_layer=2)
