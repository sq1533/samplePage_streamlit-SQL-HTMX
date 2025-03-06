import streamlit

#navigate
pages = {
    "streamlit":[
        streamlit.Page("1.home.py",title="메인 페이지")
    ],
    "backend":[
        streamlit.Page("2.DB.py",title="DataBase"),
        streamlit.Page("3.SQL.py",title="SQL")
    ],
    "frontend":[
        streamlit.Page("4.HTMX.py",title="HTMX")
    ],
    "others":[
        streamlit.Page("5.telegrambotAPI.py",title="telegramBot_API")
    ]
}
streamlit.navigation(pages=pages).run()