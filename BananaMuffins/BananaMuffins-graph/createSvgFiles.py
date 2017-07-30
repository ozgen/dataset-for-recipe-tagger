from subprocess import call
import os



def getSvgFile(filename):
  split = os.path.splitext(filename)
  call(['dot', '-Tsvg', filename, '-o', split[0] + '.svg'])



if __name__ == '__main__':
  file_list = os.listdir('.')
  for f in file_list:
    if f.endswith('.gv'):
      print f
      getSvgFile(f)
