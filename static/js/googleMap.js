(function(window, google) {
  var GoogleMap = (function(){
    function GoogleMap(element, options){
      this.gMap = new google.maps.Map(element, options);
    }
    GoogleMap.prototype = {
      zoom: function(level) {
        if (level) {
          this.gMap.setZoom(level);
        } else {
          return this.gMap.getZoom();
        }
      },
      _on: function(options) {
        var self = this;
        google.maps.event.addListener(options.obj, options.event, function(e){
          options.callback.call(self, e);
        });
      },
      addMarker: function(options) {
        var marker;
        options.position = {
          lat: options.lat,
          lng: options.lng
        }
        marker = this._createMarker(options)
        if (options.event) {
          this._on({
            obj: marker,
            event: options.event.name,
            callback: options.event.callback
          });
        }
        if (options.content) {
          this._on({
            obj: marker,
            event: 'click',
            callback: function() {
              var infoWindow = new google.maps.InfoWindow({
                content: options.content
              });
              infoWindow.open(this.gMap, marker);
            }
          })
        }
        return marker;        
      },
      _createMarker: function(options) {
        options.map = this.gMap;
        return new google.maps.Marker(options);
      }
    };
    return GoogleMap;
  }());
  GoogleMap.create = function(element, options) {
    return new GoogleMap(element, options);
  };
  window.GoogleMap = GoogleMap;
}(window, google));