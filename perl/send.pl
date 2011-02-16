use strict;
use Net::Stomp;

my $stomp = Net::Stomp->new( { hostname => 'localhost', port => '61613' } );
my $headers = {
    timestamp => time*1000,
    destination => '/queue/events',
    eventtype => "cpu"
};
my $frame = Net::Stomp::Frame->new({
        command => 'SEND',
        headers => $headers,
        body => '{"a": "b", "c": 123}'
});
$stomp->connect();
$stomp->send_frame($frame);
$stomp->disconnect();


