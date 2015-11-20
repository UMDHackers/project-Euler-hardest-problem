require 'net/http'
require 'open-uri'
require 'open_uri_redirections'
def return_pages(uri)
	http = Net::HTTP.new("www.projecteuler.com", 83)
	http.use_ssl = true
	http.ssl_version = :SSLv3
	puts "?hello"
	http.start { 
		#uri2 = URI.parse(URI.escape(uri))
		uri2 = open(uri, :allow_redirections => :safe).read
		#source = Net::HTTP.get(uri)
		source = uri2.split('\n')
		temp = []
		puts "hello?"
		source.each do |line|
			if line.include? "archives;" then 
				temp << line
			end
		end
		return source
	}
end



#main

nav_bar = return_pages('http://projecteuler.net/archives')
puts "#{nav_bar}"
