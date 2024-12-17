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

$author = isset($_GET['author']) ? $_GET['author'] : null;
$title = isset($_GET['title']) ? $_GET['title'] : null;
$content = isset($_GET['content']) ? $_GET['content'] : null;
$category = isset($_GET['category']) ? $_GET['category'] : null;

if ($author && $title && $content && $category) {
    // 데이터베이스에 삽입할 SQL 쿼리 작성
    $sql = "INSERT INTO post_data (author, title, content, category) VALUES ('" . $conn->real_escape_string($author) . "', 
    '" . $conn->real_escape_string($title) . "', '" . $conn->real_escape_string($content) . "', '" . $conn->real_escape_string($category) . "')";

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