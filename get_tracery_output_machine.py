import tracery
from tracery.modifiers import base_english
# import pycorpora


def get_tracery(rules: object, rule_key:str="origin") -> str:
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    sentence = grammar.flatten('#%s#' % rule_key)

    return sentence

def get_tracery_list(rules: object, rule_key:str="origin", number=1) -> list:
  traceries = list()
  for i in range(number):
    tracery = get_tracery(rules, rule_key)
    traceries.append(tracery)
  return traceries
