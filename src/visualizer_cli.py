import argparse

class VisualizerCli():
  filePath: str
  
  def __init__(self):
      parser = argparse.ArgumentParser(description = "")
      parser.add_argument('filePath', type = str)
      
      argument = parser.parse_args()
      
      self.filePath = argument.filePath
