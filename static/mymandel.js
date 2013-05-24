function hsv_to_rgb(h, s, v)
            {
              if ( v > 1.0 ) v = 1.0;
              var hp = h/60.0;
              var c = v * s;
              var x = c*(1 - Math.abs((hp % 2) - 1));
              var rgb = [0,0,0];

              if ( 0<=hp && hp<1 ) rgb = [c, x, 0];
              if ( 1<=hp && hp<2 ) rgb = [x, c, 0];
              if ( 2<=hp && hp<3 ) rgb = [0, c, x];
              if ( 3<=hp && hp<4 ) rgb = [0, x, c];
              if ( 4<=hp && hp<5 ) rgb = [x, 0, c];
              if ( 5<=hp && hp<6 ) rgb = [c, 0, x];

              var m = v - c;
              rgb[0] += m;
              rgb[1] += m;
              rgb[2] += m;

              rgb[0] *= 255;
              rgb[1] *= 255;
              rgb[2] *= 255;
              return rgb;
            }
        function smoothColor(steps, n, Tr, Ti)
            {
              var logBase = 1.0 / Math.log(2.0);
              var logHalfBase = Math.log(0.5)*logBase;
              /*
               * Original smoothing equation is
               *
               * var v = 1 + n - Math.log(Math.log(Math.sqrt(Zr*Zr+Zi*Zi)))/Math.log(2.0);
               *
               * but can be simplified using some elementary logarithm rules to
               */
              return 5 + n - logHalfBase - Math.log(Math.log(Tr+Ti))*logBase;
            }
        function pickColor(steps, n, Tr, Ti)
            {
              var interiorColor = [0, 0, 0, 255];
              if ( n == steps ) // converged?
                return interiorColor;

              var v = smoothColor(steps, n, Tr, Ti);
              var c = hsv_to_rgb(360.0*v/steps, 1.0, 10.0*v/steps);

              // swap red and blue
              var t = c[0];
              c[0] = c[2];
              c[2] = t;

              c.push(255); // alpha
              return c;
            }
        function iterateEquation(Cr, Ci, escapeRadius, iterations)
            {
              var Zr = 0;
              var Zi = 0;
              var Tr = 0;
              var Ti = 0;
              var n  = 0;

              for ( ; n<iterations && (Tr+Ti)<=escapeRadius; ++n ) {
                Zi = 2 * Zr * Zi + Ci;
                Zr = Tr - Ti + Cr;
                Tr = Zr * Zr;
                Ti = Zi * Zi;
              }

              /*
               * Four more iterations to decrease error term;
               * see http://linas.org/art-gallery/escape/escape.html
               */
              for ( var e=0; e<4; ++e ) {
                Zi = 2 * Zr * Zi + Ci;
                Zr = Tr - Ti + Cr;
                Tr = Zr * Zr;
                Ti = Zi * Zi;
              }

              return [n, Tr, Ti];
            }
        function drawTile(z,x,y)
          {
            var resolutionx = 256;
            var resolutiony = 256;
            var big_x_left = -2.5 , big_x_right = 1.1; 
            var big_y_bottom = -1.3, big_y_top = 1.3;
            var big_step_x = big_x_right - big_x_left;
            var big_step_y = big_y_top - big_y_bottom;

            if (z!= 0){
                var step_x = big_step_x/Math.pow(2., z)
                var step_y = big_step_y/Math.pow(2., z)
            }
                
            else { 
                var step_x = big_step_x;
                var step_y = big_step_y;
            }   

            var start_x = big_x_left + x*step_x;
            var start_y = big_y_top - y*step_y;
            var finish_x = start_x + step_x;
            var finish_y = start_y - step_y;

            var yx = resolutionx/ step_x;
            var sx = start_x*yx;
            var fx = finish_x*yx;

            var yy = resolutiony/ step_y;
            var sy = start_y*yy;
            var fy = finish_y*yy;

            var p_x_step = step_x / resolutionx;
            var p_y_step = step_y / resolutiony;

            
            // var img = context.createImageData(resolutionx, resolutiony);
            var img_data = new Uint8ClampedArray(resolutionx*resolutiony*4);
            var f = Math.sqrt(
                    0.001+2.0 * Math.min(
                      Math.abs(start_x - finish_x ),
                      Math.abs(start_y - finish_y)));

            var steps = Math.floor(223.0/f);

            var off = 0;
            // console.log("About to start going through pixels");
            
            var countpix = 0;
            for ( var py=0; py < resolutiony; ++py){
                for ( var px=0; px < resolutionx; ++px){
                

                    var real = start_x + px*p_x_step + p_x_step/2.
                    var imaginary = start_y - py*p_y_step - p_y_step/2.
                    // # print "Pixel %d,%d: %f +%fi"%(px,py,real,imaginary)
                    var p = iterateEquation(real, imaginary, 100., steps);
                    var color = pickColor(steps, p[0], p[1], p[2]);
                    img_data[off++] = color[0];
                    img_data[off++] = color[1];
                    img_data[off++] = color[2];
                    img_data[off++] = 255;
                    
                    countpix++
                }
            }
            
            return img_data
          }
          function dirtydirtypause(ms) {
            ms += new Date().getTime();
            while (new Date() < ms){}
            } 
          function sendTile(z,x,y){
              var canvas = document.getElementById('myCanvas');
              var context = canvas.getContext('2d');
              
              var ar = drawTile(z,x,y);

              //This is just silly
              var imageData = context.createImageData(256, 256);
              imageData.data.set( ar );
              context.putImageData(imageData, 0, 0);
              var canvasData = canvas.toDataURL();

              $.ajax({
                      type: "POST",
                      url: 'http://panosfirbas.webfactional.com/api/'+z +"/"+x +"/"+y ,
                      data: {
                            'arurl' : canvasData,
                      },
                      // dataType: json,
                      success: function(data){
                             // alert(data);
                             
                             console.log("win");
                         }
                      
                    });
              
              return canvasData

          }