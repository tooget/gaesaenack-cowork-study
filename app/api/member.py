from app.api import apiRestful
from flask_restplus import Resource
from datetime import date


#개새낙 창립 D-Day 계산

@apiRestful.route('/member/Dday')
class Dday(Resource):

    def get(self):

        Firstday = date(2018,8,2)
        Today = date.Today()
        StillDay = Today - Firstday
        DaysToday = int(StillDay.days) + 1

        return {"result" : 
            DaysToday
        }, 200
