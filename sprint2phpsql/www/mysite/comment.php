<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
	<body>
	<?php
		$juego_id = $_POST['juego_id'];
		$comentario = $_POST['new_comment'];
		$fecha = $_POST("Y-m-d H:i:s");

		$query = "INSERT INTO tComentarios(comentario, juego_id, usuario_id, fecha) 
VALUES ('".$comentario."',".$juego_id.",NULL, ".$fecha.")";

	mysqli_query($db, $query) or die('Error');

	echo "<p>Nuevo comentario ";
	echo mysqli_insert_id($db);
	echo " añadido</p>";

	echo "<a href='/detail.php?juego_id=".$juego_id."'>Volver</a>";

mysqli_close($db);	
?>
	</body>
</html>
