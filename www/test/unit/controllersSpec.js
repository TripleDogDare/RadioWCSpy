'use strict';

/* jasmine specs for controllers go here */
describe('Radio WCS controllers', function() {

  describe('PlaylistCtrl', function(){
    var scope, ctrl;

    beforeEach(module('radiowcsApp'));

    beforeEach(inject(function($controller) {
      scope = {};
      ctrl = $controller('PlaylistCtrl', {$scope:scope});
    }));

    it('should create "playlist" model with specified # of tracks', function() {
      expect(scope.playlist.length).toBe(20);
    });


    it('should set the default value of orderProp model', function() {
      expect(scope.orderProp).toBe('-date');
    });
    
  });
});
