<?php
// C:\Memoire2\Memoire2\prediction.php
header('Content-Type: application/json');

// 1. Lecture de la requête venant de JS
$inputData = file_get_contents('php://input');

if (!$inputData) {
    echo json_encode(['error' => 'Aucune donnée reçue par PHP.']);
    exit;
}

// 2. Traitement de l'argument CLI pour Windows
$escapedJson = escapeshellarg($inputData);

// 3. Emplacement de l'exécutable Python dans ton venv
$pythonExec = __DIR__ . '/.venv/Scripts/python.exe';

// S'il n'existe pas dans .venv, on replie sur 'python' global
if (!file_exists($pythonExec)) {
    $pythonExec = 'python';
}

// 4. Commande pointant vers src/predict.py
$command = "\"{$pythonExec}\" src/predict.py " . $escapedJson . " 2>&1";
$output = shell_exec($command);

// 5. Transmission de la réponse à JavaScript
if ($output === null) {
    echo json_encode(['error' => 'Échec de l\'exécution de la commande shell.']);
} else {
    echo $output;
}
?>