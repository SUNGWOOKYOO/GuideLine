from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import matplotlib.pyplot as plt
import sys

#######################################################################
# Set Environments
#######################################################################
cpus = tf.config.experimental.list_physical_devices('CPU')
gpus = tf.config.experimental.list_physical_devices('GPU')
MEMORY_LIMIT_CONFIG = [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)]
tf.config.experimental.set_virtual_device_configuration(gpus[0], MEMORY_LIMIT_CONFIG)

print(tf.__version__)
print(cpus)
print(gpus)
print(MEMORY_LIMIT_CONFIG)
print('GPU available?', tf.test.is_gpu_available())

#######################################################################
# Make Dataset
#######################################################################
TRUE_W = 3.0
TRUE_b = 2.0
NUM_EXAMPLES = 1000
EPOCHS = 10
BATCH_SIZE = 100
STEPS = NUM_EXAMPLES//BATCH_SIZE

inputs  = tf.random.normal(shape=[NUM_EXAMPLES])
noise   = tf.random.normal(shape=[NUM_EXAMPLES])
outputs = inputs * TRUE_W + TRUE_b + noise

dataset_x = tf.data.Dataset.from_tensor_slices(inputs)
dataset_y = tf.data.Dataset.from_tensor_slices(outputs)
dataset = tf.data.Dataset.zip((dataset_x, dataset_y))
batched_dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)

print("Dataset.shape = [input:{} output:{}]".format(inputs.shape, outputs.shape))

#######################################################################
# Build Model
#######################################################################
class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__(name='swyoo')
        self.Dense = tf.keras.layers.Dense(units=1, input_shape=[None, 1])

    def call(self, input_tensor):
        """
        Args:
            input_tensor.shape=(samples, )
        Return.shape=(samples, )
        """
        return tf.squeeze(self.Dense(tf.expand_dims(input_tensor, axis=-1)), axis=-1)

model = Model()
predictions = model(inputs)
print(model.summary())
print(model.trainable_variables)

print("================= Before Training ==================")
# plot inital examples and predictions
plt.scatter(inputs, outputs, c='b')
plt.scatter(inputs, model(inputs), c='r')
plt.show()

#######################################################################
# Train Phase
#######################################################################
def print_progress(epoch, max_epoch, step, max_step, loss, bar):
    """ print progressive states """
    # Status-message. Note the \r which means the line should
    # overwrite itself.
    msg = "\r Train Phase - epoch: {0:}/{1:} |step: {2:}/{3:} |loss: {4:.3f} |bar: {5:}".format(epoch, max_epoch, step, max_step, loss, bar)
    # Print it.
    sys.stdout.write(msg)
    sys.stdout.flush()

def loss_function(predicted_y, true_y):
    """ predicted_y, true_y are tensor for minibatch  """
    return tf.reduce_mean(tf.square(predicted_y - true_y))

optimizer = tf.keras.optimizers.Adam(learning_rate=1e-1)

# Notice the use of `tf.function`
# This annotation causes the function to be "compiled".
@tf.function
def train_step(inputs, outputs):
    """
    Global:
        model, optimizer
    Args:
        inputs, outputs
    """
    with tf.GradientTape() as T:
        loss_mini = loss_function(model(inputs), outputs)
    grads = T.gradient(target=loss_mini, sources=model.trainable_variables)
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.trainable_variables))
    return loss_mini

history = []
for e in range(EPOCHS):
    bar = ''
    loss = 0
    for s, batch_list in enumerate(batched_dataset.take(BATCH_SIZE)):
        X_mini, Y_mini = batch_list
        ###############################################
        # TODO: train for a step
        ###############################################
        loss_mini = train_step(X_mini, Y_mini)
        ###############################################
        bar+='#'
        print_progress(e+1, EPOCHS, s+1, STEPS, loss_mini, bar)
        loss += loss_mini
    history.append(loss.numpy()/STEPS)

print("================= After Training ==================")
# Plot loss graph
plt.plot(range(EPOCHS), history, 'r')
plt.legend(['loss'])
plt.show()

# plot inital examples and predictions
plt.scatter(inputs, outputs, c='b')
plt.scatter(inputs, model(inputs), c='r')
plt.show()