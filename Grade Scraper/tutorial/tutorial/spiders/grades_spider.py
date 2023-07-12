from pathlib import Path

import scrapy
from .. import items

class GradesSpider(scrapy.Spider): 
    name = "grades"
    start_urls = ['https://musis1.missouri.edu/gradedist/mu_grade_dist_intro.cfm']

    def parse(self, response):
       course_number = input("Enter a course number: ")
       try:
           yield scrapy.FormRequest.from_response(response, formdata={'subject': 'MATH', 'catalog_nbr': str(course_number)}, callback = self.parse_grades)
       except AttributeError:
           print("\nNot a valid course number.\n")

    def parse_grades(self, response):
        rows = response.css('table[style*="font-size: 11px;"] tr')
        for row in rows[1:]:  # Exclude header row
            item = items.TutorialItem()
            item['a_range'] = row.xpath('.//td[8]//text()').get().strip() if row.xpath('.//td[8]//text()').get() else None
            item['b_range'] = row.xpath('.//td[9]//text()').get().strip() if row.xpath('.//td[9]//text()').get() else None
            item['c_range'] = row.xpath('.//td[10]//text()').get().strip() if row.xpath('.//td[10]//text()').get() else None
            item['d_range'] = row.xpath('.//td[11]//text()').get().strip() if row.xpath('.//td[11]//text()').get() else None
            item['f_range'] = row.xpath('.//td[12]//text()').get().strip() if row.xpath('.//td[12]//text()').get() else None
            item['average_grade'] = row.xpath('.//td[13]//text()').get().strip() if row.xpath('.//td[13]//text()').get() else None

            yield item

