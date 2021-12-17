import tensorflow as tf


def get_data(validation_datasize) :
    mnist=tf.keras.datasets.mnist
    (X_train_full,Y_train_full),(X_test,Y_test)=mnist.load_data()
    X_valid, X_train = X_train_full[:validation_datasize] / 255., X_train_full[validation_datasize:] / 255.
    Y_valid, Y_train = Y_train_full[:validation_datasize], Y_train_full[validation_datasize:]
    ## scale the test as well
    X_test = X_test / 255.

    return(X_train,Y_train),(X_valid,Y_valid),(X_test,Y_test)