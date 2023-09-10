import torch
import tensorflow as tf

# print(tensorflow.test.is_gpu_available())
# print(torch.cuda.is_available())
#print(torch.version.cuda)
#print(torch.cuda.device_count())
#print(tf.test)
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
print(gpus, cpus)
