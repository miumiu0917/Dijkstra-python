# -*- coding: utf-8 -*-
import copy


def _next(m):
  tmp = copy.deepcopy(m)
  _updated = []
  for i, line in enumerate(m):
    for j, element in enumerate(line):
      if element == 'G' or type(element) is int:
        _updated.append(_update(m, i, j))
  if _finish(m, tmp) or not any(_updated):
    return m
  else:
    _next(m)


def _finish(m, tmp):
  _result = False
  for i, line in enumerate(m):
    for j, element in enumerate(line):
      if element == 'S':
        if type(m[i-1][j]) is int or type(m[i+1][j]) is int or type(m[i][j-1]) is int or type(m[i][j+1]) is int:
          _result = True
  return _result



def _update(m, i, j):
  _updated = False
  index = _index(m[i][j])
  if _validate(m, i-1, j, index):
    _updated = True
    m[i-1][j] = index
  if _validate(m, i+1, j, index):
    _updated = True
    m[i+1][j] = index
  if _validate(m, i, j-1, index):
    _updated = True
    m[i][j-1] = index
  if _validate(m, i, j+1, index):
    _updated = True
    m[i][j+1] = index
  return _updated

def _validate(m, i, j, index):
  if m[i][j] in ['*', 'G', 'S']:
    return False
  elif m[i][j] != ' ' and m[i][j] <= index:
    return False
  else:
    return True

def _index(e):
  if e == 'G':
    return 1
  if type(e) is int:
    return e + 1


def _input():
  lines = []
  with open('./data/input.txt') as f:
    for l in f.readlines(): 
      lines.append(list(l.rstrip('\n')))
  return lines

def main():
  m = _input()
  _next(m)
  to_map(m)


def to_map(m):
  for l in m:
    l = list(map(str, l))
    print(''.join(l))

if __name__ == '__main__':
  main()