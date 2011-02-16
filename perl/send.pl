use strict;
use JSON;
use Net::Stomp;
use warnings;

my $stomp = Net::Stomp->new({ hostname => 'localhost', port => '61613' });
my $headers = { timestamp => time*1000, destination => '/queue/events', eventtype => "memory"};
my $body = to_json({free => 1234});

my $frame = Net::Stomp::Frame->new({
        command => 'SEND',
        headers => $headers,
        body => $body,
});

$stomp->connect;
$stomp->send_frame($frame);
$stomp->disconnect;
