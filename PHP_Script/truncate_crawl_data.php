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
$sql = "TRUNCATE TABLE crawl_data";

// 쿼리 실행
if ($conn->query($sql) === TRUE) {
    echo "테이블 초기화 완료.\n";
} else {
    echo "에러 발생: " . $conn->error;
}

// compressed 폴더 내 모든 파일 삭제
$folderPath = __DIR__ . '/compressed';  // 삭제할 폴더 경로

if (is_dir($folderPath)) {
    $files = glob($folderPath . '/*'); // 폴더 내의 모든 파일 가져오기

    foreach ($files as $file) {
        if (is_file($file)) {
            unlink($file); // 파일 삭제
        }
    }

    echo "compressed 폴더 내 모든 파일 삭제 완료.\n";
} else {
    echo "compressed 폴더를 찾을 수 없습니다.\n";
}

// 연결 종료
$conn->close();
?>
