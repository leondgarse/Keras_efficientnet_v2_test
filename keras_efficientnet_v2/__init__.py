from keras_efficientnet_v2.efficientnet_v2 import (
    EfficientNetV2,
    EfficientNetV2B0,
    EfficientNetV2B1,
    EfficientNetV2B2,
    EfficientNetV2B3,
    EfficientNetV2S,
    EfficientNetV2M,
    EfficientNetV2L,
    EfficientNetV2XL,
)

__head_doc__ = """
Keras implementation of [Official efficientnetv2](https://github.com/google/automl/tree/master/efficientnetv2).
Paper [arXiv 2104.00298 EfficientNetV2: Smaller Models and Faster Training](https://arxiv.org/abs/2104.00298) by Mingxing Tan, Quoc V. Le.
"""

__tail_doc__ = """  input_shape: it should have exactly 3 inputs channels. Set `(None, None, 3)` for dynamic.
  num_classes: number of classes to classify images into. Set `0` to exclude top layers.
  dropout: dropout rate if top layers is included.
  first_strides: is used in the first Conv2D layer.
  survivals: is used for [Deep Networks with Stochastic Depth](https://arxiv.org/abs/1603.09382).
      Can be a constant value like `0.5` or `0.8`,
      or a tuple value like `(1, 0.8)` indicates the survival probability linearly changes from `1 --> 0.8` for `top --> bottom` layers.
      A higher value means a higher probability will keep the conv branch.
      or `None` to disable (default).
  classifier_activation: A `str` or callable. The activation function to use on the "top" layer if `num_classes > 0`.
      Set `classifier_activation=None` to return the logits of the "top" layer.
      Default is `softmax`.
  pretrained: value in [None, "imagenet", "imagenet21k", "imagenet21k-ft1k"].
      Will try to download and load pre-trained model weights if not None.
      Save path is `~/.keras/models/efficientnetv2/`.


Returns:
    A `keras.Model` instance.
"""

EfficientNetV2.__doc__ = __head_doc__ + """
Args:
  model_type: is the pre-defined model, value in ["s", "m", "l", "b0", "b1", "b2", "b3"].
  model_name: string, model name.
""" + __tail_doc__ + """
Model architectures:
  | Model             | Params | 1K Top1 acc |
  | ----------------- | ------ | ----------- |
  | EfficientNetV2B0  | 7.1M   | 78.7%       |
  | EfficientNetV2B1  | 8.1M   | 79.8%       |
  | EfficientNetV2B2  | 10.1M  | 80.5%       |
  | EfficientNetV2B3  | 14.4M  | 82.1%       |
  | EfficientNetV2BS  | 21.5M  | 84.9%       |
  | EfficientNetV2BM  | 54.1M  | 86.2%       |
  | EfficientNetV2BL  | 119.5M | 86.9%       |
  | EfficientNetV2BXL | 206.8M | 87.2%       |
"""

EfficientNetV2B0.__doc__ = __head_doc__ + """
Args:
""" + __tail_doc__

EfficientNetV2B1.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2B2.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2B3.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2S.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2M.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2L.__doc__ = EfficientNetV2B0.__doc__
EfficientNetV2XL.__doc__ = EfficientNetV2B0.__doc__
