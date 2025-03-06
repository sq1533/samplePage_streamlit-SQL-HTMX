import streamlit

#tigger
streamlit.write("""
                ##### HTMX_trigger
                기본 html의 동작을 세밀하게 조정 가능하게 한다.
                """)
streamlit.write("hx-trigger:every 설정된 간격으로 요청을 가능하게 한다.")
streamlit.code(body=
                """
                #매 2초마다 'path/data'로 get요청을 보낸다.
                <div hx-get:'path/data' hx-trigger:'every:2s'><div>
                """)
streamlit.divider()

#AJAX
streamlit.write("""
                ##### HTMX_AJAX get / post / put / patch / delete
                HTMX를 이용하여 AJAX 수행이 가능하다.
                """)
streamlit.write("hx-patch -> 데이터의 일부 수정을 위한 patch 요청")
streamlit.code(body=
                """
                <form hx-patch='/patchData' hx-target='#output' hx-swap='innerHTML'>
                    <input type='text' name='inputText'>
                    <button type='submit'>전송</button>
                </form>
                <div id='output'></div>
                """)
streamlit.write("""
                이해를 돕기위해 backend API서버는 Fast API로 구축한다.\n
                HTMX의 patch요청을 받아 fastapi 및 SQL문법을 통해 처리
                """)
streamlit.code(body=
                """
                from fastapi import FastAPI, Request
                from fastapi.responses import HTMLResponse
                import sqlite3

                app = FastAPI()

                @app.patch("/patchData/{id}")
                async def patch_data(id:int,request:Request)
                    conn = sqlite3.connect(DB)
                    cursor = conn.cursor()
                    data = await request.form()
                    input = data['inputText']
                    cursor.excute(
                            '''
                            UPDATE tableName
                            SET item = ?
                            WHERE item_id = ?
                            ''',
                            (input,id))
                    return HTMLResponse(content='<div>수정완료</div>')
                """)
streamlit.divider()