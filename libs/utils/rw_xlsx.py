#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 
# @Author  : Mik


import xlrd
from libs.utils.base_path import base_path


class ReadExcel():
    def __init__(self):
        """打开工作表"""
        data_address = base_path + r'\data\webdata.xlsx'
        workbook = xlrd.open_workbook(data_address)
        self.table = workbook.sheet_by_index(0)

    def get_rows_column(self):
        rows = self.table.nrows
        col = self.table.ncols
        return rows, col

    def get_rowdata(self, rowx):
        """
        获取一行的数据
        :param row: 传入行数从0开始
        :return: 这一行的数据
        """
        row = self.table.row_values(rowx)
        return row

    def get_coldata(self, colx):
        """
        获取一列的数据
        :param col: 传入列数从0开始
        :return: 这一列的数据
        """
        loc = self.table.col_values(colx)
        return loc

    def get_celldata(self, cellx):
        """
        获取单元格数据
        :param cellx: 元组类型的行和列
        :return: 数据
        """
        cell = self.table.cell_value(*cellx)
        return cell


# e = ReadExcel()
# e1 = e.get_rowdata(1)
# print(e1,type(e1))
