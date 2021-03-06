from NeuralNetwork import NeuralNetwork
from featureExtractor import FeatureExtractor
import numpy as np
from DataLoader import DataLoader
import configure


# (learningRate, noOfEpochs, noOfHidNeur, noOfEigenValues)
configure.setUpConfig(0.05, 500, 100, 100)
fe = FeatureExtractor("generatedData/eigenfaces.csv", "generatedData/average_face.csv")

#prepare data for training:
dl = DataLoader(configure.config_global.modeTrain)
dl.load_all_images()
datasetTrain = fe.generate_dataset(dl.images)

#train NN:
nn = NeuralNetwork(configure.config_global.noOfEigenValues, configure.config_global.noOfHidNeur)
nn.trainNetwork(datasetTrain)

#prepare data for testing:
dl = DataLoader(configure.config_global.modeTest)
dl.load_all_images()
dataset = fe.generate_dataset(dl.images)

#classification:
output_guess = []
for sample in dataset:
    desired = sample[-1]
    calculated = nn.classify(np.transpose(np.asmatrix(sample[:-1])))
    output_guess += [desired == calculated]

print("testing data result:", sum(output_guess)/np.shape(dataset)[0])

#prepare data for training data results:
dl = DataLoader(configure.config_global.modeTrain)
dl.load_all_images()
dataset = fe.generate_dataset(dl.images)


output_guess = []
for sample in dataset:
    desired = sample[-1]
    calculated = nn.classify(np.transpose(np.asmatrix(sample[:-1])))
    output_guess += [desired == calculated]

print("training data result: ", sum(output_guess)/np.shape(dataset)[0])
