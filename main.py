import pandas as pd
from set_options   import setPandasDisplayOptions
from sex_stat      import male_female_participants_stat
from age_stat      import age_stat
from sorting_data  import sort_by
from top_countries import top3_counties_each_year


# кодстайл:
# составные переменные: без пробелов; нижний регистр первого слова; верхний регистр остальных слов;
# составные функции: пробелы заменены на "_"; полный нижний регистр
# вспомогательные функции выделены отдельно со своими родителямми


def main():

    file = 'athlete_events.csv'
    data = pd.read_csv(file)
    setPandasDisplayOptions()


    age_stat(data)
    male_female_participants_stat(data)

    sort_by(data, 'Age')
    sort_by(data, 'Height')
    sort_by(data, 'Weight')

    top3_counties_each_year(data)

if __name__ == '__main__':
    main()

