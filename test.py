# import StringIO
# import xlsxwriter
# from django.http import HttpResponse
#
# def export_page(request):
#     # create our spreadsheet.  I will create it in memory with a StringIO
#     output = StringIO.StringIO()
#     workbook = xlsxwriter.Workbook(output)
#     worksheet = workbook.add_worksheet()
#     worksheet.write('A1', 'Some Data')
#     workbook.close()
#
#     # create a response
#     response = HttpResponse(content_type='application/vnd.ms-excel')
#
#     # tell the browser what the file is named
#     response['Content-Disposition'] = 'attachment;filename="some_file_name.xlsx"'
#
#     # put the spreadsheet data into the response
#     response.write(output.getvalue())
#
#     # return the response
#     return response