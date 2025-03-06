import streamlit
import pandas
import random

#streamlit 기능 및 데이터 시각화
streamlit.title(body=":green[든든동규] 개발 온몸비틀기")
streamlit.subheader(body=":red[streamlit] 데이터 시각화")
streamlit.divider()

#그래프_비즈
streamlit.header(body="그래프_비즈")
streamlit.graphviz_chart(
    """
    digraph {
    fullstack -> frontend
    fullstack -> backend
    frontend -> tailwindcss
    frontend -> HTMX
    tailwindcss -> UX,UI
    HTMX -> AJAX
    HTMX -> APIserver
    backend -> Fast_API
    Fast_API -> APIserver
    Rest_API -> Fast_API
    APIserver -> HTMX
    APIserver -> DataBase
    DataBase -> APIserver
    }
    """
)
streamlit.divider()

#심플 차트(Area)
if 'chartArea_value' not in streamlit.session_state:
    streamlit.session_state['chartArea_value'] = [random.sample(range(100),10), random.sample(range(100),10)]

if 'chartAreaColorA' not in streamlit.session_state:
    streamlit.session_state['chartAreaColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

if 'chartAreaColorB' not in streamlit.session_state:
    streamlit.session_state['chartAreaColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

#샘플 데이터
AreaExemple = pandas.DataFrame({'sampleA':streamlit.session_state['chartArea_value'][0],'sampleB':streamlit.session_state['chartArea_value'][1]})

streamlit.header(body="차트(Area)")
streamlit.area_chart(
    data=AreaExemple,
    x=None,
    y=None,
    x_label="randomData",
    y_label=None,
    color=[streamlit.session_state['chartAreaColorA'],streamlit.session_state['chartAreaColorB']],
    stack=True,
    height=None,
    width=None,
    use_container_width=True
)
left, middle, right = streamlit.columns(3)
if left.button(label='dataShuffle',key='chartAreaData'):
    streamlit.session_state['chartArea_value'] = [random.sample(range(100),10), random.sample(range(100),10)]
    streamlit.rerun()
if middle.button(label='AcolorShuffle',key='chartAreaAcolor'):
    streamlit.session_state['chartAreaColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
if right.button(label='BcolorShuffle',key='chartAreaBcolor'):
    streamlit.session_state['chartAreaColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
streamlit.divider()

#심플 차트(Bar)
if 'chartBar_value' not in streamlit.session_state:
    streamlit.session_state['chartBar_value'] = [random.sample(range(100),10), random.sample(range(100),10)]

if 'chartBarColorA' not in streamlit.session_state:
    streamlit.session_state['chartBarColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

if 'chartBarColorB' not in streamlit.session_state:
    streamlit.session_state['chartBarColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

#샘플 데이터
BarExemple = pandas.DataFrame({'sampleA':streamlit.session_state['chartBar_value'][0],'sampleB':streamlit.session_state['chartBar_value'][1]})

streamlit.header(body="차트(Bar)")
streamlit.bar_chart(
    data=BarExemple,
    x=None,
    y=None,
    x_label="randomData",
    y_label=None,
    color=[streamlit.session_state['chartBarColorA'],streamlit.session_state['chartBarColorB']],
    horizontal=False,
    stack=True,
    height=None,
    width=None,
    use_container_width=True
)
left, middle, right = streamlit.columns(3)
if left.button(label='dataShuffle',key='chartBarData'):
    streamlit.session_state['chartBar_value'] = [random.sample(range(100),10), random.sample(range(100),10)]
    streamlit.rerun()
if middle.button(label='AcolorShuffle',key='chartBarAcolor'):
    streamlit.session_state['chartBarColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
if right.button(label='BcolorShuffle',key='chartBarBcolor'):
    streamlit.session_state['chartBarColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
streamlit.divider()

#심플 차트(Line)
if 'chartLine_value' not in streamlit.session_state:
    streamlit.session_state['chartLine_value'] = [random.sample(range(100),10), random.sample(range(100),10)]

if 'chartLineColorA' not in streamlit.session_state:
    streamlit.session_state['chartLineColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

if 'chartLineColorB' not in streamlit.session_state:
    streamlit.session_state['chartLineColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

#샘플 데이터
BarExemple = pandas.DataFrame({'sampleA':streamlit.session_state['chartLine_value'][0],'sampleB':streamlit.session_state['chartLine_value'][1]})

streamlit.header(body="차트(Line)")
streamlit.line_chart(
    data=BarExemple,
    x=None,
    y=None,
    x_label="randomData",
    y_label=None,
    color=[streamlit.session_state['chartLineColorA'],streamlit.session_state['chartLineColorB']],
    height=None,
    width=None,
    use_container_width=True
)
left, middle, right = streamlit.columns(3)
if left.button(label='dataShuffle',key='chartLineData'):
    streamlit.session_state['chartLine_value'] = [random.sample(range(100),10), random.sample(range(100),10)]
    streamlit.rerun()
if middle.button(label='AcolorShuffle',key='chartLineAcolor'):
    streamlit.session_state['chartLineColorA'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
if right.button(label='BcolorShuffle',key='chartLineBcolor'):
    streamlit.session_state['chartLineColorB'] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
    streamlit.rerun()
streamlit.divider()