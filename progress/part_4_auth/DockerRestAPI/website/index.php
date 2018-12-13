<html>
    <body>
        <ul>
            <?php
            $listAll = json_decode(file_get_contents('http://laptop-service/listAll'));
            foreach ($listAll as $l) {
              foreach ($l as $i) {
  	            echo "<li>$i</li>";
    	        }
  	        }

  	        $listAlljson = json_decode(file_get_contents('http://laptop-service/listAll/json'));
              foreach ($listAlljson as $l) {
                foreach ($l as $i) {
    	            echo "<li>$i</li>";
      	        }
  	        }

  	        $listAllcsv = file_get_contents('http://laptop-service/listAll/csv');
  	        echo "<li>$listAllcsv</li>";


            $listOpen = json_decode(file_get_contents('http://laptop-service/listOpenOnly'));
              foreach ($listOpen as $l) {
                foreach ($l as $i) {
    	            echo "<li>$i</li>";
      	        }
  	        }

  	        $listOpenjson = json_decode(file_get_contents('http://laptop-service/listOpenOnly/json'));
              foreach ($listOpenjson as $l) {
                foreach ($l as $i) {
    	            echo "<li>$i</li>";
      	        }
  	        }

  	        $listOpencsv = file_get_contents('http://laptop-service/listOpenOnly/csv');
  	        echo "<li>$listOpencsv</li>";

            $listClose = json_decode(file_get_contents('http://laptop-service/listCloseOnly'));
              foreach ($listClose as $l) {
                foreach ($l as $i) {
    	            echo "<li>$i</li>";
      	        }
  	        }

            $listClosejson = json_decode(file_get_contents('http://laptop-service/listCloseOnly/json'));
              foreach ($listClosejson as $l) {
                foreach ($l as $i) {
    	            echo "<li>$i</li>";
      	        }
  	        }

  	        $listClosecsv = file_get_contents('http://laptop-service/listCloseOnly/csv');
  	        echo "<li>$listClosecsv</li>";

            ?>
        </ul>
    </body>
</html>
