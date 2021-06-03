#!/usr/bin/env python3
# -*- coding: utf8 -*-
# -------------------------------------
# Program by Vadim
#
#
# Version    Date   Info
# 1.2        2019   Parser log
# -------------------------------------

import re
from collections import Counter
import csv


def reader(path_to_file):
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    with open(path_to_file, 'r', encoding='utf8') as log_data:
        data_log = log_data.read()
        data_ip_list = pattern.findall(data_log)

    return data_ip_list


def counter_ip(data_ip_list):
    return Counter(data_ip_list)
    pass


def writer_csv(data_ip_dict: dict, out_csv_name: str =None):
    if out_csv_name is None:
        out_csv_name = 'no_name.csv'

    with open(out_csv_name, 'w', encoding='utf8', newline='') as out_csv:
        writer_file = csv.writer(out_csv)
        header = ['ip', 'count']
        writer_file.writerow(header)

        for item in data_ip_dict:
            print((item, data_ip_dict[item]))
            writer_file.writerow((item, data_ip_dict[item]))

        writer_file.writerows([['item', 'data_ip_dict[item]'],
                               ['item', 'data_ip_dict[item]'],
                               ['item', 'data_ip_dict[item]']])
    pass


def main(path_log_file, path_out_csv=None):
    data_list_ip = reader(path_log_file)
    data_dict_ip = counter_ip(data_list_ip)
    writer_csv(data_dict_ip, path_out_csv)


if __name__ == '__main__':
    name_log_file = r'./log_test.txt'
    name_out_csv_file = r'./csv_test.csv'
    main(name_log_file, name_out_csv_file)

