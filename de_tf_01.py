#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#import tensorflow as tf
#hello = tf.constant('Hello, TensorFlow!')
##sess = tf.Session()

import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('c:\programdata\miniconda3\lib\site-packages')

# To avoid warnings
import warnings
warnings.filterwarnings('ignore')

# Importing keras and tensorflow, and printing the versions
import keras
print('Keras: {}'.format(keras.__version__))

import tensorflow as tf
print('TensorFlow: {}'.format(tf.__version__))

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()

