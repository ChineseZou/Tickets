from get_station import *
import requests


data = []
type_data = []

def query(date,from_station,to_station):
    data.clear()
    type_data.clear()
    url='https://kyfw.12306.cn/otn/leftTicket/query?' \
        'leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&' \
        'leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
    response = requests.get(url)
    result = response.json()
    result = result['data']['result']

    if isStations() == True:
        stations = eval(read())
        if len(result) != 0:
            for i in result:
                tmp_list = i.split('|')
                from_station =\
                    list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station =\
                    list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                seat = [tmp_list[3],from_station,to_station,tmp_list[8],
                        tmp_list[9],tmp_list[10],tmp_list[32],tmp_list[31],
                        tmp_list[30],tmp_list[21],tmp_list[23],tmp_list[33],
                        tmp_list[28],tmp_list[24],tmp_list[29],tmp_list[26]]
                newSeat = []
                for s in seat:
                    if s =="":
                        s='- -'
                    else:
                        s= s
                    newSeat.append(s)
                data.append(newSeat)
        return data

def g_vehicle():
    if len(data) != 0:
        for g in data:
            i=g[0].startswith('G')
            if i:
                type_data.append(g)
def r_g_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for g in data :
            i = g[0].startswith('G')
            if i:
                type_data.remove(g)
def d_vehicle():
    if len(data) != 0:
        for d in data:
            i=d[0].startswith('D')
            if i:
                type_data.append(d)
def r_d_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for d in data :
            i = d[0].startswith('D')
            if i:
                type_data.remove(d)
def z_vehicle():
    if len(data) != 0:
        for z in data:
            i=z[0].startswith('Z')
            if i:
                type_data.append(z)
def r_z_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for z in data :
            i = z[0].startswith('Z')
            if i:
                type_data.remove(z)
def t_vehicle():
    if len(data) != 0:
        for t in data:
            i=t[0].startswith('T')
            if i:
                type_data.append(t)
def r_t_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for t in data :
            i = t[0].startswith('T')
            if i:
                type_data.remove(t)
def k_vehicle():
    if len(data) != 0:
        for k in data:
            i=k[0].startswith('K')
            if i:
                type_data.append(k)
def r_k_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for k in data :
            i = k[0].startswith('K')
            if i:
                type_data.remove(k)






