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

$name = isset($_GET['name']) ? $_GET['name'] : null;
$bio = isset($_GET['bio']) ? $_GET['bio'] : null;
$tool = isset($_GET['tool']) ? $_GET['tool'] : null;
$password = isset($_GET['password']) ? $_GET['password'] : null;

if ($name && $bio && $tool && $password) {
    // 데이터베이스에 삽입할 SQL 쿼리 작성
    $sql = "INSERT INTO user_data (name, bio, tool, password) VALUES ('" . $conn->real_escape_string($name) . "', 
    '" . $conn->real_escape_string($bio) . "', '" . $conn->real_escape_string($tool) . "', '" . $conn->real_escape_string($password) . "')";

    // 쿼리 실행
    if ($conn->query($sql) === TRUE) {
        echo "레코드 삽입 완료.";
    } else {
        echo "에러: " . $conn->error;
    }
} else {
    echo "유효하지 않은 입력 데이터";
}

// 연결 종료
$conn->close();
?>