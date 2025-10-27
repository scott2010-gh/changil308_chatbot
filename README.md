# 일정파일 경로 설정
##### schedule.py는 server_main.py에서 작성된 일정 json 파일을 해석하는데 이용되므로 경로가 반드시 수정되어야 합니다.
schedule.py 및 schedule_editor.py의 "dr" 변수를 수정합니다. 이때 경로는 해당 파일의 전체 경로를 사용해야 합니다.</br> 
#### ex) /home/user_name/server-files/main/schedule_data.dat
schedule_editor은 json파일을 쉽게 수정하기 위한 gui 프로그램이므로 경로를 수정하지 않아도 됩니다.

### 일정 json파일 형식
['YYYY/MM/DD':'schedule_data']</br>

*중간/기말과 같은 일정의 경우에는 key와 value을 뒤집어 입력하며, key에는 중간 또는 기말이 입력됩니다.</br>
['중간':'중간고사 날짜']

# 컴시간 데이터 요청
comsigan.py는 selenium 기반으로 작동되며, server_main.py는 comsigan_http_request.py를 사용합니다.</br>
http 요청은 3학년 8반 기준으로 설정되어 있으므로 다른 시간표를 가져오려면 http 요청 주소를 변경해야 합니다.

# 서버 실행하기
### uvicorn 및 ngrok을 이용한 실행
