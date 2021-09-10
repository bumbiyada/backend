import xlwings as xw
print('type filename with .xlsx or any other *.')
file_name = str(input())
wb = xw.Book(file_name)


# something magic
app = xw.apps.active


ws = wb.sheets["TDSheet"]
last_row = ws.range(1, 1).end('down').row

ws.range((1, 1), (last_row, 1)).insert()
ws.range(1, 1).value = 'id'
""" HEHEHE """
print('renaming columns')
if ws.range(1, 6).value == 'Месяц':
    ws.range((1, 6), (last_row, 6)).delete()
ws.range(1, 2).value = 'Foiv'
ws.range(1, 3).value = 'Document_type'
ws.range(1, 5).value = 'Document_number'
ws.range(1, 4).value = 'Document_init_data'
ws.range(1, 7).value = 'Stage_name'
ws.range(1, 6).value = 'Stage_data'
ws.range(1, 8).value = 'Stage_user'
ws.range(1, 9).value = 'Is_aborted'
ws.range(1, 10).value = 'State'
ws.range(1, 11).value = 'Marked_on_delete'
""" HOHOHO """
ws.range((1, 9), (last_row, 9)).insert()
ws.range(1, 9).value = 'User_department'
print('handle True and False')
for i in range(2, last_row + 1, 1):
    # ws.range(i,1).value = i - 1

    # print(i % 10)
    # временно рандомит отдел челикам от 1 до 10
    ws.range(i, 9).value = i % 10
    print(ws.range(i, 9).value)

    if ws.range(i, 12).value == "Нет":
        ws.range(i, 12).value = 0
    elif ws.range(i, 12).value == "Да":
        ws.range(i, 12).value = 1
    else:
        ws.range(i, 12).value = ''
    if ws.range(i, 10).value == 'Нет':
        ws.range(i, 10).value = 0
    elif ws.range(i, 10).value == 'Да':
        ws.range(i, 10).value = 1
    else:
        ws.range(i, 10).value = ''
    if ws.range(i, 11).value == 'Нет':
        ws.range(i, 11).value = 102
    elif ws.range(i, 11).value == 'Да':
        ws.range(i, 11).value = 408
    else:
        ws.range(i, 11).value = ''
wb.save('completed.xlsx')
# wb.close()


# something magic (2)
app.quit()


print('completed!')
