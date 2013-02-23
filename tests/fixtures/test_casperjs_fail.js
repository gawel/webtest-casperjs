
var system = require('system');
var url = system.env['APPLICATION_URL'];

var casper = require('casper').create();
casper.start(url, function() {
    this.test.assertTitle('It Work!');
});

casper.run(function() {
    this.test.done();
    this.test.renderResults(true);
});
