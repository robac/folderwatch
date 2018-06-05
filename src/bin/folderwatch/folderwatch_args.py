#!/usr/bin/python
import sys
import yaml
import os.path


def process_config():
  if (len(sys.argv) < 2):
    raise Exception('Missing path to configuration file!')

  if (not os.path.isfile(sys.argv[1])):
    raise Exception('Configuration file does not exist: ' + sys.argv[1])

  with open(sys.argv[1], 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

  watch_include = '';
  watch_exclude = ''
  for section in cfg['watch']:
    watch_include = watch_include + ' ' + section['source'];
    if ('exclude' in section):
      for item in section['exclude']:
        watch_exclude = watch_exclude + ' --exclude ' + item

  if (len(watch_include) == 0):
    raise Exception('Nothing to watch! Config file: ' + sys.argv[1])

  return (watch_include+watch_exclude)



def main():
  print("inotifywait -r -q -e close_write -m" + process_config())
  return



main()
  

