from app.api import apiRestful
from flask_restplus import Resource
from datetime import timedelta

#멤버소개
class member:
    
    @apiRestful.route('/member/introduction')
    class MemberIntroductionView(Resource):
        
        def get(self):
            return {"return" : {
                "CEO" : "오륜주",
                "개발천재" : "오지후니",
                "말쫑쏘" : "막둥이",
                "영업부장" : "오지훈꿈나무" }
            }, 200

    #디데이 계산
    @apiRestful.route('/member/dDay')
    class MemberIntroductionView(Resource):
        
        firstday = date(2018,8,2)
        today = date.today()
        StillDay = today - firstday
        daystoday = int(StillDay) + 1
       

        def get(self):
            return {"return" : {
                "d_day" : daystoday }
            }, 200
