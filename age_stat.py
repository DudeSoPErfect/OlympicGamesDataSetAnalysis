import pandas as pd
import os
import matplotlib.pyplot as plt
from sex_stat import years_data_frames

# статистика возраста участников по годам

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def create_correct_age_dataframe(yearsDataFrames, years):                                                               # создаем корректный датасет для статистики возраста участников за все года

    ageDataFrame = pd.DataFrame()

    underTwenty            = []
    betweenTwentyAndThirty = []
    betweenThirtyAndForty  = []
    betweenFortyAndFifty   = []
    overFifty              = []

    prettyData             = []                                                                                         # используем, как промежуточный элемент, который хранит у нас данные в более удобном формате
    for i in range(len(yearsDataFrames)):
        k = yearsDataFrames[i]['Age'].value_counts()                                                                    # pandas не всегда удобно представляет автоматически подсчитанные данные, переделаем.
        frame = pd.DataFrame()

        x = k.index
        y = k.values
        frame['Age']   = x
        frame['count'] = y
        prettyData.append(frame)

        underTwenty.append(prettyData[i]           [lambda x:  x['Age'] <= 20]['count'].sum())                          # заполним списки со значениями соответствующих возрастов
        betweenTwentyAndThirty.append(prettyData[i][lambda x: (x['Age'] >  20) * (x['Age'] <= 30)]['count'].sum())
        betweenThirtyAndForty.append(prettyData[i] [lambda x: (x['Age'] >  30) * (x['Age'] <= 40)]['count'].sum())
        betweenFortyAndFifty.append(prettyData[i]  [lambda x: (x['Age'] >  40) * (x['Age'] <= 50)]['count'].sum())
        overFifty.append(prettyData[i]             [lambda x:  x['Age'] >  50]['count'].sum())

    ageDataFrame['years']  = years                                                                                       # заполним соответствущие датафреймы
    ageDataFrame['<=20']   = underTwenty
    ageDataFrame['21-30']  = betweenTwentyAndThirty
    ageDataFrame['>31-40'] = betweenThirtyAndForty
    ageDataFrame['>41-50'] = betweenFortyAndFifty
    ageDataFrame['>50']    = overFifty

    return ageDataFrame



def age_data_graphs(ageDataFrame):                                                                                      # сохраним все в директорию

    ageDataFrame.plot(x = "years", y = ["<=20", "21-30", ">31-40", ">41-50", ">50"])
    try:
        os.mkdir(os.getcwd() + '\\age_data')
    except FileExistsError:
        pass
    os.chdir(os.getcwd() + '\\age_data')
    plt.savefig('age_data_graph.png')
    ageDataFrame.to_excel('age_data_stat.xlsx')                                                                         # на всякий случай сохраним статистику
    os.chdir('..')

    return 0


#-----------------------------------------------------------------------------------------------------------------------

def age_stat(data):                                                                                                     # родитель

    yearsDataFrames, years = years_data_frames(data)
    ageDataFrame = create_correct_age_dataframe(yearsDataFrames, years)
    age_data_graphs(ageDataFrame)
    print('age statistic prepared!')

    return 0
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
