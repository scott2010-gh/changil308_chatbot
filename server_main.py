import time
import schedule
import nies_api_get_gubsik
import nies_api_get_academy
import schedule
import comsigan_http_request
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import datetime

global options,loading

ymd=str(time.localtime()[0])+str(time.localtime()[1])+str(time.localtime()[2])
ytd=datetime.date(int(ymd[:4]),int(ymd[4:6]),int(ymd[6:8]))

#fastAPI 시작
app = FastAPI()

@app.post("/")
async def handle_simple_request(request: Request):
    try:
        req_data: Dict[str, Any] = await request.json()
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid JSON format"}
        )
    #print(req_data)
    user_utterance = req_data.get('userRequest', {}).get('utterance', '')
    loading = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "불러오는중입니다.. \n서버 상황에 따라 지연될 수 있습니다."
                }
            }
        ]
    }
}
    res_text = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "null"
                }
            }
        ]
    }
}
    res_img = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl":"null",
                    "altText":"null"
                    }
            }
        ]
    }
}  
    loop=1
    if "오늘" in user_utterance and "날짜"in user_utterance:
        res="오늘은 "+str(time.localtime()[1])+"월 "+str(time.localtime()[2])+"일 입니다 :)"
    elif "안녕" in user_utterance:
        res="안녕하세요! 저는 학교관련 정보들을 제공하는 일정봇입니다."
    elif "라이언" in user_utterance:
        res=0
    elif "이미지 테스트" in user_utterance:
        res=1
    elif "큰글자 테스트" in user_utterance:
       res='ㄱ'+'\u200d'
    elif "오늘" in user_utterance and "급식"in user_utterance:
        res=nies_api_get_gubsik.get_gubsik.get(ymd,1)
    elif "내일" in user_utterance and "급식"in user_utterance:
        n=ytd+datetime.timedelta(1)
        res=nies_api_get_gubsik.get_gubsik.get(str(n.year)+str(n.month)+str(n.day),1)
    elif "급식"in user_utterance:
        res=nies_api_get_gubsik.get_gubsik.get(ymd,False)
    elif "일정"in user_utterance and not "시험일정"in user_utterance:
        res=schedule.schedule.get_list(0)
    elif "디데이"in user_utterance or "시험일정"in user_utterance:
        res="기말까지 :\n"+str(schedule.schedule.get_dday(0,1))+"일 남음!!!"
    elif "시간표" in user_utterance and not "오늘" in user_utterance:
        res=comsigan_http_request.chr.get(3,8)
    elif "오늘" in user_utterance and "시간표" in user_utterance:
        res=comsigan_http_request.chr.get_week(3,8,time.localtime().tm_wday+1)
    elif "도움말" in user_utterance:
        res="안녕하세요! 저는 창일봇(beta 1.3)입니다.\n다음과 같은 명령어들을 사용하실 수 있습니다.\n\n{학교 관련 명령어}\n'일정' - 학교 일정을 나열합니다\n\n'급식' - 불러오기 가능한 전체 급식 목록을 나열합니다.\n\n'오늘 급식' - 오늘 급식 메뉴를 출력합니다.\n\n'내일 급식' - 내일 급식 메뉴를 나열합니다\n\n'디데이'/'시험일정' - 시험까지 남은 시간을 출력합니다.\n\n'시간표' - 시간표를 불러옵니다(변경된 시간표 확인 가능)\n\n{테스트용 명령어}\n'오늘 날짜' - 서버 시간 기준 오늘 날짜를 출력합니다.\n'안녕' - 챗봇이 인사를 합니다.\n'이미지 테스트' - 테스트 이미지를 출력합니다.\n'라이언' - 라이언 이미지를 출력합니다.\n\n*이 챗봇은 웹 스크롤링을 통해 사이트에서 정보를 가져오므로 특정 응답에 최대 5초 정도의 시간이 소요될 수 있습니다.\n\n*개선할점 제안과 버그 제보는 다음 링크를 사용해주세요.\nhttps://forms.gle/2zxVFkfj6KGwMLTb7"
    elif "학원검색" in user_utterance:
        res=nies_api_get_academy.get_academies.get(user_utterance[5:user_utterance.index(',')],user_utterance[user_utterance.index(',')+1:-1])
    else:
        res="(이해 못함)"
    if type(res)==int:
        if res==0:
            res_img["template"]["outputs"][0]["simpleImage"]["imageUrl"]="https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2018%2F10%2Fkakao-talk-2018-1.jpeg?q=75&w=800&cbr=1&fit=max"
            res_img["template"]["outputs"][0]["simpleImage"]["altText"]="발 담구는 라이언"
        if res==1:
            res_img["template"]["outputs"][0]["simpleImage"]["imageUrl"]="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLZf31OpU0zqzpDS-IwNBp7lF1eejh9YJHHA&s"
            res_img["template"]["outputs"][0]["simpleImage"]["altText"]="HELLO WORLD!!!"
        return JSONResponse(content=res_img)
    else:
        res_text["template"]["outputs"][0]["simpleText"]["text"]=str((res+"\n")*(loop-1)+res)
        return JSONResponse(content=res_text)
    

