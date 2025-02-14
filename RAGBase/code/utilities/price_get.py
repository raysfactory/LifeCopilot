import pandas as pd
import pickle

# 博多限定の価格予測モデル
# entminute: 最寄り駅からの時間(分)
# entarea: 面積(m2)
def get_price(ent_minute, ent_area) -> float:
    filename = './utilities/ml_model.sav'
    model_load = pickle.load(open(filename, 'rb'))

    df_real_X = pd.DataFrame(columns=['post', 'eki', 'minute', 'mad', 'area', 'born', 'bai'])

    # 特徴量
    df_real_X = df_real_X.append({'post': 7.33236181758308,  #市区町村コード(東京都板橋区)
                                  'eki': 7.38640891866175,   #最寄り駅(志村三丁目)
                                  'minute': ent_minute, #最寄り駅からの時間(分)
                                  'mad': 7.046666262,   #間取り(1K)
                                  'area': ent_area,     #面積
                                  'born': 7.51480344645723,  #建築年(令和3年)
                                  'bai': 7.32274424589367},  #取引時点(2022年)
                    ignore_index=True)

    # 予測
    y_real_pred = model_load.predict(df_real_X)

    # 値の整形
    price_log = y_real_pred[0]
    price = round(10**price_log/10000)*10000
    return price



