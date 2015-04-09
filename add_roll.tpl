<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>Film Rolls</title>
<div id="content">
<h1>Add Roll:</h1>
<form action="/add" method="GET">
<p>Order no.: <input type="text" size="50" maxlength="254" name="order_no"></p>
<p>Date: <input type="text" size="50" maxlength="100" name="dt"></p>
<p>Camera: <input type="text" size="50" maxlength="100" name="camera"></p>
<p>Film: <input type="text" size="50" maxlength="100" name="film"></p>
<p><input type="submit" id="btn" name="add" value="Add"></p>
</form>
<p><a href="/filmrolls">Back</a></p>
</div>
