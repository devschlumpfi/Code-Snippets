import pickle

data = {"name": "Alice", "age": 30}
with open("data.pickle", "wb") as file:
    pickle.dump(data, file)

with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)



#This code shows how to serialize and deserialize Python objects using the Pickle module.