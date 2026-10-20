# Cập nhật và bổ sung học liệu

Ứng dụng offline không có AI trích xuất/biên soạn PDF tự động. Thêm tài liệu là hai bước: giữ PDF để tra nguồn, rồi biên soạn gói nội dung được kiểm tra và dẫn nguồn. Không đổi PDF thành một chương chính nếu nó chỉ có vai trò bổ trợ.

## Cập nhật gói chạy

1. Xuất sao lưu cá nhân và các PDF bổ sung trước.
2. Đóng cửa sổ server cũ. Giải nén bản mới vào vị trí mong muốn.
3. Mở cùng launcher, cùng trình duyệt và cùng `127.0.0.1:18765`.
4. Nếu dữ liệu không hiện, nhập JSON sao lưu. Không dùng xoá dữ liệu browser để “sửa” khi chưa xuất.

## Bổ sung PDF

Trong **Sao lưu & cập nhật**, chọn PDF. Tệp lưu theo tên trong IndexedDB và ưu tiên khi mở nguồn. Giữ tên duy nhất; thêm tệp trùng tên sẽ thay bản tra cứu của tên đó. Hoặc chép PDF vào `sources/`, không thay đè nguồn cũ nếu nội dung có số trang khác. PDF không nằm trong bản JSON backup, vì có thể rất lớn.

## Gói JSON

Dùng **Xuất học liệu hiện tại** làm mẫu đầy đủ, hoặc nhập một gói một phần với:

```json
{
  "schemaVersion": 1,
  "version": "2026.11.01.1",
  "chapters": [],
  "lessons": [],
  "questions": [],
  "terms": [],
  "essays": [],
  "documents": []
}
```

Các mảng không có thay đổi có thể bỏ qua. Đối tượng cùng ID được thay thế toàn bộ; ID mới được thêm. `documents` ghép theo `file`. Không xoá hay đánh số lại ID bài cũ chỉ để đổi vị trí: done, saved, notes, stats đều gắn với ID. Câu hỏi có thay đổi bản chất nên có ID mới để không dùng nhầm hàng ôn sai cũ. Snapshot đề đã làm giữ câu/lời giải cũ để kết quả lịch sử không bị thay theo học liệu mới.

### Bài học

Có `id`, `chapter`, `title`, `problem`, `technical`, `plain`, `example`, `confusion`, `tradeoff`, `check`, `related`, `terms`, `refs`. Mỗi `refs` có `file`, `start`, `end`, `kind`, tùy chọn `printed`. start/end là trang PDF 1-based. Chỉ ghi printed khi xác minh được trang in.

### Chương

Có `id`, `title`, `source`, `book`, `questions` (câu hỏi lớn), `goals` (hành vi kiểm chứng), `prior` (ID bài tiên quyết), `context`. Chỉ ra mối liên hệ thực tế, không viết mục tiêu chung chung.

### Câu hỏi trắc nghiệm

Có `id`, `lesson`, `chapter`, `level` (Nhận biết/Hiểu/Vận dụng), `prompt`, `options` gồm 4 chuỗi khác nhau, `answer` là chỉ số 0–3, `reasons` gồm 4 giải thích tương ứng, `refs`. Ứng dụng tự đảo thứ tự hiển thị và chấm theo chỉ số gốc. Không dùng vị trí chữ A trong lời giải.

### Thuật ngữ

Có ID ổn định, `name`, `en`, `abbr`, `definition`, `plain`, `example`, `confusion`, `lesson`. Không chỉ dịch tên. Ví dụ cần gắn cơ chế và nêu giới hạn phép ví von.

### Tự luận

Có `id`, `title`, `lessons`, `prompt`, `hints`, `model`, `criteria` (mỗi phần `text`, `max`, tổng 10), `refs`. `examEssaySets` gồm 3 mảng ID, mỗi mảng đúng 3 bài khi muốn thay bộ tự luận. Giữ ít nhất một tình huống phân tích trong từng bộ.

### Tài liệu và độ bao phủ

`documents` có `file` (chỉ tên file, không có thư mục), `pages`, `role`, `imageHeavy` (mảng trang ít chữ), tùy chọn `texts` (mảng trích xuất theo trang).

`coverage` nếu cập nhật cần cung cấp bảng đầy đủ hoặc mở rộng từ bản xuất hiện tại: mỗi hàng gồm `file`, `pdfPage`, `printedPage`, `lessons`, `status`. Nếu bỏ qua, bảng cũ giữ nguyên và tài liệu mới sẽ có thông báo chưa có đối chiếu. Bảng CSV trong thư mục là bản đóng gói gốc, không tự ghi lại khi nhập gói trong trình duyệt; xuất JSON mới để lưu bản cập nhật.

## Ra đề sau bổ sung

Nếu có không quá 40 nhóm có câu hỏi, mỗi nhóm được ưu tiên một câu; phần còn lại ưu tiên trục chương và luân phiên trong ngân hàng cho đủ 40. Khi vượt 40 nhóm, chọn 40 nhóm luân phiên theo tổ hợp; xem ma trận thực tế để biết phạm vi. Mỗi đề vẫn cần đủ ngân hàng và đúng 3 ID tự luận. Import kiểm tra điều này trước khi lưu.

## Kiểm chứng trước phát hành

- Đọc nguồn tại từng trang, xác minh nội dung ảnh/công thức nếu phần chữ chưa đủ.
- Phân biệt tài liệu, diễn giải và ví dụ giả định.
- Kiểm tra câu hỏi chỉ có một lựa chọn đúng, lý do mọi phương án, không sao chép biến thể câu cũ.
- Kiểm tra ID, tiên quyết, liên kết, nguồn và trang.
- So sánh ma trận 3 bộ đề; kiểm tra ít nhất 1 tự luận tình huống mỗi bộ.
- Thử cập nhật bằng bản sao tiến độ, kiểm tra ghi chú vẫn ở đúng ID.
- Với sửa mã nguồn, chạy test; trên Windows mở launcher, PDF, đóng/mở lại và nhập/xuất backup.

Không có chương trình tự kiểm tra tính đúng chuyên môn của mọi câu chữ; schema và tests không thay thế rà soát nội dung.
