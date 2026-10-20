# Gói chạy và bộ cài Windows

Bản bàn giao là ZIP portable đầy đủ, không cần biên dịch để học. Nó có launcher PowerShell dùng thư viện hệ thống Windows. Chưa có EXE/MSI đã biên dịch hoặc đã ký.

Muốn tạo bộ cài: trên Windows cài Inno Setup theo nguồn chính thức của công cụ, mở `tools/CloudLab.iss` bằng trình biên dịch GUI rồi chọn Compile. Script sẽ chép toàn bộ gói vào thư mục ứng dụng của người dùng và tạo shortcut. File output nằm trong `installer-output/CloudLab-Setup.exe` nếu biên dịch thành công. Đây là cấu hình tham khảo chưa được chạy trong môi trường Linux hiện tại, không phải cam kết bộ cài đã kiểm chứng.

Sau khi biên dịch cần thử trên Windows sạch: cài bằng user thường; mở Desktop shortcut; kiểm tra localhost, PDF và backup; ngắt Internet rồi học/thi; đóng/mở và xác nhận dữ liệu; thử cập nhật bản mới; gỡ ứng dụng. Tiến độ nằm trong browser theo origin, không nằm trong thư mục chương trình và không tự bị gỡ theo phần mềm. Không dọn dữ liệu browser nếu chưa xuất backup.

Nếu chia sẻ bộ cài, rà soát quyền phân phối các PDF. Gói nguồn này được chuẩn bị cho việc tự học từ tài liệu người dùng đã cung cấp.
