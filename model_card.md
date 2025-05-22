# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a Random Forest Classifier trained to predit wheather an individuals income is greater than or equal to 50K, based on features from the U.S census dataset. It includes categorical and numerical features. 

## Intended Use

This model is intended to be used as a binary classifier to assist in identifing individuals whose income exceeds 50K, based on census features.It could be used for demographic studies or economic research.

## Training Data

The training data is sourced from the U.S. Census Bureau dataset provided in census.csv. 

## Evaluation Data

a 20% split of the original dataset was reserved as test data to evaluate model performance. The test set was processed identically to the training data to help ensure consistency. 

## Metrics

The following metrics were used to evaluate the model: Precision, Recall, and F1 Score. On the test data the models score were as follows:

* Precision: 0.7391
* Recall: 0.6384
* F1 Score: 0.6851

## Ethical Considerations

The model is trained on historical census data, this could reflect social biases, particularly regarding race, gender, and occupation. It should be taken into consideration before decisions are made using this models predictions. 

## Caveats and Recommendations

The model was trained on a specific dataset and may not generalize to populations that are vastly different. Future improvements could include model calibration and fairness auditing. 
