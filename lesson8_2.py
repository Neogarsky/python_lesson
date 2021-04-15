import re


with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    log_str = f.read()


PARSE = r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$'
parse_txt = list(re.findall(PARSE, log_str, re.MULTILINE))
print(*parse_txt, sep='\n')

log_lst = log_str.split('\n')
print(f'log_str lines:  {len(log_lst)}\n'   
      f'RE_PARSE lines: {len(parse_txt)}')

for line in log_str.split('\n'):
    parse_str = re.findall(PARSE, line)
    if not parse_str:
        print(f'Строка которую не удалось распарсить: ({line})')