 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml




with open("bernadotte.yaml") as f:
    family = yaml.load(f)



pprint(family)