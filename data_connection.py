#!/usr/bin/env python
# encoding: utf-8

import struct


class DataConnection:

    def __init__(self):
        self.data_file = open("./db-2.db", "rb")

        self.reading_file()

    def reading_file(self):

        self.positioning_cursor_of_begin_file()

        dict_fields_head = self.reading_fields_head()

        number_all_records_of_file = self.number_all_records_of_file()

        dict_fields_and_datas = {}
        for each_line in range(number_all_records_of_file):

            for each_fields in range(0, self.number_fields):
                field_and_byte = dict_fields_head.items()[each_fields]
                field = field_and_byte[0]
                byte = field_and_byte[1]

                if each_fields == 0:
                    flag = self.reading_fields_binary(1)

                data = self.reading_fields_string(byte)
                dict_fields_and_datas[field] = data

    def positioning_cursor_of_begin_file(self):
        self.data_file.seek(0, 2)
        self.size_all_file = self.data_file.tell()
        self.data_file.seek(0)

    def reading_fields_head(self):
        dict_fields = {}

        magic_cookie = self.reading_fields_binary(4)
        self.total_each_record = self.reading_fields_binary(4)[3]
        self.number_fields = self.reading_fields_binary(2)[1]

        for i in range(0, self.number_fields):

            size_name_of_field = self.reading_fields_binary(2)
            name_of_field = self.reading_fields_string(size_name_of_field[-1])[0]
            size_of_field_bytes = self.reading_fields_binary(2)[1]

            dict_fields[name_of_field] = size_of_field_bytes

        return dict_fields

    def number_all_records_of_file(self):
        size_all_of_head = self.data_file.tell()

        number_lines_of_file = (self.size_all_file - size_all_of_head)/self.total_each_record

        return number_lines_of_file

    def reading_fields_binary(self, number_of_bytes):

        return struct.unpack(str(number_of_bytes) + 'B', self.data_file.read(number_of_bytes))

    def reading_fields_string(self, number_of_bytes):

        return struct.unpack(str(number_of_bytes) + 's', self.data_file.read(number_of_bytes))


if __name__ == '__main__':

    try:
        DataConnection()

    except Exception as e:
        print e
