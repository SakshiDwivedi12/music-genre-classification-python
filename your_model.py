import numpy as np
import scipy.io.wavfile as wav
from python_speech_features import mfcc
import pickle
import operator

def classify_genre(audio_file):
    def distance(instance1, instance2, k):
        mm1, cm1 = instance1[0], instance1[1]
        mm2, cm2 = instance2[0], instance2[1]
        dist = np.trace(np.dot(np.linalg.inv(cm2), cm1))
        dist += (np.dot(np.dot((mm2-mm1).transpose(), np.linalg.inv(cm2)), mm2-mm1))
        dist += np.log(np.linalg.det(cm2)) - np.log(np.linalg.det(cm1))
        dist -= k
        return dist
        
    def getNeighbors(trainingset, instance, k):
        distances = []
        for x in range(len(trainingset)):
            dist = distance(trainingset[x], instance, k) + distance(instance, trainingset[x], k)
            distances.append((trainingset[x][2], dist))
        distances.sort(key=operator.itemgetter(1))
        return [distances[x][0] for x in range(k)]
        
    def nearestclass(neighbors):
        classVote = {}
        for response in neighbors:
            classVote[response] = classVote.get(response, 0) + 1
        return sorted(classVote.items(), key=operator.itemgetter(1), reverse=True)[0][0]

    # डेटा लोड करना
    dataset = [] 
    try:
        with open("my.dat", 'rb') as f:
            while True:
                try:
                    dataset.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        return "Error: my.dat file not found!"

    if not dataset:
        return "Error: Dataset is empty!"

    # Genre mapping
    results = {1:"blues", 2:"classical", 3:"country", 4:"disco", 5:"hiphop", 
               6:"jazz", 7:"metal", 8:"pop", 9:"reggae", 10:"rock"}

    try:
        (rate, sig) = wav.read(audio_file)
        mfcc_feat = mfcc(sig, rate, winlen=0.020, appendEnergy=False)
        covariance = np.cov(np.matrix.transpose(mfcc_feat))
        mean_matrix = mfcc_feat.mean(0)
        feature = (mean_matrix, covariance, 0)
        
        # Prediction using KNN neighbors
        neighbors = getNeighbors(dataset, feature, 5)
        pred = nearestclass(neighbors)
        return results.get(pred, "Unknown")
    except Exception as e:
        return f"Error: {str(e)}"