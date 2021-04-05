# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
# информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
# <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

RE_PARSE = re.compile(r'((?:\d+.)+).*\[(.+)\].{2}(\w+)\s(.+) .+(\d{3})\s(\d+)')


with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    for line in f:
        parsed_raw = RE_PARSE.match(line)
        if parsed_raw:
            print(parsed_raw.groups())
        else:
            raise Exception('Check your re')


# Если я правильно понял вопрос, то беру одну строку из файла и работаю с ней, поэтому ограничился одной строкой
# Особенными во время решения оказались строки, в которых response_size длиннее одного символа, поэтому пришлось
# подкорректировать. И ещё не совсем пока разобрался с различием между \s и просто пробелом, объясните пожалуйста,
# а так же поставил '?:', но так и не разобрался до конца, как работает эта штука