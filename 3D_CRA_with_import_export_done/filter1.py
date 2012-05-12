from db_code import get_db_session
from models import *
import insert
from commands import *
dbsession = get_db_session()
class Filter():
    def __init__(self, cmnd_Object):
        self.count = 0
        self.e = UserInterfaceEnv(cmnd_Object)
        
    def filter(self, enteredName):
        e = self.e
        name1 = enteredName
        #e.Remove
        self.dbsession = get_db_session()
        V = self.dbsession.query(Person).count()
        self.e.cx = (V/10) + 4
        for v in self.dbsession.query(Person).all():
            calls = []
            msg = []
            email = []
            d=0
            #for c in v:
        #........person name............
            if v.name == name1:
                    e.center(name1)
                    d = 1
                    calls = self.dbsession.query(Call).filter(Person.name == name1 ).all()
                    msg = self.dbsession.query(Msg).filter(Person.name == name1).all()
                    email = self.dbsession.query(Email).filter(Person.name ==  name1).all()

                        #rmv_cal_dub_in = []
                    calls_in_list = e.separate_in(calls)
                    rmv_cal_dub_in = e.durations(calls_in_list)
                            #..................
                    calls_out_list = e.separate_out(calls)
                    rmv_cal_dub_out = e.durations(calls_out_list)
                        #.................
                    msg_in_list = e.separate_in(msg)
                    rem_msg_dub_in = e. durations(msg_in_list)
                            #.................
                    msg_out_list = e.separate_out(msg)
                    rem_msg_dub_out = e.durations(msg_out_list)
                  #...................
                    mail_in_list = e.separate_in(email)
                    rem_mail_dub_in = e.durations(mail_in_list)
                            #.......................
                    mail_out_list = e.separate_out(email)
                    rem_mail_dub_out = e.durations(mail_out_list)
                            #.....merge all incomming_outgoing..set duration
                    in_list = []
                    in_list.append(rmv_cal_dub_in)
                    in_list.append(rem_msg_dub_in)
                    in_list.append(rem_mail_dub_in)
                    in_merge = in_list
                    in_merge = e.merge(in_list)


                        #......................
                    out_list = []
                    out_list.append(rmv_cal_dub_out)
                    out_list.append(rem_msg_dub_out)
                    out_list.append(rem_mail_dub_out)
                    z = out_list
                    outt = e.merge_out(z)
            #..........represent incoming outgoing both.............
                    r =[]
                    g = []
                    for item in in_merge:
                     for o in outt:
                         if (cmp(int(item['from']), int(o['from']))) == 0:
                            r = item
                            g = o
                            NUM = item['from']
                            center= (1,1,1)
                            pos= e.addball(NUM)
                            k = item['key']
                            colour1 = e.colours(k)
                                #print colour1
                                #print colour1
                                #k = o['key']
                                #colourr2 = e.colours(k)
                            if item['duration'] <= 10:
                                d = 0.1
                            if item['duration'] > 10:
                                d = item['duration']
                                d = d/10
                                d = d*(0.1)
                            e.drawLine(center,pos,colour1,d)

                           # if o['duration'] <= 10:
                            # m = 0.1
                            #if o['duration'] > 10:
                             # m = o['duration']
                              # m = m/10
                               # m = m*(0.1)
                            #e.drawLine(center,pos,colourr2,m)
                            in_merge.remove(r)
                            outt.remove(g)


                 #......for incoming use any other line seg........................
                    for i in in_merge:
                        center= (1,1,1)
                        NUM = i['from']
                        pos= e.addball(NUM)
                        k = i['key']
                        if i['duration'] <= 10:
                            d = 0.1
                        if i['duration'] > 10:
                            d = i['duration']
                            d = d/10
                            d = d*(0.1)

                        colour2 = e.colours(k)
                        e.drawLine(center,pos,colour2,d)


                 #..........Use different style of line to draw outgoing
                    for l in outt:
                        center= (1,1,1)
                        NUM = l['from']
                        pos= e.addball(NUM)
                        k = l['key']
                        if l['duration'] <= 10:
                            d = 0.8
                        if l['duration'] > 10:
                            d = l['duration']
                            d = d/10
                            d = d*(0.8)

                        colour3 = e.colours(k)
                        e.drawLine(center,pos,colour3,d)
        e.model = True
        e.text = True
        e.link = True
        e.person = True
        if d== 0:
            e.person = False
