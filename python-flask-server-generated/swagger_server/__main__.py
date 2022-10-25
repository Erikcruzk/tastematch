#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    data = pd.read_csv("data/random_recipes1.csv")
    X = data.drop(['recipe_id'], axis=1)
    y = data.recipe_id

    from sklearn.model_selection import train_test_split
    ## Split data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    ## Import the Classifier.
    ## Instantiate the model with 5 neighbors. 
    model = KNeighborsClassifier(n_neighbors=5)
    ## Fit the model on the training data.
    model.fit(X_train, y_train)
    ## See how the model performs on the test data.
    # print(model.score(X_test, y_test))

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'TasteMatch - OpenAPI 3.0'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
