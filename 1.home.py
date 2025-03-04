import streamlit
import pandas
import random

#streamlit 기능 및 데이터 시각화
streamlit.title(body=":green[든든동규] 개발 온몸비틀기")
streamlit.subheader(body=":red[streamlit] 데이터 시각화")
#그래프_비즈
streamlit.header(body="그래프_비즈")
streamlit.graphviz_chart(
    """
    digraph {
    fullstack -> backend
    backend -> SQL
    backend -> NoSQL
    backend -> Restfull_API
    SQL -> PostgreSQL
    NoSQL -> MongoDB
    fullstack -> frontend
    frontend -> HTMX
    frontend -> tailwindcss
    HTMX -> Restfull_API
    HTMX -> HTML
    HTMX -> CDN
    tailwindcss -> CDN
    }
    """
)
streamlit.divider()

#샘플 데이터
A = random.sample(range(100),10)
B = random.sample(range(100),10)
exemple = pandas.DataFrame({'sampleA':A,'sampleB':B})

#심플 차트(Area)
streamlit.header(body="차트(Area)")
chart, DataFrame = streamlit.columns(spec=[2,1],gap='small',vertical_alignment='center')
DataFrame.dataframe(data=exemple,hide_index=True)
chart.area_chart(
    data=exemple,
    x=None,
    y=None,
    x_label="sampleData_A",
    y_label="sampleData_B",
    color=[(0,0,255),(0,255,0)],
    stack=True,
    height=None,
    width=None,
    use_container_width=True
)
streamlit.divider()