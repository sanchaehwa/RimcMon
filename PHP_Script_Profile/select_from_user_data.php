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

$sql = "SELECT * FROM user_data";
$result = $conn->query($sql);

header('Content-Type: application/json; charset=utf-8'); 

if ($result->num_rows > 0) {
    $data = [];
    // 데이터를 배열로 저장
    while ($row = $result->fetch_assoc()) {
        $data[] = [
            "id" => $row["id"],
            "name" => $row["name"],
            "password" => $row["password"],
            "bio" => $row["bio"],
            "tool" => $row["tool"]
        ];
    }
    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
} else {
    echo json_encode(["message" => "데이터가 없습니다"]);
}

// 연결 종료
$conn->close();
?>
