#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlsxwriter


def export_results(users,results,found):
    # var's of excel
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    i = 0
    try:

        print "Exporting the results in an excel"
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, "Users hacked")
        worksheet.write(row, col + 1, "Status")
        worksheet.write(row, col + 2, "Results")
        row += 1
        # Iterate over the data and write it out row by row.
        for user in users:
            col = 0
            worksheet.write(row, col, user)
            worksheet.write(row, col + 1, found[i])
            worksheet.write(row, col + 2, results[i])
            row += 1
            i += 1
        # close the excel
        workbook.close()

    except Exception as e:
        print "Exception in export_results " + str(e)
