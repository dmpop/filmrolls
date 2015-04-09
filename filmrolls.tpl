<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="static/styles.css">
<link href='http://fonts.googleapis.com/css?family=Quicksand:300,400,700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
</head>
<title>Film Roll</title>
<div id="content">
<h1>Film Rolls:</h1>
<p><a href="add">Add Item</a></p>
<table border="0">
<tr><th>ID</th><th>Order no.</th><th>Date</th><th>Camera</th><th>Film</th></tr>
%for row in rows:
    %id = row[0]
    %order_no = row[1]
    %date = row[2]
    %camera = row[3]
    %film = row[4]
    <tr>
    <td class="col1">{{id}}</td>
    <td class="col2">{{order_no}}</td>
    <td>{{date}}</td>
    <td>{{camera}}</td>
    <td>{{film}}</td>
    <td><a href="/edit/{{id}}">Edit</a></td>
    <td><a href="/delete/{{id}}">Delete</a></td>
  </tr>
%end
</table>
</div>
