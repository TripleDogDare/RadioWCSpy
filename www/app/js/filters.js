'use strict';

/* Filters */

var radiowcsFilters = angular.module('radiowcsFilters', []);''

radiowcsFilters.filter('checkmark', function() {
  return function(input) {
    return input ? '\u2713' : '\u2718';
  };
});

radiowcsFilters.filter('emptyX', function() {
	return function(input) {
		return input.trim() == '' ? '\u2718' : input;
	};
});
