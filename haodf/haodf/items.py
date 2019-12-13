# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HaodfItem(scrapy.Item):
    #hospital.sql
    province = scrapy.Field()
    city = scrapy.Field()
    hospital = scrapy.Field()
    hospital_level = scrapy.Field()
    hospital_type = scrapy.Field()
    department_num = scrapy.Field()
    doctorTotal_num = scrapy.Field()
    telephone = scrapy.Field()
    hospital_href = scrapy.Field()

    #department.sql
    department = scrapy.Field()
    doctorDep_num = scrapy.Field()
    department_href = scrapy.Field()

    #doctor.sql
    doctor_name = scrapy.Field()
    doctor_title = scrapy.Field()
    doctor_score = scrapy.Field()
