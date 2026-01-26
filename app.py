import streamlit as st
import pandas as pd

# タイトル
st.title('各年における漁業産出額')

df = pd.read_csv('漁業産出額.csv')

# サイドバー
# 漁業の種類によってマルチセレクトを変更
with st.sidebar:
    st.subheader('条件の設定')
    type = st.selectbox('漁業の種類を選択してください (複数選択可)',
                          ['海面','内水面','栽培'])
    if type == '海面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['漁船漁業','捕鯨業','海面養殖業'])
        if '漁船漁業' in fish:
            fish = '漁業（海面）'
        elif '捕鯨業' in fish:
            fish = '捕鯨業'
        elif '海面養殖業' in fish:
            fish = '養殖業（海面）'

    elif type == '内水面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['内水面漁業','内水面養殖業'])
        if '内水面漁業' in fish:
            fish = '漁業（内水面）'
        elif '内水面養殖業' in fish:
            fish = '養殖業（内水面）'
    
    elif type == '栽培':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['海面養殖業','内水面養殖業'])
        if '海面養殖業' in fish:
            fish = '海面養殖業'
        elif '内水面養殖業' in fish:
            fish = '内水面養殖業'
    
    # 現状elifでは複数条件を選択しても1つしか条件をしぼれない