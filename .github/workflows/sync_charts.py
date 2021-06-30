import yaml
import os
from git import (Repo, RemoteProgress)
import tarfile
import shutil

class Chart:
  def __init__(self, name, version, source_dir):
    self.name = name
    self.version = version
    self.source_dir = source_dir

  def package_filename(self):
    return self.name + "-" + self.version + ".tgz"
  
  def package_chart(self, target_dir):
    target_file = target_dir + "/" + self.package_filename()
    with tarfile.open(target_file, "w:gz") as tar:
      tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))
      print(target_file + " is created!")

def get_chart(source, path, branch, target_dir):
  if branch: 
    Repo.clone_from(source, target_dir, branch=branch)
  else:
    Repo.clone_from(source, target_dir)

  chart_dir = target_dir + "/" + path
  chart_file = chart_dir + "/Chart.yaml"
  stream = open(chart_file, 'r')
  document = yaml.safe_load(stream)
  return Chart(document['name'], document['version'], chart_dir)

def sync():
  stream = open('charts.yml', 'r')
  try:
    os.mkdir("charts/")
  except FileExistsError:
    pass
  for chart in yaml.safe_load(stream):
    branch = None
    if chart['sync'] == False:
      continue
    if 'branch' in chart:
      branch = chart['branch']
    
    temp_path = "tmp/" + chart['name']
    print('Trying to sync ' + chart['name'])
    chart = get_chart(chart['source'], chart['path'], branch, temp_path)
    shutil.move(chart.source_dir, "charts/" + chart.name)

if __name__ == "__main__":
  sync()