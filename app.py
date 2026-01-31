import streamlit as st
import pandas as pd

# タイトル
st.title('各年における漁業産出額')

df = pd.read_csv('漁業産出額.csv')
df = df.reset_index()
df = df.rename(columns={'index':'年次'})

print(df.head())
print(df.index)
print(df.columns)

# サイドバー
# 漁業の種類によってマルチセレクトを変更
with st.sidebar:
    st.subheader('条件の設定')
    type = st.selectbox('漁業の種類を選択してください (複数選択可)',
                          ['海面','内水面','栽培'])
    if type == '海面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['漁船漁業','捕鯨業','海面養殖業'])
        
        # 選択肢とCSVファイルで使用している名称を対応づける
        mapping = {'漁船漁業':'漁業（海面）',
                   '捕鯨業':'捕鯨業',
                   '海面養殖業':'養殖業（海面）'}
        
        # mappingで変換した名称をリストfishに入れる
        fish = [mapping[f] for f in fish]

    elif type == '内水面':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['内水面漁業','内水面養殖業'])
        mapping = {'内水面漁業':'漁業（内水面）',
                   '内水面養殖業':'養殖業（内水面）'}

        fish = [mapping[f] for f in fish]

    elif type == '栽培':
        fish = st.multiselect('売上を確認したい漁業を選択してください（複数選択可）',
                              ['海面養殖業','内水面養殖業'])
        
        mapping = {'海面養殖業':'養殖業（海面）',
                   '内水面養殖業':'養殖業（内水面）'}
    
        fish = [mapping[f] for f in fish]
   
if fish:
    data = df[['年次'] + ['漁業産出額'] + fish + ['生産漁業所得']]
    st.write("単位：100万円")
    st.dataframe(data)

on = st.toggle('グラフを表示する')
if on:
    st.line_chart(df,x='年次',y='漁業産出額',color={type})