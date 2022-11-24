import datetime
import streamlit as st
import pandas_datareader as pdr #pip install pandas_datareader
from cryptocmd import CmcScraper #pip install cryptocmd
import plotly.express as px #pip install plotly-express

st.set_page_config(
    page_title="Investment Research Data",
    page_icon="🤑",
)


st.title("Investment Research Data 🤑")

st.sidebar.success("Select a page above.")

#stock
df = pdr.get_data_yahoo('005930.KS','2020-01-01','2022-11-21')

st.subheader("삼성전자 주식 데이터")
st.write("마감 가격과 거래량을 차트로 보여줍니다.")
st.line_chart(df.Close)
st.line_chart(df.Volume)

st.subheader('비트코인 BTC 데이터')
st.write("마감 가격과 거래량을 차트로 보여줍니다.")


#coin container
c= st.container()
name = c.selectbox('Name',['BTC','ETH','USDT'])

start_Date = c.date_input('Start Date', datetime.date(2022,1,1))
end_Date = c.date_input('End Date', datetime.date(2022,1,7))

#coin
scraper = CmcScraper(name, start_Date.strftime('%d-%m-%Y'),end_Date.strftime('%d-%m-%Y'))

dd = scraper.get_dataframe()

fig_close = px.line(dd, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
fig_volume = px.line(dd, x='Date', y=['Volume'], title='Volume')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)

