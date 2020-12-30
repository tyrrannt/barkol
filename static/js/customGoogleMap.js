(function (window, googleMap) {
    var styles = [
        // {
        //   // featureType: 'labels',
        //   elementType: 'labels',
        //   stylers: [
        //   {
        //     color: "#585858"
        //   },
        //   {gamma: 0.9}]
        // },
        {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [
                {
                    color: "#d8d8d8"
                }]
        },
        {
            featureType: 'landscape',
            elementType: 'geometry',
            stylers: [
                {
                    color: "#ececec"
                }]
        },
        {
            featureType: 'poi',
            elementType: 'geometry',
            stylers: [
                {
                    color: "#f2f2f2"
                }]
        },
        {
            featureType: 'road',
            elementType: 'geometry',
            stylers: [
                {
                    color: "#ffffff"
                }]
        }];

    // map options
    var options = googleMap.MAP_OPTIONS = {
            center: {
                lat: 42.5917,
                lng: -74.7505
            },
            // zoom: 10,
            disableDefaultUI: true,//bool value, default fasle
            scrollwheel: false, //bool value, default true
            zoomControl: false,
            draggable: true,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            styles: styles
        },
        element = document.getElementById('map'),
        // map
        map = googleMap.create(element, options);
    map.zoom(16);
    var marker1 = map.addMarker({
        lat: 42.5917,
        lng: -74.7505,
        visible: true,
        draggable: true,
        icon: 'img/pin.png',
        content: '<div style="padding: 30px 40px 30px 60px;"><h4>ADDRESS</h4>' +
            '<div>' +
            '<a href="#"><p><i class="fa fa-map-marker" aria-hidden="true"></i>Green lake, Hotel plaza</p>' +
            '<p><span></span> New york, USA</p></a>' +
            '<a href="#"><p><i class="fa fa-phone" aria-hidden="true"></i>807 302 2186</p></a>' +
            '</div>' +
            '</div>'
    });
    var marker2 = map.addMarker({
        lat: 42.5931,
        lng: -74.7485,
        visible: true,
        draggable: true,
        icon: 'img/pin.png',
        content: '<div style="padding: 30px 40px 30px 60px;"><h4>ADDRESS</h4>' +
            '<div>' +
            '<a href="#"><p><i class="fa fa-map-marker" aria-hidden="true"></i>Green lake, Hotel plaza</p>' +
            '<p><span></span> New york, USA</p></a>' +
            '<a href="#"><p><i class="fa fa-phone" aria-hidden="true"></i>807 302 2186</p></a>' +
            '</div>' +
            '</div>'
    });
    var marker3 = map.addMarker({
        lat: 42.5931,
        lng: -74.7535,
        visible: true,
        draggable: true,
        icon: 'img/pin.png',
        content: '<div style="padding: 30px 40px 30px 60px;"><h4>ADDRESS</h4>' +
            '<div>' +
            '<a href="#"><p><i class="fa fa-map-marker" aria-hidden="true"></i>Green lake, Hotel plaza</p>' +
            '<p><span></span> New york, USA</p></a>' +
            '<a href="#"><p><i class="fa fa-phone" aria-hidden="true"></i>807 302 2186</p></a>' +
            '</div>' +
            '</div>'
    });
}(window, GoogleMap));
