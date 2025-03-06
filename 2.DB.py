import streamlit

#DB
streamlit.header(body="DB")

#간단한 이커머스 DB 구축
streamlit.write("""
                데이터베이스 기획 및 구축에 대한 이해를 돕기위해, 기초적인 이커머스 DB구축을 진행하겠다.\n
                DB기획\n\n
                
                - login\n
                회원ID : INDEX : str(04~08 영문, 숫자 조합) / 무결성 / 유일성\n
                회원PW : column[passward] : str(08~20 영문, 숫자, 허용된 특수문자 조합) + 후추 / 암호화\n
                권한1 : column[authority_1] : bools (ex. 상품 등록, 수정, 삭제 권한 == 일반 회원 False)\n
                권한2 : column[authority_2] : bools (ex. 회원 등급, 권한부여, 블랙리스트 등록 등)\n
                권한3 : column[authority_3] : bools (ex. 회원 정보 수정)\n
                - 회원 정보\n
                회원ID : INDEX(login[회원ID] 접근시 허용)\n
                회원정보 : column[info] : str (name, 생년월일, 전화번호 등)\n
                회원등급 : column[class] : int (ex. 01-프리미엄, 02-골드, 03-실버)\n
                포인트 : column[point] 56000 : int\n
                검색기록 : column[lookup] ['컵','gtx5000','노트북', ...] : list(str)_10\n
                방문상품 : column[visit] [30006545,30006437,40002237,20001203,20001204] : list(int)_5 / 상품코드\n
                구입상품 : column[buy] [20001203,20001204,30000033,90001889, ...] : list(int) / 상품코드\n
                사용금액 : column[used] [100,300,400,1600,0, ...] : list(int)\n
                결제수단 : column[method] ['card','account','kakaopay','point', ...] : list(str)\n
                - 회원등급표\n
                등급 : INDEX : int\n
                할인 : column[discount] : int\n
                적립 : column[collect] : int\n\n

                - 상품\n
                상품코드 : INDEX : int(카테고리 구분 4 + 상품고유 코드 4) (ex. 20003242, 70001312)\n
                상품이름 : column[itemName] : str\n
                상품가격 : column[itemCost] : int\n
                상품할인율 : column[itemDiscount] : int (최종 가격 == 상품가격*(상품할인율/100) 3f.0 올림)\n
                event : column[event] : list(int) (프로모션 코드 ex. [001,003])\n
                """)