import requests
import json

class get_academies():
    def get(wr,nm):
        try:
            data = requests.get("https://open.neis.go.kr/hub/acaInsTiInfo?KEY=26b53e80dcdf49a2bb93e8e7597861bf&Type=json&pIndex=1&pSize=12&ATPT_OFCDC_SC_CODE=B10&ADMST_ZONE_NM="+str(wr)+"&ACA_NM="+str(nm))
            data_dic = data.json()
            outputs=[]
            outputs.append('[ 검색 결과 ]\n')
            for a in range(int(len(data_dic['acaInsTiInfo'][1]['row']))):
                outputs.append("이름: "+data_dic['acaInsTiInfo'][1]['row'][a]['ACA_NM']+'\n주소: '+data_dic['acaInsTiInfo'][1]['row'][a]['FA_RDNDA']+'\n전화번호: '+data_dic['acaInsTiInfo'][1]['row'][a]['FA_TELNO'])

            return '\n\n\n'.join(outputs)
        except:
            return "서버오류[500]\n나이스 api에서 해당 내용을 찾지 못했습니다.\n정확한 학원명 또는 지역명인지 확인하세요"

        
