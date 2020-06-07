<!doctype html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <title>Computer Status</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
        <script src="js/jquery.knob.min.js"></script>
        <script type = "text/javascript" src = "https://www.gstatic.com/charts/loader.js"></script>
        <script type = "text/javascript">
           google.charts.load('current', {packages: ['corechart']});     
        </script>
        <style>
            body {
                background-color:#000;
                color:white;
                background:url('img/background.jpg');
                  background-size: cover;

            }
        </style>
    </head>

    <body>

        <div class="container" style="padding: 20px; background-color: #0f0f0f; margin: 35px; border-radius: 10px; opacity: 0.65;">
          <div class="row">
            <div class="col-sm">
              <input id="cpu" type="text" value="0" class="dial" data-fgColor="#3CFF33" data-bgColor="#133c07">
              <div style="color: #3CFF33">CPU %</div>
            </div>
            <div class="col-sm">
              <input id="cpu_temp" type="text" value="0" class="dial" data-fgColor="#cc0000" data-bgColor="#301111">
              <div style="color: #a40000">CPU Temp &deg;F</div>
            </div>
            <div class="col-sm">
              <input id="network_bytes" type="text" value="0" class="dial" data-fgColor="#FFBE33" data-bgColor="#503906">
              <div style="color: #e9b96e">Network [MB/Sec]</div>
            </div>
          </div>
          <br/>
          <div class="row">
            <div class="col-sm">
              Hard Drives: [<span id="hardrive_temp_f"></span> , <span id="hardrive_files_temp_f"></span>]
            </div>
            <div class="col-sm">
              <input id="ram_free" type="text" value="0" class="dial" data-fgColor="#1f47f1" data-bgColor="#060b42">
              Memory: 48Gb [<span id="free"></span>]
            </div>
          </div>
          
        </div>
        
        <script>
            function getData() {
            
                $.get("http://dashboard.kevinhinds.net/computer", function(data, status) {
                    data = data.message.replace("{'HTML': '", "");
                    data = data.replace("'}", "");
                    data = JSON.parse(data);
                    
                    $("#hardrive_files_temp_f").html(data.hardrive_files_temp_f + "&deg; F");
                    $("#hardrive_temp_f").html(data.hardrive_temp_f + "&deg; F");
                    
                    $("#cpu").val(data.cpu_percent).trigger('change');
                    $("#cpu_temp").val(data.cpu_temp).trigger('change');
                    $("#network_bytes").val(data.network_bandwidth_bytes/1024/1024).trigger('change');
                    $("#free").html(parseInt((data.totalMemory_gigs - data.usedMemory_gigs)/data.totalMemory_gigs * 100) + "% Available");
                
                    $("#ram_free").val(parseInt(data.usedMemory_gigs/data.totalMemory_gigs * 100)).trigger('change');
                    
                });

                setTimeout(function() {
                    getData();
                }, 1000);
            };

            $(function() {
                $("#cpu").knob();
                $("#cpu_temp").knob({
                    'min':50,
                    'max':220
                });
                $("#network_bytes").knob({
                    'min':0,
                    'max':100
                });
                $("#ram_free").knob({
                    'min':0,
                    'max':100,
                    'width': 60,
                    'height': 60
                });
                getData();
            });
        </script>

    </body>
    </html>
