from math import isnan, nan
import pandas as pd


def try_float(x):
    try:
        return float(x)
    except:
        return nan


df = pd.read_csv('datasets/Full_Mark_2020.csv')


# Ép kiểu cho cột Vatli, vì có 1 row có dữ liệu ko hợp lệ nên phải dùng cách này
df['Vatli'] = df['Vatli'].apply(try_float)


# Code,Diali,GDCD,Hoahoc,KHTN,KHXH,LichSu,Ngoaingu,Nguvan,Sinhhoc,Toan,Vatli,city,tongdiem

df['TongDiem'] = df['Diali'].apply(lambda x: x if not isnan(x) else 0) \
    + df['GDCD'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Hoahoc'].apply(lambda x: x if not isnan(x) else 0)\
    + df['LichSu'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Ngoaingu'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Nguvan'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Sinhhoc'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Toan'].apply(lambda x: x if not isnan(x) else 0)\
    + df['Vatli'].apply(lambda x: x if not isnan(x) else 0)

df['TongSoMonThi'] = df['Diali'].apply(lambda x: 1 if not isnan(x) else 0) \
    + df['GDCD'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Hoahoc'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['LichSu'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Ngoaingu'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Nguvan'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Sinhhoc'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Toan'].apply(lambda x: 1 if not isnan(x) else 0)\
    + df['Vatli'].apply(lambda x: 1 if not isnan(x) else 0)

df['DiemTrungBinh'] = df['TongDiem'] / df['TongSoMonThi']


def all_greater_than_or_equal(obj, diem):
    if(not isnan(obj['Diali']) and obj['Diali'] < diem):
        return False

    if(not isnan(obj['GDCD']) and obj['GDCD'] < diem):
        return False

    if(not isnan(obj['Hoahoc']) and obj['Hoahoc'] < diem):
        return False

    if(not isnan(obj['LichSu']) and obj['LichSu'] < diem):
        return False

    if(not isnan(obj['Ngoaingu']) and obj['Ngoaingu'] < diem):
        return False

    if(not isnan(obj['Nguvan']) and obj['Nguvan'] < diem):
        return False

    if(not isnan(obj['Sinhhoc']) and obj['Sinhhoc'] < diem):
        return False

    if(not isnan(obj['Toan']) and obj['Toan'] < diem):
        return False

    if(not isnan(obj['Vatli']) and obj['Vatli'] < diem):
        return False

    return True


df['XepLoai'] = 'rot'

for i, row in df.iterrows():
    # if isnan(row['KHTN']) and isnan(row['KHXH']):
    #     continue

    if not all_greater_than_or_equal(row, 1):
        # df.at[i, 'XepLoai'] = 'rot'
        continue

    if (row['DiemTrungBinh'] < 5):
        # df.at[i, 'XepLoai'] = 'rot'
        continue

    if row['DiemTrungBinh'] >= 8 and all_greater_than_or_equal(row, 7):
        df.at[i, 'XepLoai'] = 'gioi'
        continue

    if row['DiemTrungBinh'] >= 6.5 and all_greater_than_or_equal(row, 6):
        df.at[i, 'XepLoai'] = 'kha'
        continue

    df.at[i, 'XepLoai'] = 'trungbinh'

df.to_csv('datasets/Extended_Full_Mark_2020.csv', index=False)
