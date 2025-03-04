import streamlit

streamlit.header(body="HTMX")

streamlit.subheader(body="tigger")
streamlit.code()

streamlit.subheader(body="AJAX처리 get / post / put / patch / delete")
streamlit.write("""
                ###### AJAX_patch
                일부 수정이 필요한 요청 처리
                """)
streamlit.code(body=
                """
                <head>
                <script src="https://unpkg.com/htmx.org@2.0.4/dist/htmx.min.js"></script>
                <head>
                <body>
                    <form hx-patch='/patchData' hx-target='#output' hx-swap='innerHTML'>
                        <input type='text' name='inputText'>
                        <button type='submit'>전송</button>
                    </form>
                    <div id='output'></div>
                </body>
                """)
streamlit.write("""
                이해를 돕기위해 backend는 Fast API로 작성.\n
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
                    data = await request.form()
                    input = data['inputText']
                    conn = sqlite3.connect(DB)
                    cursor = conn.cursor()
                    cursor.excute(
                            '''
                            UPDATE tableName
                            SET item = ?
                            WHERE item_id = ?
                            ''',
                            (input,id))
                    return HTMLResponse(content='<div>수정완료</div>')
                """)
