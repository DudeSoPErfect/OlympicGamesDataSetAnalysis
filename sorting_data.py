import os
from   pandas import ExcelWriter

# сортировки

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def save_sorted(data, param):
    try:
        os.mkdir(os.getcwd() + '\\sorted_by_' + param)
    except FileExistsError:
        pass
    os.chdir(os.getcwd() + '\\sorted_by_' + param)

    writer = ExcelWriter(param + '.xlsx')
    data.to_excel(writer, param)
    writer.save()

    os.chdir('..')
    print('sorted ' + param + ' data prepared!')

    return 0

def sort_by(data, param):
    data = data.sort_values(param)
    save_sorted(data, param)

    return 0

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



