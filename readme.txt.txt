pip install -r spotify_requirments.txt
vsCode 에서 app.py 실행

postman 아니면 insomnia 사용
app/ app.py , model/ model.py에 DB 연결

서버 시작 app.py 실행
시간이 좀 걸림, 콘솔창 확인

restful    -> Create_user_table = 임의의 유저 데이터 DB table 생성
	-> insert_Dummydata = 랜덤의 노래를 유저 데이터 DB table에 삽입 지금은 한곡 들어감
	-> Recommand_Data = 임의의 노래 DB에 노래를 가져오고, 알고리즘 돌려서 노래 추출해서 추천 DB에 저장 (한곡)

※ popularity라고 인기도 수치가 있는데 현재 50 이상만 추출됨 - 인기도수치가 적으면 유튜브에서도 검색 안되는 것도 있음
   50이상은 거의 다 검색 됨.

