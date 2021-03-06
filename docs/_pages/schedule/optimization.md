---
layout: default
permalink: schedule/optimization.html
---

## Optimization of Neural Networks (2 days)

* Readings
    * [_Deep Learning_ Chapter 8, Optimization for Training Deep Models, Sections 8.1-8.5](http://www.deeplearningbook.org/contents/optimization.html)
* Initialization
  * Why is it important?
  * Initialization through the decades
* Optimization algorithms
    * Batch gradient descent
    * Stochastic gradient descent (SGD)
        * Momentum
        * Nesterov accelerated gradient
    * Mini-batch SGD
    * Adagrad
    * Adadelta
    * RMSprop
    * Adam
    * Optimization benchmarks
    * When do adaptive gradient algorithms help? When they help, why?
* Hyperparameter selection
    * Grid search
    * Random hyperparameter search
    * Bayesian hyperparameter search
* Distributed optimization
    * [Overview](https://seba-1511.github.io/dist_blog/)
    * [Asynchronous SGD](https://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks)
    * [HogWild](https://arxiv.org/abs/1106.5730)
    * [Large-Scale Distributed Neural Network Training Through Distillation](https://arxiv.org/abs/1804.03235)
        * Horovod ([paper](https://arxiv.org/abs/1802.05799), [code](https://github.com/uber/horovod))
