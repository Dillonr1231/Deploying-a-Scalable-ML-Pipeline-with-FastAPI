import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics


def test_model_train_type():
    """
    Tests that the train_model returns a RandomForestClassifier
    """
    X = np.random.rand(20,4)
    y = np.random.randint(0, 2, size = 20)
    model = train_model(X,y)

    assert isinstance(model, RandomForestClassifier)



def test_inference_output():
    """
    Test the inference returns the correct number of predictions. 
    """
    X = np.random.rand(10,4)
    y = np.random.randint(0, 2, size=10)
    model = train_model(X,y)
    preds = inference(model, X)

    assert len(preds) == len(X)


def test_compute_model_metrics_range():
    """
    Test that precision, recall, and F1 sscore are between 0 and 1
    """
    y_true = np.array([0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0