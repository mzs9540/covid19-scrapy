import scrapy
import locale
from ..items import Covid19Item

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class FirstSpider(scrapy.Spider):

    name = 'covid19'
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    def parse(self, response):
        items = Covid19Item()
        t = response.css('table')
        countries = []
        total_cases = []
        new_cases = []
        total_deaths = []
        new_deaths = []
        total_recovered = []
        active_cases = []
        total_cases_per_million = []
        death_per_million = []

        for data in t.css('td:nth-child(1)'):
            value = "".join(data.css('::text').get(default='0'))
            countries.append(value)

        for data in t.css('td:nth-child(2)'):
            value = "".join(data.css('::text').get(default='0'))
            total_cases.append(locale.atoi(value))

        for data in t.css('td:nth-child(3)'):
            value = "".join(data.css('::text').get(default='0'))
            new_cases.append(locale.atoi(value))

        for data in t.css('td:nth-child(4)'):
            value = "".join(data.css('::text').get(default='0'))
            if value == ' ' or '  ':
                value = '0'
            total_deaths.append(locale.atoi(value))

        for data in t.css('td:nth-child(5)'):
            value = "".join(data.css('::text').get(default='0'))
            new_deaths.append(locale.atoi(value))

        for data in t.css('td:nth-child(6)'):
            value = "".join(data.css('::text').get(default='0'))
            total_recovered.append(locale.atoi(value))

        for data in t.css('td:nth-child(7)'):
            value = "".join(data.css('::text').get(default='0'))
            active_cases.append(locale.atoi(value))

        for data in t.css('td:nth-child(9)'):
            value = "".join(data.css('::text').get(default='0'))
            total_cases_per_million.append(locale.atof(value))

        for data in t.css('td:nth-child(10)'):
            value = "".join(data.css('::text').get(default='0'))
            death_per_million.append(locale.atof(value))
        # new_cases = t.css('td:nth-child(3)::text').get(default=0)
        # total_deaths = t.css('td:nth-child(4)::text').get(default=0)
        # new_deaths = t.css('td:nth-child(5)::text').get(default=0)
        # total_recovered = t.css('td:nth-child(6)::text').get(default=0)
        # active_cases = t.css('td:nth-child(7)::text').get(default=0)
        # total_cases_per_million = t.css('td:nth-child(9)::text').extract()
        # death_per_million = t.css('td:nth-child(10)::text').extract()
        for i in range(len(total_cases)):
            items['countries'] = countries[i]
            items['total_cases'] = total_cases[i]
            items['new_cases'] = new_cases[i]
            items['total_deaths'] = total_cases[i]
            items['new_deaths'] = new_deaths[i]
            items['total_recovered'] = total_recovered[i]
            items['active_cases'] = active_cases[i]
            items['total_cases_per_million'] = total_cases_per_million[i]
            items['death_per_million'] = death_per_million[i]
            yield items

