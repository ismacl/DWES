<?php
$db = mysqli_connect('localhost', 'root','1234','mysitedb') or die('Fail');
?>
<html>
<style>
	table, th, td {
		border: 1px solid black;
}
</style>
  <body>
<h1>Conexión establecida</h1>
	<table>
		<tr>
			<th>juego_id</th>
			<th>Nombre</th>
			<th>url_imagen</th>
			<th>duracion_h</th>
			<th>desarolladora</th>
		</tr>
	<?php
	//Lanzar una query
	$query = 'SELECT * FROM tJuegos';
	$result= mysqli_query($db, $query) or die ('Query error');
	// Recorrer el resultado
	while ($row = mysqli_fetch_array($result)) {
	  echo $row['nombre'];
	  echo '<tr>';
	  echo '<td><a href="/detail.php?juego_id='.$row [0].'">Nombre:'.$row[1].'</a></td>';
	  echo '<td>'.$row ['nombre'].'</td>';
	  echo '<td><img src="'.$row ['url_imagen'].'"></img></td>';
	  echo '<td>'.$row ['duracion_h'].'</td>';
	  echo '<td>'.$row ['desarolladora'].'</td>';
	  echo '</tr>';
}
	?>
	</table>
  </body>
</html>
