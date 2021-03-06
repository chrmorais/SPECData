# Author: Jasmine Oliveira
# Date: 02/16/2017

class Chemical:
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.matched_lines = []

    def add_line(self, line, match):
        self.lines.append(line)
        self.matched_lines.append(match)


class Line:
    def __init__(self, frequency, line_list, units="MHz"):
        self.frequency = frequency
        self.line_list = line_list
        self.units = units


