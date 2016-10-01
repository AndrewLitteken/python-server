import json
import os
from os.path import join, dirname
from watson_developer_cloud import TradeoffAnalyticsV1


tradeoff_analytics = TradeoffAnalyticsV1(
    username='af7839e5-5719-4357-9f2f-8b4607ba84d5',
    password='IY2KB0panLuF')

with open(join(dirname(__file__), 'userAnalyticsPy.json')) as data_file:
    problem_data = json.load(data_file)
print(json.dumps(tradeoff_analytics.dilemmas(problem_data), indent=2))
resolution = tradeoff_analytics.dilemmas(problem_data)
solutionNum = 0
while resolution["resolution"]["solutions"][solutionNum]["status"]!="FRONT":
	solutionNum = solutionNum+1
firstChoice = resolution["resolution"]["solutions"][solutionNum]["solution_ref"]
index = int(firstChoice)-1
reccomend = resolution["problem"]["options"][index]["name"]
print(reccomend)