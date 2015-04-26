'use strict';

/* App Module */

var radiowcsApp = angular.module('radiowcsApp', [
  'ngRoute',
  // 'radiowcsAnimations',
  'radiowcsControllers',
  'radiowcsFilters',
  // 'radiowcsServices'
]);

radiowcsApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/playlist', {
        templateUrl: 'partials/playlist.html',
        controller: 'PlaylistCtrl'
      }).
      otherwise({
        redirectTo: '/playlist'
      });
  }]);
