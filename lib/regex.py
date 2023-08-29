import re

FINDALL_STRING = """
    It's such a lovely day today.
    Where'd all the time go?
    Some weather we're having today, huh?
    Tomorrow never knows!
    Maybe today's just not my day.
    It's clobbering time!
"""

my_pattern = r"It's such a lovely day today\.|Maybe today's just not my day\.|Some weather we're having today, huh\?"
my_regex = re.compile(my_pattern)
matches = re.findall(my_pattern, FINDALL_STRING)



