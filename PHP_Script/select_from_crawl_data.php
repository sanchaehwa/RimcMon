<?php
$servername = "localhost";  // 데이터베이스 서버
$username = "opsw4";        // 사용자 이름
$password = "opswteam4!";   // 비밀번호
$dbname = "opsw4";          // 데이터베이스 이름

// MySQL 연결
$conn = new mysqli($servername, $username, $password, $dbname);

// 연결 확인
if ($conn->connect_error) {
    die("연결 실패: " . $conn->connect_error);
}

// SQL 쿼리 작성
$sql = "SELECT * FROM crawl_data";

// 쿼리 실행
$result = $conn->query($sql);

// JSON 출력 설정
header('Content-Type: application/json; charset=utf-8'); 

if ($result->num_rows > 0) {
    $data = [];
    // 데이터를 배열로 저장
    while ($row = $result->fetch_assoc()) {
        $data[] = [
            "id" => $row["id"],
            "title" => $row["title"],
            "date" => $row["date"],
            "image" => $row["image"],
            "page" => $row["page"]
        ];
    }
    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
} else {
    echo json_encode(["message" => "데이터가 없습니다"]);
}

// 연결 종료
$conn->close();
?>
