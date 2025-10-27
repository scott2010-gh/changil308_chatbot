#컴시간 http 요청
import requests
import json


class chr:
    def get(grade,class_num):
        wl = ['월','화','수','목','금']
        source = requests.get('http://222.106.100.23:4082/36179?NzM2MjlfMjUyMTRfMF8x')
        source.encoding='UTF-8'
        data = source.text
        f = open('save.json','w')
        f.write(data[:data.index('}')+1])
        f.close()
        f = open('save.json','r')
        c = json.load(f)
        f.close()
        o_list = []
        n=0
        for a in c['자료147'][grade][class_num][1:]:
            o_list.append('---'+wl[n]+'---\n')
            for b in a[1:]:
                if b==0:
                    return ''.join(o_list)
                if len(str(b))==5:
                    o_list.append(c['자료492'][int(str(b)[:3])//10]+'\n')
                else:
                    o_list.append(c['자료492'][int(str(b)[:2])//10]+'\n')
            n+=1
            if n!=5:
                o_list.append('\n\n')
        return ''.join(o_list)
    def get_week(grade,class_num,dotw):
        if dotw>5 or dotw<1:
            return "서버오류[500]\n입력된 요일은 시간표 요청이 불가합니다"
        wl = ['월','화','수','목','금']
        source = requests.get('http://222.106.100.23:4082/36179?NzM2MjlfMjUyMTRfMF8x')
        source.encoding='UTF-8'
        data = source.text
        f = open('save.json','w')
        f.write(data[:data.index('}')+1])
        f.close()
        f = open('save.json','r')
        c = json.load(f)
        f.close()
        o_list = []
        o_list.append('[ '+str(wl[dotw-1])+'요일 시간표 ]\n')
        for a in c['자료147'][grade][class_num][dotw][1:]:
            if a==0:
                return ''.join(o_list)
            if len(str(a))==5:
                o_list.append(c['자료492'][int(str(a)[:3])//10]+'\n')
            else:
                o_list.append(c['자료492'][int(str(a)[:2])//10]+'\n')
        return ''.join(o_list)
