# -*- coding: utf-8 -*-
db.define_table('user_email',
    Field('user_id', 'bigint'),
    Field('email_address', 'string'),
    Field('confirmed','integer'),
 	Field('primary_key','integer'),
    Field('login_time','datetime', default = request.now)       
)

db.user_email.id.readable = False
db.user_email.email_address.requires = IS_EMAIL() and IS_NOT_EMPTY()
