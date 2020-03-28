#!/bin/sh
scrapy startproject spider_test
cp talent.py spider_test/spider_test/spiders/talent.py
cp -f settings.py spider_test/spider_test/settings.py
cd spider_test
scrapy crawl talent -o talent.jl
