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

$title = isset($_GET['title']) ? $_GET['title'] : null;
$date = isset($_GET['date']) ? $_GET['date'] : null;
$image = isset($_GET['image']) ? $_GET['image'] : null;

// 데이터 유효성 확인
if ($title && $date && $image) {
    // 압축 이미지를 저장할 폴더 및 파일명 설정
    $compressed_dir = __DIR__ . '/compressed';
    $image_name = basename($image);
    $compressed_path = $compressed_dir . '/' . $image_name;

    // 폴더가 없는 경우 생성
    if (!file_exists($compressed_dir)) {
        mkdir($compressed_dir, 0777, true);
    }

    // cURL로 이미지 다운로드
    $ch = curl_init($image);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    $original_image = curl_exec($ch);

    if (curl_errno($ch)) {
        die("이미지 다운로드 실패: " . curl_error($ch));
    }
    curl_close($ch);

    if (!$original_image) {
        die("해당 URL에서 이미지를 다운로드 할 수 없습니다: $image");
    }

    // 임시 파일로 저장
    $temp_path = $compressed_dir . '/temp_' . $image_name;
    file_put_contents($temp_path, $original_image);

    // 압축 작업
    $image_info = getimagesize($temp_path);
    if ($image_info === false) {
        unlink($temp_path);
        die("이미지 정보 가져오기 실패");
    }

    $compression_quality = 50; // 압축 품질
    switch ($image_info['mime']) {
        case 'image/jpeg':
            $image = imagecreatefromjpeg($temp_path);
            imagejpeg($image, $compressed_path, $compression_quality);
            break;
        case 'image/png':
            $image = imagecreatefrompng($temp_path);
            imagepng($image, $compressed_path, round(9 * (100 - $compression_quality) / 100));
            break;
        case 'image/gif':
            $image = imagecreatefromgif($temp_path);
            imagegif($image, $compressed_path);
            break;
        default:
            unlink($temp_path);
            die("지원하지 않는 이미지 형식입니다.");
    }

    imagedestroy($image);
    unlink($temp_path);
    echo "이미지 압축 완료. ";
    
    // 데이터베이스에 삽입할 SQL 쿼리 작성
    $sql = "INSERT INTO crawl_data (title, date, image) VALUES ('" . $conn->real_escape_string($title) . "', 
    '" . $conn->real_escape_string($date) . "', 'http://opsw4.dothome.co.kr/compressed/" . $conn->real_escape_string($image_name) . "')";
    
    // 쿼리 실행
    if ($conn->query($sql) === TRUE) {
        echo "레코드 삽입 완료. ";
    } else {
        echo "에러: " . $conn->error;
    }
} else {
    echo "유효하지 않은 입력 데이터";
}

// 연결 종료
$conn->close();
?>