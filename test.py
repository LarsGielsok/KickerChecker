from datetime import datetime
part1 = "<rss version=\"2.0\"><channel><title>MaibornWolff Kicker  RSS Feed</title><description>Hier wird angezeigt, ob der Kicker frei ist</description><language>de</language><link></link>"
part2 = "<lastBuildDate>"
part3 = " Sat, 1 Jan 2015 00:00:00 GMT</lastBuildDate>"
part4 = "<item><title>"
part5 = str(datetime.now())
part6 = "</title><description>Die Nachricht an sich</description>"
part7 = "<link></link>"
part8 = "<pubDate>Sat, 1. Jan 2015 00:00:00 GMT</pubDate>"
part9 = "<guid>01012000-000000</guid>"
part10 = "</item></channel></rss>"

with open("./http/rss.xml", "r+") as f:
     f.truncate()	
     f.write(part1+part2+part3+part4+part5+part6+part7+part8+part9+part10)
