'use strict';

/* Controllers */

var radiowcsControllers = angular.module('radiowcsControllers', []);

radiowcsControllers.controller('PlaylistCtrl', ['$scope',
  function($scope) {
    $scope.playlist = [
    {
        "artist": "SELENA GOMEZ" ,
        "bpm": "83" ,
        "date": "1430021103" ,
        "filename": "SELENA GOMEZ - The Heart Wants What It Wants.mp3" ,
        "genre": "Pop" ,
        "id": "24e7f8ec-c49d-45af-9b36-8a6cda852fe9" ,
        "image": "SELENA GOMEZ - The Heart Wants What It Wants.jpg" ,
        "title": "The Heart Wants What It Wants" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "SAM & DAVE" ,
        "bpm": "112" ,
        "date": "1430020949" ,
        "filename": "SAM & DAVE - Soul Man.mp3" ,
        "genre": "Soul" ,
        "id": "18f314c8-a70b-4729-8642-219ff0d9a82c" ,
        "image": "SAM & DAVE - Soul Man.jpg" ,
        "title": "Soul Man" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "ED SHEERAN" ,
        "bpm": "80" ,
        "date": "1430020674" ,
        "filename": "ED SHEERAN - Thinking Out Loud.mp3" ,
        "genre": "Pop" ,
        "id": "88030a1e-1c4e-4510-9ffe-2dd8a3e77f2d" ,
        "image": "ED SHEERAN - Thinking Out Loud.jpg" ,
        "title": "Thinking Out Loud" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "JAYMES YOUNG" ,
        "bpm": "" ,
        "date": "1430020448" ,
        "filename": "JAYMES YOUNG - What Is Love.mp3" ,
        "genre": "" ,
        "id": "a16beb8f-a1c2-4cfd-8fa3-135488c0b2c1" ,
        "image": "radiowcs.jpg" ,
        "title": "What Is Love" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "TOM SCOTT" ,
        "bpm": "" ,
        "date": "1430020120" ,
        "filename": "TOM SCOTT - Ode To Billie Joe.mp3" ,
        "genre": "" ,
        "id": "94711c71-8323-4520-9ef5-728d2b87315f" ,
        "image": "radiowcs.jpg" ,
        "title": "Ode To Billie Joe" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "BEN L'ONCLE SOUL" ,
        "bpm": "110" ,
        "date": "1430019946" ,
        "filename": "BEN L'ONCLE SOUL - Seven Nation Army.mp3" ,
        "genre": "Soul" ,
        "id": "8da45e06-ee05-4156-b0b7-a4913b6e56d9" ,
        "image": "BEN L'ONCLE SOUL - Seven Nation Army.jpg" ,
        "title": "Seven Nation Army" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "KEM" ,
        "bpm": "99" ,
        "date": "1430019720" ,
        "filename": "KEM - Downtown (Feat. Snoop Dogg).mp3" ,
        "genre": "R&B" ,
        "id": "a9f5a1e8-5015-453e-b913-a1699335e700" ,
        "image": "KEM - Downtown (Feat. Snoop Dogg).jpg" ,
        "title": "Downtown (Feat. Snoop Dogg)" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "LUCY PEARL" ,
        "bpm": "106" ,
        "date": "1430019504" ,
        "filename": "LUCY PEARL - Don't Mess With My Man.mp3" ,
        "genre": "R&B" ,
        "id": "667b9df0-d2f7-4477-a135-1e01ba338fd5" ,
        "image": "LUCY PEARL - Don't Mess With My Man.jpg" ,
        "title": "Don't Mess With My Man" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "HAMILTON LOOMIS" ,
        "bpm": "92" ,
        "date": "1430019273" ,
        "filename": "HAMILTON LOOMIS - No, No, No.mp3" ,
        "genre": "Blues" ,
        "id": "b7c8c3f7-2efe-4d9c-b7c2-379b6b183803" ,
        "image": "HAMILTON LOOMIS - No, No, No.jpg" ,
        "title": "No, No, No" ,
        "url_amazon": "B004YRFEVU" ,
        "url_itunes": ""
    } ,
    {
        "artist": "ERICK SERMON" ,
        "bpm": "100" ,
        "date": "1430019028" ,
        "filename": "ERICK SERMON - Just Like Music (Feat. Marvin Gaye).mp3" ,
        "genre": "R&B" ,
        "id": "31ef5c78-1b70-4c56-b54a-f425efbfe250" ,
        "image": "ERICK SERMON - Just Like Music (Feat. Marvin Gaye).jpg" ,
        "title": "Just Like Music (Feat. Marvin Gaye)" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "JUSTIN NOZUKA" ,
        "bpm": "99" ,
        "date": "1430018787" ,
        "filename": "JUSTIN NOZUKA - After Tonight.mp3" ,
        "genre": "Rock" ,
        "id": "8342e10c-4fbb-48c8-9fe2-76cc94ec5bc7" ,
        "image": "JUSTIN NOZUKA - After Tonight.jpg" ,
        "title": "After Tonight" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "MAYER HAWTHORNE" ,
        "bpm": "113" ,
        "date": "1430018576" ,
        "filename": "MAYER HAWTHORNE - Designer Drug.mp3" ,
        "genre": "Pop" ,
        "id": "17539df4-d186-4ec6-886d-02510da24ac5" ,
        "image": "MAYER HAWTHORNE - Designer Drug.jpg" ,
        "title": "Designer Drug" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "LORDE" ,
        "bpm": "100" ,
        "date": "1430018386" ,
        "filename": "LORDE - Team.mp3" ,
        "genre": "Pop" ,
        "id": "6d7a484c-cd9a-492b-9711-b1e9fc4888d8" ,
        "image": "LORDE - Team.jpg" ,
        "title": "Team" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "ROBIN THICKE" ,
        "bpm": "108" ,
        "date": "1430018176" ,
        "filename": "ROBIN THICKE - Magic.mp3" ,
        "genre": "Soul" ,
        "id": "bd588bae-3703-49a5-b0f1-909a46229857" ,
        "image": "ROBIN THICKE - Magic.jpg" ,
        "title": "Magic" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "SADE" ,
        "bpm": "108" ,
        "date": "1430017900" ,
        "filename": "SADE - Hang On To Your Love.mp3" ,
        "genre": "Soul" ,
        "id": "16b83de8-6bef-4c69-a284-860845b6315c" ,
        "image": "SADE - Hang On To Your Love.jpg" ,
        "title": "Hang On To Your Love" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "ANNIE LENNOX" ,
        "bpm": "87" ,
        "date": "1430017680" ,
        "filename": "ANNIE LENNOX - I Put a Spell On You.mp3" ,
        "genre": "Blues" ,
        "id": "e5e89631-ff03-4a73-bded-e2c1624a02ab" ,
        "image": "ANNIE LENNOX - I Put a Spell On You.jpg" ,
        "title": "I Put a Spell On You" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "ANA POPOVIC" ,
        "bpm": "118" ,
        "date": "1430017450" ,
        "filename": "ANA POPOVIC - Unconditional.mp3" ,
        "genre": "Blues" ,
        "id": "85659241-ff7a-4d55-ae6e-059f09078f29" ,
        "image": "ANA POPOVIC - Unconditional.jpg" ,
        "title": "Unconditional" ,
        "url_amazon": "B004QBDB64" ,
        "url_itunes": "NF"
    } ,
    {
        "artist": "J WILLIAMS" ,
        "bpm": "102" ,
        "date": "1430017224" ,
        "filename": "J WILLIAMS - Your Style (Feat. Tyree And Erakah).mp3" ,
        "genre": "R&B" ,
        "id": "617e5fe8-d76d-40f8-8147-8ba604625b4c" ,
        "image": "J WILLIAMS - Your Style (Feat. Tyree And Erakah).jpg" ,
        "title": "Your Style (Feat. Tyree And Erakah)" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "KENDRICK LAMAR" ,
        "bpm": "122" ,
        "date": "1430016999" ,
        "filename": "KENDRICK LAMAR - i.mp3" ,
        "genre": "R&B" ,
        "id": "7b1cc8bb-08f0-443a-8349-9c45d472f865" ,
        "image": "KENDRICK LAMAR - i.jpg" ,
        "title": "i" ,
        "url_amazon": "" ,
        "url_itunes": ""
    } ,
    {
        "artist": "FUGEES" ,
        "bpm": "89" ,
        "date": "1430016742" ,
        "filename": "FUGEES - No Woman, No Cry.mp3" ,
        "genre": "Rap" ,
        "id": "b5cbd129-2009-44a8-b3e5-73b51cef601e" ,
        "image": "FUGEES - No Woman, No Cry.jpg" ,
        "title": "No Woman, No Cry" ,
        "url_amazon": "" ,
        "url_itunes": ""
    }
    ];
   
    $scope.orderProp = '-date';
  }]);
