# WebScrap with Scrapy
This project is used to scrap match data from 
'https://www.goal.com/en-my/live-scores'.
, but you can use this program to scrap any site as long as you replace the urls correctly 


You can use the following command to open the shell and start scrapping straight away

    $ scrapy shell ('url_comes_here')

Type the following commands to get the following data

    $ response.css('h3::text').getall() #to get all the h3 tags in the file
    $ response.css('.div_class_name html tag like <a>::text').get() --gives the first a attributes in the given class
    $ response.css('p::text').re(r'(\w+) any_word (\w+)') ---searches any_word in the whole doc
    $ response.xpath('xpath_here').extract ---to get elements in x path

Type the following commands to get the data from specific div

    $ post = response.css('div_class_name ')[0] --- to get div in variable post
    $ name = response.css('div_class_name a::text')[0] --- to get div attributes in variable name

    $ for post in response.css('div_class_name'):
        title= post.css('.post-header h2 a::text')[0].get(); --- to get all the title in whole div
        print(dict(title=title))--- to print whole dictionary of data

    $ quit()--- to quit the shell

Apart from shell you can also use the scraper/scraper/spiders/properties_spider.py
to scrap the data from the python file

    $ scrapy crawl posts

You can also convert the data to JSON file using following command

    $ scrapy crawl posts -0 posts.json

