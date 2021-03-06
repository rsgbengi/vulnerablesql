<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gatitos</title>
    <link rel="stylesheet" href="static/css/bootstrap5.css">
    <link rel="shortcut icon" href="static/gatito.jpg" type="image/x-icon">
</head>

<body class="text-center">

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">🐱 GATITOS RANDOM</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Flag</a>
                </div>
            </div>
        </div>
    </nav>

    <section class="mt-5">
        <h1>Bienvenido</h1>
        <h2>al generador de gatitos random</h2>
        <p>Disponemos de una enorme base de datos de gatitos generadas por Machine learning</p>
        <!-- Mentira, son solo 50 fotos y están en una carpeta xd -->

        <button onclick="gatoboton()" type="button" class="mt-5 btn btn-lg btn-primary">Generar foto aleatoria</button>

        <div class="card mx-auto mt-5" style="width: 18rem;">
	<img src="data:image/png;base64,<?php echo base64_encode(file_get_contents("static/img/{$_GET['foto']}")); ?>" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Miau miau</h5>
            </div>
        </div>

    </section>
   

</body>

<script src="static/js/bootstrap5.js"></script>
<script src="static/js/script.js"></script>

</html>
