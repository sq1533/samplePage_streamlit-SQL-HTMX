import streamlit

#navigate
pages = {
    "streamlit":[
        streamlit.Page("1.home.py",title="메인 페이지")
    ],
    "backend":[
        streamlit.Page("2.SQL.py",title="SQL"),
        streamlit.Page("3.SQL기본문법.py",title="SQL 기본문법")
    ],
    "frontend":[
        streamlit.Page("4.HTMX.py",title="HTMX")
    ],
    "others":[
        streamlit.Page("5.telegrambotAPI.py",title="telegramBot_API")
    ]
}
streamlit.navigation(pages=pages).run()