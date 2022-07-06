import scrapy

class PropertiesSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://www.goal.com/en-my/live-scores'
    ]

    def parse(self, response):
        # # page = response.url('/live-scores')
        # filename = 'posts-%s.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)  # copy the html file locally

        for post in response.css('div.match-data'):
            yield{
                'home_team': post.css('div.team-home span.team-name::text').getall()
,
                'home_score': post.css('div.team-home span.goals::text').getall()
,
                'away_team': post.css('div.team-away span.team-name::text').getall()
,
                'away_score': post.css('div.team-away span.goals::text').getall()
,
            }

