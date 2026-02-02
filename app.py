import streamlit as st
import pandas as pd

# タイトル
st.title('各年における漁業産出額')

df = pd.read_csv('漁業産出額.csv',na_values=['未計測'],skipinitialspace=True)
df.columns = df.columns.str.strip()

# グラフのX軸用に「西暦」を数値として抽出
df['西暦'] = df['年次'].str.extract('(\d{4})').astype(int)

fish = []

# サイドバー
# 漁業の種類によってマルチセレクトを変更
with st.sidebar:
    st.subheader('条件の設定')
    
    type = st.segmented_control(
        '漁業の種類',
        ['海面','内水面','栽培'],
        key = 'fish_type',
        selection_mode='single'
    )

    if type == '海面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['漁船漁業','捕鯨業','海面養殖業'])
        
    elif type == '内水面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['内水面漁業','内水面養殖業'])

    elif type == '栽培':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['海面養殖業','内水面養殖業'])
        
if type and fish:
    data = df[['年次'] + ['漁業産出額'] + fish + ['生産漁業所得']]
    st.write("単位：100万円")
    st.write(f'漁業の種類：{type}漁業')
    st.dataframe(data,hide_index=True)
    st.line_chart(df,x='西暦',y=fish)

elif type is None:
    st.info('サイドバーから漁業の種類を選択してください')

st.link_button('使用したデータのあるサイトへ移動','https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&toukei=00500208&bunya_l=04&tstat=000001015664&cycle=7&tclass1=000001034725&tclass2val=0')

a_mapping = [':material/thumb_down:',':material/thumb_up:']
selected = st.feedback('thumbs')
