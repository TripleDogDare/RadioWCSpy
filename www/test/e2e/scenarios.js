'use strict';

/* http://docs.angularjs.org/guide/dev_guide.e2e-testing */

describe('Radio WCS App', function() {

  it('should redirect index.html to #/playlist', function() {
    browser.get('app/index.html');
    browser.getLocationAbsUrl().then(function(url) {
        expect(url.split('#')[1]).toBe('/playlist');
      });
  });


  describe('Playlist view', function() {

    beforeEach(function() {
      browser.get('app/index.html#/playlist');
    });


    it('should filter the playlist as a user types into the search box', function() {

      var playList = element.all(by.repeater('track in playlist'));
      var query = element(by.model('query'));

      expect(playlist.count()).toBe(20);

      query.sendKeys('en');
      expect(playlist.count()).toBe(4);

      query.clear();
      query.sendKeys('gomez');
      expect(playlist.count()).toBe(1);
    });


    it('should be possible to control order via the drop down select box', function() {

      var column = element.all(by.repeater('track in playlist').column('track.title'));
      var query = element(by.model('query'));

      function getNames() {
        return column.map(function(elm) {
          return elm.getText();
        });
      }

      query.sendKeys('en'); //let's narrow the dataset to make the test assertions shorter
      

      expect(getNames()).toEqual([
        "The Heart Wants What It Wants",
        "Seven Nation Army",
        "I Put a Spell On You",
        "i"
      ]);

      element(by.model('orderProp')).element(by.css('option[value="title"]')).click();
      expect(getNames()).toEqual([
        "i"
        "I Put a Spell On You",
        "Seven Nation Army",
        "The Heart Wants What It Wants",
      ]);

    });

  });

});
