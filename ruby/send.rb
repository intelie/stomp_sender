
require 'rubygems'
require 'stomp'
require 'json'

conn = Stomp::Connection.open(nil, nil, 'host', '61613', true)

headers = {'eventtype' => 'ping', 'timestamp' => Time.new.to_i * 1000 } # timestamp in milliseconds
conn.publish '/queue/events', JSON({:host => 'example.com', :idle => 42}), headers