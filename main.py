from get_name_machine import get_uuid_filename
from get_file_output_machine import output_file
from get_tracery_output_machine import get_tracery, get_tracery_list

from aprendizaje import get_rules

## TODO: move this somewhere
def unique(list1): 
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    return unique_list

def drive_fabulas():
  full_grammar = []

  # 1. get file name
  file_name = get_uuid_filename(identifier="./generated/fabulas/final",extension="txt")
  print(file_name)

  # 2. get grammar
  ## 1500 more or less gets you 50k words
  while len(full_grammar) < 1500:
    full_grammar = full_grammar + get_all_seeds_tracery()
  output = "\n\nƸ̵̡Ӝ̵̨̄Ʒ\n\n\n\n\n".join(full_grammar)

  # print(output)
  # 3. output file (fileName, grammar)
  output_file(file_name, output)


def get_all_seeds_tracery():
  full_grammar = []
  seeds = range(0, 13)

  for i in seeds:
    tracery_title = get_tracery_grammar(number=1)[0]
    tracery_title = tracery_title.title()
  
    tracery_list = get_tracery_grammar(rule_key=f"seed{i}")
    tracery_list = [x.capitalize() for x in tracery_list]  
    tracery = "\n\n".join(tracery_list)
    tracery = f"{tracery_title}\n●▬▬▬▬๑۩۩๑▬▬▬▬▬●\n\n\n{tracery}"
    full_grammar.append(tracery)
  return full_grammar


def get_tracery_grammar(rule_key="origin", number=10):
  rules = get_rules()
  tracery_list = get_tracery_list(rules, number=number, rule_key=rule_key)
  tracery_list = unique(tracery_list)
  
  return tracery_list
