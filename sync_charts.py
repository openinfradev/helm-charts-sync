import yaml

stream = open('charts.yml', 'r')
for data in yaml.load_all(stream, Loader = yaml.FullLoader):
  print(data)

