#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-9 下午5:36

import xadmin
from .models import UserComments,UserFavorite


class UsercommentsAdmin(object):
    pass

class UserfavoriteAdmin(object):
    pass

xadmin.site.register(UserComments,UsercommentsAdmin)
xadmin.site.register(UserFavorite,UserfavoriteAdmin)