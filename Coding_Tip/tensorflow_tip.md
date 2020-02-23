# Tensorflow Guide

### environment setting

```python
!type python
from warnings import filterwarnings
filterwarnings('ignore')
print(tf.test.is_gpu_available())
```



### dataset

This tutorial is work it through by using [MNIST](https://en.wikipedia.org/wiki/MNIST_database) dataset.

```python
# using tensorflow_gpu=1.12.0, dataset can be downloaded
(train_x, train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()
valid_x, train_x, valid_y, train_y = train_x[:5000], train_x[5000:], train_y[:5000], train_y[5000:]
print("Size of:")
print("- Training-set:\t\t\t{} \t label: \t{}".format(train_x.shape, train_y.shape))
print("- Validation-set:\t\t{} \t\t label: \t{}".format(valid_x.shape, valid_y.shape))
print("- Test-set:\t\t\t{} \t label: \t{}".format(test_x.shape, test_y.shape))
"""
Size of:
- Training-set:		(55000, 28, 28) 	 label: 	(55000,)
- Validation-set:	(5000, 28, 28) 		 label: 	(5000,)
- Test-set:			(10000, 28, 28) 	 label: 	(10000,)
"""
```
[^reference]: you can use this module 

```python
# sklearn==0.21.3
from sklearn.model_selection import train_test_split  
```



#### helper functions for train
 yield mini batch for each iteration
```python
""" helper functions """
# yield mini-batch function
def get_minibatch(X, Y, b):
    """
    inputs: 
    - X: data features, shape (N, D)
    - Y: labels, shape (N, )
    - b: batch size, shape ()
    
    outputs:
    - x_mini, y_mini: minibatch dataset
    """
    step = len(X) // b
    # yield minibatch for each step
    for indices in np.array_split(np.random.permutation(len(X)), step):
        x_mini, y_mini = X[indices], Y[indices]
        yield x_mini, y_mini
```



### Fully Connected Neural Net

```python
""" layers module"""
class Model:
    # computation graph 
    def __init__(self, H, W, HD, L, beta):
        """
        hyper parameters
        _, H, W = train_x.shape
        HD = 1024 # hidden dimension
        L = 10 # number of labels
        """
        # feed
        self.X = tf.placeholder(dtype=tf.float32, shape=(None, H, W))
        self.Y = tf.placeholder(dtype=tf.int64, shape=(None))
        self.dropout = tf.placeholder(tf.float32)
        
        # helper
        reg = tf.contrib.layers.l2_regularizer(scale=beta)
        init = tf.contrib.layers.xavier_initializer()
        
        with tf.variable_scope("FC", initializer=init, regularizer=reg):
            X = tf.contrib.layers.flatten(self.X)
            dense = tf.contrib.layers.fully_connected(inputs=X, num_outputs=HD, activation_fn=tf.nn.relu)
            # dense = tf.layers.dense(x, L, activation = tf.nn.relu)
            dense = tf.nn.dropout(dense, keep_prob=self.dropout)
            self.logits = tf.contrib.layers.fully_connected(inputs=dense, num_outputs=L, activation_fn=None)
            # self.logits = tf.layers.dense(dense, L, activation=None)

        with tf.variable_scope("loss", initializer=init, regularizer=reg):
            reg_loss = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
            self.loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.Y, logits=self.logits))
            self.loss += tf.reduce_sum(reg_loss) # scalar
            
        # metric
        self.pred = tf.nn.softmax(self.logits)
        correct = tf.nn.in_top_k(predictions=self.logits, targets=self.Y, k=1)
        self.accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))
        
    # train and evaluation  
    def fit(self, config, train_x, train_y, valid_x, valid_y, epoch, lr, b, dr, keep_prob=0.7, 
            save=False, SAVE_FILE='./models_mnist/model', log=False, LOG_DIR='./models_mnist'):
        """
        hyper parameters
        - epoch = 10
        - lr = 0.001
        - b = 150 # minibatch size
        - dr = 0.97 # learning rate decay rate
        - keep_prob = 0.7
        """
        step = tf.get_variable(name="global_step", shape=(), initializer=tf.zeros_initializer(), trainable=False)
        # each decay_step, learning rate will be decreased by decay_rate
        # decayed_learning_rate = learning_rate * decay_rate^(global_step / decay_steps) 
        lr = tf.train.exponential_decay(learning_rate=lr, global_step=step, decay_steps=100, decay_rate=dr, staircase=True)
        optimizer = tf.train.AdamOptimizer(learning_rate=lr).minimize(self.loss, global_step=step)
        
        _, H, W = train_x.shape
        
        # save options 
        saver = tf.train.Saver(var_list=tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES))
        # saver = tf.train.Saver()
        
        # tensorboard visualization
        if log:
            train_loss = tf.get_variable(name='train_loss', shape=(), dtype=tf.float32, initializer=tf.zeros_initializer(), trainable=False)
            valid_acc = tf.get_variable(name='valid_acc', shape=(), dtype=tf.float32, initializer=tf.zeros_initializer(), trainable=False)
            train_loss_summ = tf.summary.scalar('train_loss', train_loss)
            valid_acc_summ = tf.summary.scalar('valid_acc', valid_acc)
            summ_op = tf.summary.merge([train_loss_summ, valid_acc_summ])
        
        with tf.Session(config=config) as sess:
            # initialize all variables 
            sess.run(tf.global_variables_initializer())
            # add graph to tensorboard
            if log:
                print("@terminal: $ tensorboard --logdir={}".format(LOG_DIR))
                writer = tf.summary.FileWriter(LOG_DIR, session=sess)
                writer.add_graph(sess.graph)
            # minibatch training 
            k = 0
            for e in range(epoch):
                loss_train = 0
                for i, xy in tqdm(enumerate(get_minibatch(train_x, train_y, b)), desc='Train'):
                    # minibatch dataset
                    x, y = xy
                    feed = {self.X: x, self.Y: y, self.dropout: keep_prob}
                    loss_mini, _ = sess.run([self.loss, optimizer], feed_dict=feed)
                    loss_train += loss_mini
                loss_train = loss_train / (i+1)
                
                # evaluation
                acc_valid = self.accuracy.eval(feed_dict={self.X: valid_x, self.Y: valid_y, self.dropout: 1})
                print('epoch {} \t| loss: {:.4f} \t| acc_valid: {:.4f} \t| lr: {:0.5} '.format(e+1, loss_train, acc_valid, lr.eval()))
                if log:
                    sess.run([train_loss.assign(loss_train), valid_acc.assign(acc_valid)])
                    summary = sess.run(summ_op)
                    writer.add_summary(summary, global_step=k)
                    k += 1
            print("Training End")
            if save: 
                saver.save(sess, SAVE_FILE)
                print("save model @{}".format(SAVE_FILE))
    # restore model and evaluation
    def test(self, config, test_x, test_y, SAVE_FILE='./models_mnist/model'):
        """
        restore trained weights and evaluate a model
        """
        saver = tf.train.Saver(var_list=tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES))
        # saver = tf.train.Saver()
        
        with tf.Session(config=config) as sess:
            saver.restore(sess, SAVE_FILE)
            print("restore is completed")
            acc_test = self.accuracy.eval(feed_dict={self.X: test_x, self.Y: test_y, self.dropout: 1})
            print("acc_test: {}".format(acc_test))
            
    def summary(self):
        # print("=============================================")
        # print("list of all parameters")
        # print("=============================================")
        # for x in tf.global_variables():
        #     print(x)
        
        print("=============================================")
        print("list of all trainable parameters")
        print("=============================================")
        for x in tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES):
            print(x)
        
        # print("=============================================")
        # print("list of parameters reflected regularization ")
        # print("=============================================")
        # for x in tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES):
        #     print(x)
        
```

#### train and evaluation 

```python
tf.reset_default_graph()
_, H, W = train_x.shape
model = Model(H=H, W=W, HD=1024, L=10, beta=0.1)
model.fit(conf, train_x, train_y, valid_x, valid_y, epoch=10, lr=0.001, b=150, dr=0.97, keep_prob=0.7, save=True, log=True)
model.summary()
model.test(conf, test_x, test_y)
```













