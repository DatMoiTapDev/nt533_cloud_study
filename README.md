# CloudLab — Học để hiểu

Ứng dụng học Điện toán đám mây bằng tiếng Việt: bài học theo chủ đề, từ điển song ngữ, luyện tập và thi thử.

**Website:** https://cloudlab-hoc-de-hieu.calmgnome10.chatgpt.site

## Nội dung

- 18 chương theo trục slide và 5 mô-đun bổ trợ, tổng 103 bài.
- 241 thuật ngữ Việt–Anh có định nghĩa và ví dụ theo ngữ cảnh.
- 103 câu trắc nghiệm giải thích từng lựa chọn.
- 3 bộ đề, mỗi đề 40 trắc nghiệm + 3 tự luận; rubric để tự chấm.
- Ghi chú, đánh dấu đã học, lưu bài, ôn câu sai, xuất/nhập sao lưu.
- Các ví dụ tương tác về Amdahl, compute/DB, MapReduce và qubit đơn.
- 24 PDF gốc cùng bảng đối chiếu trang nguồn.

## Chạy ứng dụng

Mở `dist/index.html` trong Edge/Chrome, hoặc trên Windows bấm `dist/Mo-CloudLab.cmd`. Không cần cài Node.js/Python để học. Có thể dùng `dist/Tao-shortcut.vbs` để tạo lối tắt Desktop.

Dùng một cách mở cố định: dữ liệu cá nhân lưu riêng theo trình duyệt và địa chỉ web. Bản web cần Internet để tải tài nguyên; bản local dùng tài nguyên trong thư mục. Xuất backup trước khi đổi máy hoặc xoá dữ liệu trình duyệt.

## Cấu trúc

- `dist/`: website tĩnh và bản chạy local.
- `dist/data/`: học liệu JSON và bản nhúng JavaScript.
- `dist/sources/`: PDF để đối chiếu.
- `dist/docs/`: bảng nguồn, hướng dẫn và kết quả test.
- `tools/author.py`: nguồn biên soạn và tạo dữ liệu.
- `tools/test.cjs`: kiểm thử logic và sinh trang.

## Kiểm thử

Cài Node.js để bảo trì rồi chạy `npm test` hoặc `node tools/test.cjs`. 19 nhóm kiểm thử gồm cấu trúc 40+3, chấm khi đảo lựa chọn, backup, hết giờ, hàng câu sai và sinh trang cho mọi bài. Kiểm thử DOM nhẹ không thay kiểm thử trực quan trên trình duyệt hoặc Windows.

Chỉ cần Python và PyMuPDF nếu chạy lại `tools/author.py` để biên soạn dữ liệu. Lệnh này ghi đè các tệp được tạo từ nguồn biên soạn; lưu thay đổi trước khi chạy.

## Cập nhật học liệu

Xem `dist/docs/CAP_NHAT.md`. Giữ ID bài ổn định để không mất liên kết với tiến độ và ghi chú. Sách dùng giải thích bổ trợ, slide là trục. Số bài trong app không tự coi là số mục gốc; mỗi bài có tên file và số trang để tra lại.

Bộ đề phục vụ tự luyện, chưa được xác nhận là đề thi thật. Tự luận tự chấm bằng rubric, không có API chấm AI. Các PDF nguồn giữ thông tin tác giả/xuất xứ của từng tài liệu; không gán giấy phép phần mềm của dự án cho các tài liệu này.
