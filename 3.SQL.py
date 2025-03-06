import streamlit
import sqlite3

#SQL 예제
streamlit.header(body="SQL 기본문법")
streamlit.code(body="SELECT\nFROM\nWHERE\nORDER BY\nGROUP BY\nHAVING\nLIMIT",language="python")

streamlit.subheader(body="SELECT")
streamlit.code(body="SELECT columns1, columns2\nFROM tableName;")
streamlit.write("""
                특정 테이블 (:blue[FROM tableName])에서 조회할 컬럼(:blue[SELECT columns1, columns2])을 지정합니다.\n
                pandas 표현식 :panda_face: df.loc[:, ['columns1', 'colums2']]
                """)

streamlit.subheader(body="WHERE")
streamlit.code(body="SELECT column1\nFROM tableName\nWHERE column1 LIKE '%test%';")
streamlit.write("""
                'test' 문구가 포함된 조건문 (:blue[WHERE column1 LIKE '%test%']) 작성\n
                pandas 표현식 :panda_face: df[df['columns'].str.contains('test')]
                """)

streamlit.subheader(body="ORDER BY")
streamlit.code(body="SELECT column1\nFROM tableName\nORDER BY column1 ASC;")
streamlit.write("""
                데이터의 오름차순(:blue[ASC]) 또는 내림차순(:blue[DESC]) 정렬을 위해 작성\n
                pandas 표현식 :panda_face: df.sort_values('column1', ascending= True/오름차순 or False/내림차순)
                """)

streamlit.subheader(body="GROUP BY")
streamlit.code(body="SELECT column1\nFROM tableName\nGROUP BY column1;")
streamlit.write("""
                column1 내 동일한 데이터의 그룹화를 진행합니다.(:blue[GROUP BY column1])\n
                pandas 표현식 :panda_face: df.groupby('column1')
                """)