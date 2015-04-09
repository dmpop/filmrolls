<head
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:700,400' rel='stylesheet' type='text/css'>
</head>
<title>Film Rolls</title>
<div id="content">
<h1>Edit Roll {{no}}</h1>
<form action="/edit/{{no}}" method="GET">
<p>Order no.: <input type="text" name="order_no" value="{{old[1]}}" size="50" maxlength="254"></p>
<p>Date: <input type="text" name="dt" value="{{old[2]}}" size="50" maxlength="100"></p>
<p>Camera: <input type="text" name="camera" value="{{old[3]}}" size="50" maxlength="100"></p>
<p>Film: <input type="text" name="film" value="{{old[4]}}" size="50" maxlength="100"></p>
<p><input type="submit" id="btn" name="save" value="Save"></p>
</form>
<p><a href="/filmrolls">Back</a></p>
</div>
