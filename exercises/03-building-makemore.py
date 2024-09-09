# E01: I did not get around to seeing what happens when you initialize all weights and biases to zero.
# Try this and train the neural net. You might think either that 1) the network trains just fine or
# 2) the network doesn't train at all, but actually it is 3) the network trains but only partially,
# and achieves a pretty bad final performance. Inspect the gradients and activations to figure out what is happening
# and why the network is only partially training, and what part is being trained exactly.


# E02: BatchNorm, unlike other normalization layers like LayerNorm/GroupNorm etc.
# has the big advantage that after training, the batchnorm gamma/beta can be "folded into" the weights of the
# preceding Linear layers, effectively erasing the need to forward it at test time. Set up a small 3-layer MLP
# with batchnorms, train the network, then "fold" the batchnorm gamma/beta into the preceding Linear layer's W,b by
# creating a new W2, b2 and erasing the batch norm. Verify that this gives the same forward pass during inference.
# i.e. we see that the batchnorm is there just for stabilizing the training, and can be thrown out after training is
# done! pretty cool.