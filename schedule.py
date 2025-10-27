import datetime

#아래 경로를 일정이 저장될 json 파일 경로로 설정하시오
dr="/home/radxa/server-files/main/schedule_data.dat"
class schedule():
    def get_list(self):
        try:
            global dr
            data = open(dr,'r',encoding='UTF8')
            data2 = eval(data.readline())
            data.close()
            out_list=[]
            for r in data2.keys():
                if not str(r)=='기말' or str(r)=='중간' :
                    out_list.append(str(r)+' : '+data2[r]+'\n')
            return ''.join(out_list)
            
        except:
            return("Internal_server_error[500]\nschedule_data_not_found")
    def get_dday(self,test_code):
        try:
            global dr
            data = open(dr,'r',encoding='UTF8')
            data2 = eval(data.readline())
            data.close()
            n=datetime.datetime.now()
            if test_code==0:
                ymd=data2['중간'].split('/')
            else:
                ymd=data2['기말'].split('/')
            return((datetime.date(int(ymd[0]),int(ymd[1]),int(ymd[2]))-datetime.date(n.year,n.month,n.day)).days)
        except:
            return("Internal_server_error[500]\nschedule_data_not_found")

