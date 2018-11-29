#!/usr/bin/python3

import yaml

def configparse(Variable):

  with open('config.yml', 'r') as yml:
    YMLConfig = yaml.load(yml)
    
    YMLValue = YMLConfig[Variable]

    return YMLValue
