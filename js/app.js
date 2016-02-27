var app = angular.module('app', ['ngRoute']);

//Routing Set Up
//app.config(function($routeProvider){
//	$routeProvider.when('/',
//	{
//		templateUrl:'/templates/home.html',
//		controller: 'JewelryController'
//	})
//});

//I change the AngularJS delimiters because JINJA uses the same delimiters and it caused errors
//In this app just use "{[ ]}" instead of "{{ }}"
app.config(['$interpolateProvider', function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}');
}]);

