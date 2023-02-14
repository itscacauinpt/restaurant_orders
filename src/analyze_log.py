import csv
from collections import Counter

def read_path_to_file(path_to_file):
    logs = []
    menu = []
    week = []

    with open(path_to_file, newline='') as file:
        lines = csv.reader(file)

        for line in lines:
            logs.append({'name': line[0], 'order_info': (line[1], line[2])})

            if line[1] not in menu:
                menu.append(line[1])
            
            if line[2] not in week:
                week.append(line[2])

    return logs, menu, week


def write_file(path_to_file, info):
    # print(info)
    content = "\n".join([str(data) for data in info])

    with open(path_to_file, "w") as file:
        file.write(content)


def get_marias_orders_info(logs):
    maria_stuff = []

    for log in logs:
        if log['name'] == 'maria':
            maria_stuff.append(log['order_info'][0])

    return Counter(maria_stuff).most_common(1)[0][0]


def get_arnaldo_orders_info(logs):
    arnaldo_stuff = []

    for log in logs:
        if log['name'] == 'arnaldo':
            arnaldo_stuff.append(log['order_info'][0])
    
    return arnaldo_stuff.count('hamburguer')


def get_joao_orders_info(logs_info):
    logs = logs_info[0]
    menu = logs_info[1]
    week = logs_info[2]
    joao_dish = ''
    joao_day = ''

    for log in logs:
        if log['name'] == 'joao':
            if log['order_info'][0] in menu:
                joao_dish = log['order_info'][0]

            if log['order_info'][1] in week:
                joao_day = log['order_info'][1]
    
    return (
        {dish for dish in menu if dish != joao_dish},
        {day for day in week if day != joao_day}
    )


def analyze_log(path_to_file):
    '''
    Qual o prato mais pedido por 'maria'?
    Quantas vezes 'arnaldo' pediu 'hamburguer'?
    Quais pratos 'joao' nunca pediu?
    Quais dias 'joao' nunca foi à lanchonete?
    '''

    if 'csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    
    try:
        info = []

        logs_info = read_path_to_file(path_to_file)

        info.append(get_marias_orders_info(logs_info[0]))
        info.append(get_arnaldo_orders_info(logs_info[0]))
        info.append(get_joao_orders_info(logs_info)[0])
        info.append(get_joao_orders_info(logs_info)[1])

        # return info
        write_file("data/mkt_campaign.txt", info)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

print(analyze_log('data/orders_1.csv'))
