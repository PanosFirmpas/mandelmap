var map;
var ajaxRequest;
var plotlist;
var plotlayers=[];


function initmap() {
    // // set up the map
    // map = new L.Map('map');

    // // create the tile layer with correct attribution

    // //var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    // var osmUrl="http://panosfirbas.webfactional.com/img/{z}/{x}/{y}";//'http://panosfirbas.webfactional.com/static/dump/{z}/{x}/{y}.png';
    // var osmAttrib='Map data © OpenStreetMap contributors';
    // var osm = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 15, attribution: osmAttrib,noWrap:true});       

    // // start the map in South-East England
    // map.setView(new L.LatLng(0, 0),0);
    // map.addLayer(osm);


 $(function() {
            
            // create a map in the "map" div, set the view to a given place and zoom
            var map = L.map('map').setView([0, 0], 0);
            var osmUrl="http://panosfirbas.webfactional.com/static/media/{z}/{x}/{y}.png";//'http://panosfirbas.webfactional.com/static/dump/{z}/{x}/{y}.png';
            var osmAttrib='Map data © OpenStreetMap contributors';
            var osm = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 15, attribution: osmAttrib,noWrap:true});       
            map.addLayer(osm);
            

            
            
            // var tiles = new L.TileLayer.Canvas();
            // tiles.drawTile = function (canvas, tile, zoom) {
            //     var context = canvas.getContext('2d');
            //     var t = context.getImageData(0,0,100,100);
                // console.log(tile);
                // console.log(t.data);
                // // circle radius
                // var radius = 12;

                // var tileSize = this.options.tileSize;

                // for (var i = 0; i < points.length; i++) {

                //     var point = new L.LatLng(points[i].lat, points[i].lon);

                //     // start coordinates to tile pixels
                //     var start = tile.multiplyBy(tileSize);

                //     // actual coordinates to tile pixel
                //     var p = map.project(point);

                //     // point to draw
                //     var x = Math.round(p.x - start.x);
                //     var y = Math.round(p.y - start.y);

                //     // Circle
                //     context.beginPath();
                //     context.arc(x, y, radius, 0, 2 * Math.PI, false);

                //     // Fill (Gradient)
                //     var grd = context.createRadialGradient(x, y, 5, x, y, radius);
                //     grd.addColorStop(0, "#8ED6FF");
                //     grd.addColorStop(1, "#004CB3");
                //     context.fillStyle = grd;

                //     // Shadow
                //     context.shadowColor = "#666666";
                //     context.shadowBlur = 5;
                //     context.shadowOffsetX = 7;
                //     context.shadowOffsetY = 7;
                //     context.fill()

                //     context.lineWidth = 2;
                //     context.strokeStyle = "black";
                //     context.stroke();

                //     // Text
                //     context.lineWidth = 1;
                //     context.fillStyle = "#000000";
                //     context.lineStyle = "#000000";
                //     context.font = "12px sans-serif";
                //     context.textAlign = "center";
                //     context.textBaseline = "middle";
                //     context.fillText(i + 1, x, y);

                        //}
                
            // };
            
            // map.addLayer(tiles);    
            
            
            
         });


}

