#!/usr/bin/python

#
# Copyright 2018 Chris Cartland
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from random import choice


def qotd():
  output = ''
  NEWLINE = '<br />\n'

  with open('name.txt', 'r') as n:
    name = n.read().strip()
    if len(name) > 0:
      output += NEWLINE + name

  with open('quotes.txt', 'r') as f:
    quotes = [quote.strip() for quote in f.readlines() if len(quote.strip()) > 0]
    if len(quotes) > 0:
      quote = choice(quotes)
      output += NEWLINE + quote

  return output


if __name__ == '__main__':
  print(qotd())

