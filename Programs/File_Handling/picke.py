import pickle

file = open("picke.txt", "rb")

print(pickle.load(file))
# pickle.dump({1:2}, file)

file.close()