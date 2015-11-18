require 'net/http'
require 'open-uri'
def return_pages(url)
	source = Net::HTTP.get('stackoverflow.com', '/index.html')
	return source
end



#main

nav_bar = return_pages("https://projecteuler.net/archives")
puts "#{source}"
