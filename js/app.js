var app = angular.module('app', []);

//I change the AngularJS delimiters because JINJA uses the same delimiters and it caused errors
//In this app just use "{[ ]}" instead of "{{ }}"
app.config(['$interpolateProvider', function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}');
}]);

