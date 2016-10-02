import socket
import sys
import json
import os
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1

HOST, PORT = 'https://whispering-castle-67381.herokuapp.com', 5000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
while True:
    client_connection, client_address = listen_socket.accept()

    while True:
        request = client_connection.recv(1024)
        print request

    '''with open("userAnalyticsPy.json") as json_file:
        d = json.load(json_file)
        print(d)'''
        if request:
            tradeoff_analytics = TradeoffAnalyticsV1(
            username='af7839e5-5719-4357-9f2f-8b4607ba84d5',
            password='IY2KB0panLuF')

            with open(join(dirname(__file__), 'userAnalyticsPy.json')) as data_file:
                problem_data = json.load(data_file)
                # print(json.dumps(tradeoff_analytics.dilemmas(problem_data), indent=2))
            resolution = tradeoff_analytics.dilemmas(problem_data)
            solutionNum = 0
            while resolution["resolution"]["solutions"][solutionNum]["status"]!="FRONT":
                solutionNum = solutionNum+1
            firstChoice = resolution["resolution"]["solutions"][solutionNum]["solution_ref"]
            index = int(firstChoice)-1
            reccomend = resolution["problem"]["options"][index]["name"]
            client_connection.sendall(reccomend)
            else:
                break
