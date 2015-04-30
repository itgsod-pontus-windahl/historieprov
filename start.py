 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml




with open("bernadotte.yaml") as f:
    family = yaml.load(f)



pprint(family)


# -*- coding: utf-8 -*-
#from pprint import pprint
import yaml


with open("bernadotte.yaml") as f:
    family=yaml.load(f)

    #for name in sorted(f):
        #print name


for name in family['bernadotte']['barn'][0]:
    print name




