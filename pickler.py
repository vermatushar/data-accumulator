import bz2
import pickle

# Saves the "data" with the "title" and adds the .pickle
def full_pickle(title, data):
    with open(title + '.pickle', 'wb') as pikd:
        pickle.dump(data, pikd)

# loads and returns a pickled object
def loosen(file):
    with open(file, 'rb') as pikd:
        data = pickle.load(pikd)
    return data

# Pickle a file and then compress it into a file with extension
def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        pickle.dump(data, f)

# Load the data using the full_pickle function
data = loosen('/Users/kayle/Projects/Python/helloworld/phishingdetection_model.pkl')

# Compress and save the data
compressed_pickle('/Users/kayle/Projects/Python/helloworld/phishingdetection_model.pbz2', data)
