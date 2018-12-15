## Regularization (2 days)

* Empirical Risk Minimization
    * Motivation
    * Formulation
    * When does regularization help? How does it help?
    * See section on Regularization in Wikipedia article on [Statistical Learning Theory](https://en.wikipedia.org/wiki/Statistical_learning_theory#Regularization)
* Data augmentation
    * Examples with different types of input data
        * Visual
        * Textual
        * Aural
    * Train- versus inference-time augmentation
        * Train-time: too few examples, too many parameters
        * Test-time: too complex a mapping from inputs to outputs, similar to using ensemble
* Weight Decay
    * When is it beneficial?
    * L1, L2 - their effects
    * Implementation details - adding to gradients, adding to loss
* Stochastic Regularization
    * Additive noise
        * [Training with Noise is Equivalent to Tikhonov Regularization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bishop-tikhonov-nc-95.pdf)
    * Dropout
        * Two interpretations
            * Preventing overfitting/conspiracies
            * Implicit ensemble
        * Implementation details
* Connection between optimization and regularization (specifically, data augmentation): the conclusion that "we obtain an unbiased estimator of the exact gradient of the generalization error by sampling a minibatch of examples {x_1, ..., x_m} with corresponding targets y_i from the data generating distribution p_data, and computing the gradient of the loss with respect to the parameters for that minibatch", **so long as examples are not reused** (emphasis added) ties the optimization of models trained with relatively small datasets (by today's standards) to data augmentation in that data augmentation can effectively increase the number of examples beyond the total number of unique examples necessary for the training to converge, thereby ensuring that examples are not reused, at least in some form. The kind of data augmentation I have in mind: crops, perturbations of hue, brightness, contrast (images); random dropout of words, random substitution of synonyms (text); dropout of activations; addition of Gaussian noise to activations.

