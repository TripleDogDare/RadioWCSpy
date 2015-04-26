'use strict';

/* jasmine specs for filters go here */

describe('filter', function() {

  beforeEach(module('radiowcsFilters'));


  describe('checkmark', function() {

    it('should convert boolean values to unicode checkmark or cross',
        inject(function(checkmarkFilter) {
      expect(checkmarkFilter(true)).toBe('\u2713');
      expect(checkmarkFilter(false)).toBe('\u2718');
    }));
  });

  describe('emptyX', function() {

    it('should convert empty strings to unicode cross',
        inject(function(emptyXFilter) {
  		expect(emptyXFilter('')).toBe('\u2718');
  		expect(emptyXFilter(' ')).toBe('\u2718');
  		expect(emptyXFilter('\n')).toBe('\u2718');
  		expect(emptyXFilter('\t')).toBe('\u2718');
    }));
  });

});
