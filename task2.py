# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


remote_addresses = {}


def check_address(address):
    global remote_addresses
    if remote_addresses.get(address) is None:
        remote_addresses[address] = 1
    else:
        address_value = remote_addresses[address]
        remote_addresses[address] = address_value + 1


with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        check_address(line.split()[0])

max_requests = 0
spamer_address = ''
for key, val in remote_addresses.items():
    if val > max_requests:
        max_requests = val
        spamer_address = key

print(f"Адрес спамера - {spamer_address}, количество запросов  - {max_requests}")
