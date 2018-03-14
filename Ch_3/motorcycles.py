motorcycles = ['suzuki', 'yamaha', 'honda']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('harley')
print(motorcycles)
motorcycles = []
print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('harley')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)
motorcycles = []
motorcycles.insert(0, 'yamaha')
motorcycles.insert(1, 'suzuki')
motorcycles.insert(2, 'ducati')
motorcycles.insert(3, 'harley')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)