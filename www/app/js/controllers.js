'use strict';

/* Controllers */

var radiowcsControllers = angular.module('radiowcsControllers', []);

radiowcsControllers.controller('PlaylistCtrl', ['$scope', '$http',
  function($scope, $http) {
	$http.get('api/recent').success(function(data) {
		$scope.playlist = data;
	});    
   
    $scope.orderProp = '-date';
  }]);
