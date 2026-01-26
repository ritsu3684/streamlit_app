import streamlit as st
import pandas as pd

# タイトル
st.title('各年における漁業産出額')

df = pd.read_csv('漁業産出額.csv')

# サイドバー
with st.sidebar:
    st.subheader('条件の設定')
    type = st.multiselect('漁業の種類を選択してください (複数選択可)',
                          ['海面','内水面','栽培'])
    if type == '海面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['漁船漁業','捕鯨業','海面養殖業'])
        if fish == '漁船漁業':
            fish = '漁業（海面）'
        elif fish == '捕鯨業':
            fish = '捕鯨業'
        elif fish == '海面養殖業':
            fish = '養殖業（海面）'

    if type == '内水面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['内水面漁業','内水面養殖業'])
        if fish == '内水面漁業':
            fish = '漁業（内水面）'
        elif fish == '内水面養殖業':
            fish = '養殖業（内水面）'
    