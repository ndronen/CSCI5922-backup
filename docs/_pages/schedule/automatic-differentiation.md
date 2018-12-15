---
layout: default
permalink: schedule/automatic-differentiation.html
---

## Automatic Differentiation (1 day)
* Method of Finite Difference
* Automatic Differentiation
    * Forward- and Reverse-Mode
    * Source Transformation
        * Advantage: complete representation of control flow, which makes optimization easy
        * Disadvantage: may require implementation of elements of a compiler (verify with Kowarz)
    * Operator overloading
        * Advantage: simple to implement in any language with operator overloading
        * Limitations: control flow information is reduced to the contents of the tape, potentially hindering optimization
* Automatic Differentiation in Deep Learning
    * Declarative (Theano, TensorFlow)
    * Tape-based (PyTorch, Chainer)
* History of Deep Learning Frameworks
    * Torch7, PyTorch
    * Theano
    * Chainer
    * TensorFlow
    * [DyNet](https://github.com/clab/dynet) 
    * Others
    * Wrappers
        * Pylearn2 (Theano)
        * Keras (First Theano, then Theano+TensorFlow, then *)
        * TF-slim (TensorFlow)
* Readings
* Homework
* Resources
    * Andreas Griewank, [On Automatic Differentiation](http://softlib.rice.edu/pub/CRPC-TRs/reports/CRPC-TR89003.pdf)
    * Andreas Griewank, [On Automatic Differentiation and Algorithmic Linearization](http://www.scielo.br/pdf/pope/v34n3/0101-7438-pope-34-03-0621.pdf)
    * Andreas Kowarz, [Advanced Concepts forAutomatic Differentiation Based on Operator Overloading](http://www.qucosa.de/fileadmin/data/qucosa/documents/827/1206719130404-2230.pdf)
    * Håvard Berland, [Talk on Automatic Diffentiation](http://www.robots.ox.ac.uk/~tvg/publications/talks/autodiff.pdf)
    * https://rufflewind.com/2016-12-30/reverse-mode-automatic-differentiation
    * https://gist.github.com/rxwei/30ba75ce092ab3b0dce4bde1fc2c9f1d
    * [Compiling machine learning programs via high-level tracing, Frostig et al, ](https://www.sysml.cc/doc/146.pdf)
