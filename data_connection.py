#!/usr/bin/env python
# encoding: utf-8

import struct


class DataConnection:

    def __init__(self):
        
        file_name = "./db-2.db"
        self.data_file = open(file_name, "rb")

        self.reading_file()

    def reading_file(self):

        self.data_file.seek(0,2)
        self.data_file.seek(0) 

        self.magic_cookie = self.reading_fields_binary(4)
        self.total_each_record = self.reading_fields_binary(4)
        self.number_fields = self.reading_fields_binary(2)

        self.reading_fields()
        
    def reading_fields(self):
        dict_file = {}
        
        for i in range(0,self.number_fields[1]):

            size_name_of_field = self.reading_fields_binary(2)
            name_of_field = self.reading_fields_string(size_name_of_field[-1])
            size_of_field_bytes = self.reading_fields_binary(2)

            dict_file[name_of_field[0]] = size_of_field_bytes[1]

        return dict_file

    def reading_fields_binary(self, number_of_bytes):

       return struct.unpack(str(number_of_bytes) + 'B', self.data_file.read(number_of_bytes))
    
    def reading_fields_string(self, number_of_bytes):

       return struct.unpack(str(number_of_bytes) + 's', self.data_file.read(number_of_bytes))


if __name__ == '__main__':

    try:
        DataConnection()

    except Exception as e:
        print e

