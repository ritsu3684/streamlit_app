import streamlit as st
import pandas as pd
import altair as alt

# タイトル
st.title('各年における漁業産出額')

df = pd.read_csv('漁業産出額.csv',na_values=['未計測'],skipinitialspace=True)
df.columns = df.columns.str.strip()
# 選択肢になり得るすべての列を数値型に変換
cols_to_convert = ['漁業産出額', '漁業（海面）', '捕鯨業', '養殖業（海面）', 
                   '漁業（内水面）', '養殖業（内水面）', '生産漁業所得']

for col in cols_to_convert:
    if col in df.columns:
        # カンマを取り除き、数値に変換。変換できないものはNaN（欠損値）にする
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

# グラフのX軸用に「西暦」を数値として抽出
df['西暦'] = df['年次'].str.extract('(\d{4})').astype(float)
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
if on :
    if fish:
        # Altair用にデータを縦長に変換
        chart_data = df.melt(id_vars=['西暦'], value_vars=fish)

        chart = alt.Chart(chart_data).mark_line().encode(
            x=alt.X('西暦:Q', title='年'),
            y=alt.Y('value:Q', 
                    title='産出額 (100万円)',
                    scale=alt.Scale(domain=[1960, 2023])), # ここで [最小, 最大] を指定！
            color='variable:N'
        )

        st.altair_chart(chart, use_container_width=True)
        st.write(df[fish].head())