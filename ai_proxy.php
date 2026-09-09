<?php
// CORS Proxy for ChatGPT-Compatible AI Endpoints
// Enterprise PRD Studio

// Silence standard error output to prevent corrupting JSON payloads
error_reporting(0);
ini_set('display_errors', '0');

// Set generous timeout for complex enterprise LLM generations (6 minutes)
set_time_limit(360);
ini_set('max_execution_time', '360');

// Set complete CORS headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With, Origin, Accept");
header("Access-Control-Max-Age: 86400");

$method = isset($_SERVER['REQUEST_METHOD']) ? strtoupper($_SERVER['REQUEST_METHOD']) : 'GET';

// Handle CORS Preflight
if ($method === 'OPTIONS') {
    http_response_code(200);
    exit();
}

// Handle Health Check Ping (GET)
if ($method === 'GET') {
    header("Content-Type: application/json; charset=utf-8");
    http_response_code(200);
    echo json_encode([
        'status' => 'ok',
        'proxy' => 'Enterprise PRD Studio AI Proxy',
        'php_version' => PHP_VERSION,
        'curl_available' => function_exists('curl_version'),
        'timeout_limit' => 360,
        'timestamp' => time()
    ]);
    exit();
}

// Read raw POST body
$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (!$data || !isset($data['endpoint']) || empty(trim($data['endpoint']))) {
    header("Content-Type: application/json; charset=utf-8");
    http_response_code(400);
    echo json_encode([
        'error' => [
            'message' => 'Missing or invalid endpoint in request payload'
        ]
    ]);
    exit();
}

$targetUrl = trim($data['endpoint']);
$apiKey = isset($data['apiKey']) ? trim($data['apiKey']) : '';
$payload = isset($data['body']) ? json_encode($data['body'], JSON_UNESCAPED_UNICODE) : '';

$ch = curl_init($targetUrl);
$headers = [
    'Content-Type: application/json',
    'Accept: application/json',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) EnterprisePRDStudio/2.0'
];

if (!empty($apiKey)) {
    $headers[] = 'Authorization: Bearer ' . $apiKey;
}

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

// 360 seconds (6 minutes) timeout for intensive long LLM completions
curl_setopt($ch, CURLOPT_TIMEOUT, 360);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 30);

// Keepalive settings to prevent intermediate NAT drops on long generation
curl_setopt($ch, CURLOPT_TCP_KEEPALIVE, 1);
curl_setopt($ch, CURLOPT_TCP_KEEPIDLE, 15);
curl_setopt($ch, CURLOPT_TCP_KEEPINTVL, 15);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

header("Content-Type: application/json; charset=utf-8");

if ($response === false) {
    http_response_code(502);
    echo json_encode([
        'error' => [
            'message' => 'cURL Proxy Connection Failed: ' . ($curlError ?: 'Unknown network error')
        ]
    ]);
    exit();
}

http_response_code($httpCode > 0 ? $httpCode : 200);
echo $response;
