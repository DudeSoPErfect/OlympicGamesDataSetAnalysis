import pandas as pd
import os
import matplotlib.pyplot as plt
# статистика пола участников по годам

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def years_data_frames(data):                                                                                            # создаем список из датафреймов всех годов

    years = list(sorted(list(set(data['Year'].values))))
    yearsDataFrames = []
    for year in years:
        mask = data['Year'] == year
        yearsDataFrames.append(data[mask])

    return yearsDataFrames, years


def sex_data_from_year(year):                                                                                           # возвращаем статистику по каждому полу за конкретный год

    return year['Sex'].value_counts().to_frame()


def exception_handling_add_column(arr, data, column, string):                                                           # когда мы составляем корректную модель столбца датасета, может оказаться такое, что данных
                                                                                                                        # к которым мы попытаемся получить доступ по индексу, просто не существует.
    try:                                                                                                                # Обработаем это исключение
        arr.append(int(data[column][string]))
    except KeyError:
        arr.append(0)

    return arr


def create_correct_sex_dataframe(yearsDataFrames, years):                                                               # создаем корректный датасет для статистики пола за все года

    sexDataFrame = pd.DataFrame()
    maleNumbers   = []
    femaleNumbers = []
    for year in range(len(yearsDataFrames)):

        dataFromYear  = sex_data_from_year(yearsDataFrames[year])

        maleNumbers   = exception_handling_add_column(maleNumbers, dataFromYear, 'Sex', 'M')

        femaleNumbers = exception_handling_add_column(femaleNumbers, dataFromYear, 'Sex', 'F')

    sexDataFrame['Year'] = years
    sexDataFrame['M']    = maleNumbers
    sexDataFrame['F']    = femaleNumbers

    return sexDataFrame


def sex_data_graphs(sexDataFrame):                                                                                      # строим график и сохраняем в директорию

    sexDataFrame.plot(x = "Year", y = ["M", "F"])
    try:
        os.mkdir(os.getcwd() + '\\male_female_data')
    except FileExistsError:
        pass
    os.chdir(os.getcwd() + '\\male_female_data')
    plt.savefig('male_female_graph.png')
    sexDataFrame.to_excel('male_female_data_stat.xlsx')                                                                 # на всякий случай сохраним статистику
    os.chdir('..')

    return 0

#-----------------------------------------------------------------------------------------------------------------------

def male_female_participants_stat(data):                                                                                # родитель

    yearsDataFrames, years = years_data_frames(data)
    sexDataFrame = create_correct_sex_dataframe(yearsDataFrames, years)
    sex_data_graphs(sexDataFrame)
    print('male/female statistic prepared!')

    return 0

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
