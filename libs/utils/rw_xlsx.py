#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 
# @Author  : Mik


import xlrd
import openpyxl
from libs.utils.base_path import root_dir


class ReadExcel():
    def __init__(self, index=0):
        """
        打开工作表
        :param index: 传入表号，默认为0
        """
        data_address = root_dir + r'\data\webdata.xlsx'
        workbook = xlrd.open_workbook(data_address)
        self.table = workbook.sheet_by_index(index)
        self.row_max1 = self.table.nrows
        self.col_max1 = self.table.ncols

    def get_sheet_info(self):
        """
        获取表信息
        :return: 名字，行数，列数
        """
        name = self.table.name
        row = self.table.nrows
        col = self.table.ncols
        return name, row, col

    def get_row(self, rowx):
        """
        获取一行的数据
        :param row: 传入行数从0开始
        :return: 这一行的数据
        """
        row = self.table.row_values(rowx)
        return row

    def get_rows(self, min, max):
        """
        获取指定行的数据
        :param min: 传入开始行，从0开始
        :param max: 传入结束行
        :return: 选择读取数据
        """
        rows = []
        for i in range(min, max):
            rows.append(self.get_row(i))
        return rows

    def get_cols(self, min, max):
        """
        获取指定列的数据
        :param min: 传入开始列，从0开始
        :param max: 传入结束列
        :return: 选择读取数据
        """
        cols = []
        for i in range(min, max):
            cols.append(self.get_row(i))
        return cols

    def get_col(self, colx):
        """
        获取一列的数据
        :param col: 传入列数从0开始
        :return: 这一列的数据
        """
        loc = self.table.col_values(colx)
        return loc

    def get_cell(self, cellx):
        """
        获取单元格数据
        :param cellx: 元组类型的行和列
        :return: 数据
        """
        cell = self.table.cell_value(*cellx)
        return cell


class WriteExcel():
    def __init__(self, sheet='Sheet1'):
        """
        打开工作表
        :param sheet: 传入工作表名
        """
        self.data_address = root_dir + r'\data\webdata.xlsx'
        self.book = openpyxl.load_workbook(self.data_address)
        self.bs = self.book.get_sheet_by_name(sheet)

    def write_call(self, cellx, val):
        """
        按单元格写入数据
        :param cellx: 传入单元格地址，列入A1
        :param val: 传入写入值
        :return: None
        """
        self.bs[cellx] = val

    def write_row(self, val):
        """
        按行在末尾逐行写入数据
        :param val: 列表数据类型
        :return: None
        """
        self.bs.append(val)

    def save_book(self):
        self.book.save(self.data_address)


# e = ReadExcel()
# print(e.row_max1, type(e.row_max1))
# e1 = e.get_rows(0, e.row_max1)
# print(e1, type(e1))
#
# w=WriteExcel()
# w.write_call('A1','WWWWWWWWW')
# w.save_book()