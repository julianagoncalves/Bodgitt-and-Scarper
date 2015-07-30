#!/usr/bin/env python
# encoding: utf-8

import struct


class DataConnection:

    def __init__(self):
        self.data_file = open("./db-2.db", "rb")

        self.reading_file()

    def reading_file(self):

        self.positioning_cursor_begin_file()

        self.list_fields_head = self.reading_fields_head()

        self.number_all_records_of_file = self.number_all_records_of_file()

        list_fields_and_datas = self.going_each_record_file()

    def going_each_record_file(self):
        list_fields_and_datas = []
        for each_records in range(self.number_all_records_of_file):
            list_datas = []
            for each_fields in range(0, self.number_fields):
                field_and_byte = self.list_fields_head[each_fields]
                name_field = field_and_byte[0]
                byte = field_and_byte[1]

                if each_fields == 0:
                    byte_flag = self.reading_fields_binary(1)

                data = self.reading_fields_string(byte)
                data = ''.join(data).strip()

                list_datas.append(name_field)
                list_datas.append(data)

            list_fields_and_datas.append(list_datas)

        return list_fields_and_datas

    def positioning_cursor_begin_file(self):
        self.data_file.seek(0, 2)
        self.size_all_file = self.data_file.tell()
        self.data_file.seek(0)

    def reading_fields_head(self):
        list_fields = []

        magic_cookie = self.reading_fields_binary(4)
        self.total_each_record = self.reading_fields_binary(4)[3]
        self.number_fields = self.reading_fields_binary(2)[1]

        for i in range(0, self.number_fields):

            size_name_of_field = self.reading_fields_binary(2)
            name_of_field = self.reading_fields_string(size_name_of_field[1])[0]
            size_of_field_bytes = self.reading_fields_binary(2)[1]

            list_fields.append((name_of_field, size_of_field_bytes))

        return list_fields

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
