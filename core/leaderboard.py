import urllib.request
import json


class Leaderboard:
    """ 处理排行榜，Azure REST API提供支持 """

    def __init__(self):

        self.application_url = "http://gl-tower-defence.azurewebsites.net/tables/scoreboardentry"
        self.application_headers = {"x-zumo-application": "cwrbABoHBGWKMhIiHrkVChWHoDcmAa78"}
        self.entries = []

    def retrieve(self):
        """ 从REST API更新排行榜 """
        try:
            request = urllib.request.Request(self.application_url, headers=self.application_headers)
            response = urllib.request.urlopen(request)

            raw = response.read().decode()
            data = json.loads(raw)

            self.entries = [LeaderboardEntry(d) for d in data]
            self.entries.sort(key=lambda e: e.score, reverse=True)

        except:
            print("Error downloading leaderboard")

    def add(self, level, name, score, wave):
        """
        向排行榜添加一个新条目，使用REST API保存它。
        
        Args:
            level (str): 该分数的关卡
            name (str): 用户名称
            score (int): 得分
            wave (int): 波数
        """
        try:
            raw = {"level": level, "name": name, "score": score, "wave": wave}
            data = json.dumps(raw).encode()

            request = urllib.request.Request(self.application_url, data, self.application_headers)
            request.add_header("Content-Type", "application/json")
            request.add_header("Content-Length", len(data))
            response = urllib.request.urlopen(request)

        except:
            print("Error updating scoreboard")


class LeaderboardEntry:
    """ 排行榜中的单个条目 """

    def __init__(self, data):
        """
        Args:
            data (dict): 来自json的条目数据
        """
        self.level = data["level"]
        self.name = data["name"]
        self.score = int(data["score"])
        self.wave = int(data["wave"])
