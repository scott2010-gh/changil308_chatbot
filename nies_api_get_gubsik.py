import requests
import json
import time

class get_gubsik():
    def get(fr,o):
        if o==1:
            data = requests.get("https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=26b53e80dcdf49a2bb93e8e7597861bf&Type=json&pIndex=1&pSize=12&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7051207&MLSV_YMD="+str(fr))
        elif o==2:
            data = requests.get("https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=26b53e80dcdf49a2bb93e8e7597861bf&Type=json&pIndex=1&pSize=12&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7051207&MLSV_YMD="+str(fr[:6]+str(int(fr[6:])+1)))
        else:
            data = requests.get("https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=26b53e80dcdf49a2bb93e8e7597861bf&Type=json&pIndex=1&pSize=12&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7051207&MLSV_FROM_YMD="+str(fr))
        data_dic = data.json()
        outputs=[]
        try:
            if data_dic['RESULT']['CODE']=='INFO-200':
                return "요청 날짜가 주말이거나 급식 정보가 없습니다."
        except:
            pass
        for a in range(int(len(data_dic['mealServiceDietInfo'][1]['row']))):
            YMD=data_dic['mealServiceDietInfo'][1]['row'][a]['MLSV_YMD']
            outputs.append('['+YMD[:4]+'-'+YMD[4:6]+'-'+YMD[6:8]+']\n'+data_dic['mealServiceDietInfo'][1]['row'][a]['DDISH_NM'].replace('<br/>','\n'))
        return '\n\n\n'.join(outputs)
