'use strict';

/* jasmine specs for controllers go here */
describe('Radio WCS controllers', function() {

  describe('PlaylistCtrl', function(){
    var scope, ctrl;

    beforeEach(module('radiowcsApp'));

    beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
      $httpBackend = _$httpBackend_;
	$httpBackend.expectGet('api/recent');
	respond([{artist:'Selena', title: 'test', bpm: 32, image: '', date: 123456789}]);
	scope = $rootScope.$new();
      ctrl = $controller('PlaylistCtrl', {$scope:scope});
    }));

    it('should create "playlist" model with specified # of tracks', function() {
      expect(scope.playlist.length).toBe(1);
    });


    it('should set the default value of orderProp model', function() {
      expect(scope.orderProp).toBe('-date');
    });
    
  });
});
