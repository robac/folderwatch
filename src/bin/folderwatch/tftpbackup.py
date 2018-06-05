#!/usr/bin/python
import sys
import os
import os.path
import time
import syslog
import logging
import logging.handlers
import MySQLdb
import yaml
import math




class Config():
  start_time = 0
  log = None
  service_name = ''
  log_address = ''
  src_dir = ''
  src_basedir = ''
  dst_basedir = ''
  raise_event = ''
  event = ''
  filename = ''
  src_path = ''
  dst_path = ''
  use_mysql = False
  max_filesize = 0
  mysql_host = ''
  mysql_db = ''
  mysql_port = 3306
  mysql_user = ''
  mysql_pwd = ''
  mysql_table = ''
  mysql_insert = ''
 



def is_subdirectory(child, parent):
  child = os.path.normpath(child)
  parent = os.path.normpath(parent)
  if (child == parent):
    return True
  if (len(child) < (len(parent)+1)):
    return False
  return (os.path.join(parent,child[len(parent)+1:]) == child)


def process_config(config):
  if (not os.path.isfile(sys.argv[1])):
    raise Exception('Configuration file does not exist: ' + sys.argv[1])

  with open("/etc/tftpwatch.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

  config.log_address = cfg['general']['log_address'];
  config.use_mysql = cfg['general']['use_mysql']

  if (config.use_mysql):
    config.mysql_host = cfg['mysql']['host']
    config.mysql_db = cfg['mysql']['db']
    if ('port' in cfg['mysql']):
      config.mysql_port = cfg['mysql']['port']
    config.mysql_user = cfg['mysql']['user']
    config.mysql_pwd = cfg['mysql']['password']
    config.mysql_table = cfg['mysql']['table']
    config.mysql_insert = cfg['mysql']['insert_command']
 
  config.service_name = cfg['general']['service_name']
 
  section_exists = False;
  for section in cfg['watch']:
    if (is_subdirectory(sys.argv[2], section['source'])):
      config.src_basedir = section['source'];
      config.dst_basedir = section['destination']
      config.max_filesize = section['max_filesize']
      config.raise_event = section['event']
      section_exists = True;
      break

  if (not section_exists):
    raise Exception('No section for directory: ' + sys.argv[2])   

  return  


def configure_logging(config):
  config.log = logging.getLogger(__name__)
  config.log.setLevel(logging.INFO)
  handler = logging.handlers.SysLogHandler(address = config.log_address)
  formatter = logging.Formatter(config.service_name + ': %(message)s')
  config.log.addHandler(handler)
  handler.setFormatter(formatter)
  config.log.addHandler(handler)

  

def check_arguments():
  if (len(sys.argv) < 5):
    raise Exception('Invalid number of parameters: ' + str(len(sys.argv) - 1))
    sys.exit()



def create_dst_filename(config):
  milisec = str(int(math.floor((config.start_time - math.floor(config.start_time)) * 1000)))
  while (len(milisec) < 3):
    milisec = '0'+milisec

  suffix = time.strftime('%y%m%d%H%M%S', time.localtime((config.start_time))) + milisec
  return (config.filename + '.' + suffix)



def process_arguments(config):
  config.src_dir = sys.argv[2]
  config.event = sys.argv[3]
  config.filename = sys.argv[4]

  events = config.event.split(',')
  if (not config.raise_event in events):
    config.log.warning('Exiting. Not an desired event: ' + event)
    sys.exit()

  config.src_path = os.path.join(config.src_dir, config.filename)

  if (not os.path.isfile(config.src_path)):
    config.log.warning('Exiting. Not a file: ' + config.src_path)
    sys.exit()

  if (config.max_filesize < os.path.getsize(config.src_path)):
    config.log.warning('Exiting. File size exceeds limit: ' + config.src_path + '. Limit: ' + str(config.max_filesize) + ' Size: ' + str(os.path.getsize(config.src_path)))
    sys.exit()

  rel_path = os.path.relpath(config.src_dir, config.src_basedir)
  config.dst_path = os.path.normpath(os.path.join(config.dst_basedir, rel_path, create_dst_filename(config)))
  return



def write_db(config):
  db = MySQLdb.connect(host = config.mysql_host, 
                       user = config.mysql_user, 
                       passwd = config.mysql_pwd,
		       port = config.mysql_port,
                       db = config.mysql_db)

  cur = db.cursor()
  command = config.mysql_insert.format(config.mysql_table,
                           	       os.path.basename(config.src_path),
		           	       os.path.basename(config.dst_path), 
	                               os.path.normpath(os.path.dirname(config.src_path)),
		      	               os.path.normpath(os.path.dirname(config.dst_path)),
				       os.path.getsize(config.dst_path))
  config.log.info(command) 
  cur.execute(command)
  db.commit()
  db.close()
  return


def move_file(config):
  dst_dir = os.path.dirname(config.dst_path)
  if (not os.path.isdir(dst_dir)):
    config.log.info('Trying to create directory: ' + dst_dir)
    os.makedirs(dst_dir)

  config.log.info('Trying to move file ' + config.src_path + ' to ' + config.dst_path)
  os.rename(config.src_path, config.dst_path)
  return


def main():
  config = Config()
  config.start_time = time.time();
  
  check_arguments()
  process_config(config)

  configure_logging(config)
  process_arguments(config)
  move_file(config)
  if (config.use_mysql):
    write_db(config)
  return


main()








