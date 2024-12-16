<?php
$servername = "localhost";  
$username = "opsw4";       
$password = "opswteam4!";   
$dbname = "opsw4";         

$conn = new mysqli($servername, $username, $password, $dbname);

// 연결 확인
if ($conn->connect_error) {
    die("연결 실패: " . $conn->connect_error);
}

$id = isset($_GET['id']) ? $_GET['id'] : null;
$category = isset($_GET['category']) ? $_GET['category'] : null;

if ($id) {
    $sql = "SELECT id, title, content, author, category FROM post_data WHERE id = ?";
} elseif ($category) {
    $sql = "SELECT id, title, content, author, category FROM post_data WHERE category = ?";
} else {
    echo json_encode(["error" => "id 또는 category를 제공해야 합니다"], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    $conn->close();
    exit;
}

// SQL 실행
$stmt = $conn->prepare($sql);
if ($id) {
    $stmt->bind_param("i", $id); 
} elseif ($category) {
    $stmt->bind_param("s", $category); 
}

$stmt->execute();
$result = $stmt->get_result();

header('Content-Type: application/json; charset=utf-8');

// 결과 반환
if ($result->num_rows > 0) {
    $data = [];
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
} else {
    echo json_encode(["message" => "데이터가 없습니다"], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
}

// 연결 종료
$stmt->close();
$conn->close();
?>