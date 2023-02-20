import os
import pandas as pd

# выделим топ-3 страны по медалям за каждый год

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def little_other_years_data_frames(data):                                                                               # создаем список из датафреймов всех годов немного иначе
    years     = list(sorted(list(set(data['Year'].values))))
    countries = list(sorted(list(set(data['Team'].values))))
    yearsDataFrames = []
    for year in years:
        mask = data['Year'] == year
        yearsDataFrames.append(data[mask])

    return yearsDataFrames, years, countries


def isNaN(num):

    return num != num                                                                                                   # проверяем число на NaN для корректности


def save_data(bestCountries, years):                                                                                    # сохраняем
    try:
        os.mkdir(os.getcwd() + '\\country_data')
    except FileExistsError:
        pass
    os.chdir(os.getcwd() + '\\country_data')

    nYears = len(years)
    for i in range(nYears + 1):
        curFrame = pd.DataFrame()
        curFrame['Country'] = [bestCountries[i][j][0] for j in range(3)]
        curFrame['Gold']    = [bestCountries[i][j][1] for j in range(3)]
        curFrame['Silver']  = [bestCountries[i][j][2] for j in range(3)]
        curFrame['Bronze']  = [bestCountries[i][j][3] for j in range(3)]
        curFrame['nMedals'] = [bestCountries[i][j][4] for j in range(3)]

        if i == nYears:
            curFrame.to_excel('bestOfTheBest.xlsx')
        else:
            curFrame.to_excel(str(years[i]) + '.xlsx')

    os.chdir('..')
    print('Done!')
    return 0


def select_top3_countries_in_year(curDataFrame, countries):                                                             # выбираем топ 3 страны по количеству медалей в году year

    countries_sorted_by_n_medals = {name: [name, 0, 0, 0, 0] for name in countries}
    GOLD, SILVER, BRONZE = 1, 2, 3
    NMEDALS = 4

    medals, teams = curDataFrame['Medal'].values, curDataFrame['Team'].values
    nItems        = len(curDataFrame)


    for item in range(nItems):
        if not isNaN(medals[item]):
            if medals[item]   == 'Gold':
                countries_sorted_by_n_medals[teams[item]][GOLD]  += 1
            elif medals[item] == 'Silver':
                countries_sorted_by_n_medals[teams[item]][SILVER] += 1
            else:
                countries_sorted_by_n_medals[teams[item]][BRONZE] += 1

            countries_sorted_by_n_medals[teams[item]][NMEDALS] += 1

    countries_sorted_by_n_medals = list(countries_sorted_by_n_medals.values())
    countries_sorted_by_n_medals = sorted(countries_sorted_by_n_medals, key=lambda x: x[NMEDALS], reverse=True)

    best_countries = []

    for i in range(3):
        best_countries.append(countries_sorted_by_n_medals[i])

    return best_countries


#-----------------------------------------------------------------------------------------------------------------------

def top3_counties_each_year(data):                                                                                      # родитель
    yearsDataFrames, years, countries = little_other_years_data_frames(data)
    nYears = len(years)

    bestCountries = []
    for nYear in range(nYears):
        bestCountries.append(select_top3_countries_in_year(yearsDataFrames[nYear], countries))

    bestCountries.append(select_top3_countries_in_year(data, countries))

    save_data(bestCountries, years)

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

