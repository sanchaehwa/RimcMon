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
$password = isset($_GET['password']) ? $_GET['password'] : null;

// 업데이트할 새로운 값 
$new_bio = isset($_GET['bio']) && $_GET['bio'] !== '' ? $_GET['bio'] : null;
$new_tool = isset($_GET['tool']) && $_GET['tool'] !== '' ? $_GET['tool'] : null;

if ($name && $password) {
    $stmt = $conn->prepare("UPDATE user_data SET bio = ?, tool = ? WHERE name = ? AND password = ?");
    $stmt->bind_param("ssss", $new_bio, $new_tool, $name, $password);

    // 쿼리 실행
    if ($stmt->execute()) {
        if ($stmt->affected_rows > 0) {
            echo "사용자 정보 업데이트 완료.\n";
        } else {
            echo "업데이트할 데이터가 없습니다.\n";
        }
    } else {
        echo "에러 발생: " . $stmt->error;
    }
    // 스테이트먼트 닫기
    $stmt->close();
}
// 연결 종료
$conn->close();
?>
