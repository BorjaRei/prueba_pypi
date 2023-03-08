from tinto_prueba.methods import tinto
data="C:\\Users\\borja\\PycharmProjects\\prueba_pypi\\Datasets\\iris.csv"
folder="C:\\Users\\borja\\PycharmProjects\\prueba_pypi\\res"
t=tinto(data,folder)
t.generateImages()