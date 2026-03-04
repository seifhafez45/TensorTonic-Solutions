import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    b = np.random.randint(1)
    X = np.array(X)
    try:
      X.shape[1]
      
    except:
      X=X.reshape(-1,1)  
    y = np.array(y).reshape(-1,1)
  
    w = np.random.random(X.shape[1]).reshape(-1,1)
    # Write code here
    for _ in range(steps):
        y_hat = _sigmoid(np.dot(X,w)+b)

        w = w-lr*np.dot(X.T, (y_hat- y))/len(X)
        
        b = b-lr*np.mean((y_hat - y))
    return(w.flatten(),b)
    pass