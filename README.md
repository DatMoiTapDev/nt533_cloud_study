# NT533 — Cloud & Distributed Computing

**CloudLab** là không gian tự học bằng tiếng Việt dành cho các chủ đề điện toán đám mây và hệ thống tính toán phân tán trong môn NT533. Website kết nối bài giảng, sách tham khảo, ví dụ và bài tập để người học hiểu cơ chế, giải thích lại bằng lời của mình và vận dụng vào tình huống thực tế.

**Website học tập:** [datmoitapdev.github.io/nt533_cloud_study](https://datmoitapdev.github.io/nt533_cloud_study/)

## Môn học giúp tìm hiểu điều gì?

Môn học đi từ câu hỏi vì sao cần nhiều máy tính cùng làm việc đến cách xây dựng, triển khai và vận hành ứng dụng trên hạ tầng phân tán. Các chủ đề liên hệ với nhau: ảo hóa tạo tài nguyên linh hoạt, mạng và lưu trữ nối các thành phần, điều phối duy trì dịch vụ, còn các mô hình lập trình giúp khai thác tài nguyên đó.

Sau khi học, người học hướng tới việc:

- Phân biệt các mô hình dịch vụ và triển khai cloud, giải thích trách nhiệm của từng bên.
- Giải thích cách VM, container, mạng ảo và lưu trữ hỗ trợ ứng dụng.
- Phân tích co giãn, cân bằng tải, chịu lỗi, độ trễ và các nút thắt hiệu năng.
- So sánh MapReduce, microservices và serverless theo yêu cầu bài toán.
- Đánh giá lựa chọn kiến trúc dựa trên hiệu năng, độ tin cậy, chi phí và bảo mật.

## Nội dung học tập

| Nhóm kiến thức | Các chủ đề chính |
| --- | --- |
| Nền tảng cloud | Động lực ra đời, co giãn tài nguyên, IaaS/PaaS/SaaS, private/public/hybrid/multi-cloud |
| Hạ tầng trung tâm dữ liệu | Rack và pod vật lý, điện và làm mát, north-south/east-west, leaf-spine |
| Ảo hóa | Máy ảo, hypervisor, I/O ảo, live migration, container, namespace và Docker |
| Mạng và lưu trữ | Underlay/overlay, VLAN/VXLAN, NAT, SDN; block/file/object, NAS, SAN và HDFS |
| Tự động hóa và vận hành | Infrastructure as Code, orchestration, Kubernetes, controller, CI/CD, DevOps và SRE |
| Lập trình phân tán | Song song dữ liệu, MapReduce/Hadoop, microservices, giao tiếp và service mesh |
| Chủ đề mở rộng | Serverless/FaaS, edge/fog, bảo mật, quyền riêng tư và độ phức tạp hệ thống |
| Tài liệu bổ trợ | Amdahl/Gustafson, cluster HA/HPC/HTC, MPI, OpenFaaS/OpenWhisk, Quantum Cloud và định hướng đồ án NT533 |

Học liệu hiện có **18 chương theo trục slide và 5 mô-đun bổ trợ**, được tổ chức thành **103 bài**, cùng **241 thuật ngữ Việt–Anh**. Có **24 PDF nguồn** và bảng đối chiếu để tra lại nội dung.

## Website có gì?

### Học để hiểu bản chất

Mỗi chương có câu hỏi lớn, mục tiêu kiểm chứng được, kiến thức tiên quyết và liên hệ với các phần khác. Mỗi bài trình bày vấn đề, cơ chế kỹ thuật, cách hiểu gần gũi, ví dụ, điểm dễ nhầm, giới hạn và câu tự kiểm tra.

Thuật ngữ có thể tra bằng tiếng Việt, tiếng Anh hoặc chữ viết tắt. Các mô hình tương tác giúp khám phá định luật Amdahl, nút thắt web/DB, word count MapReduce và xác suất đo qubit đơn.

### Luyện tập và thi thử

- **103 câu trắc nghiệm**, có giải thích đáp án và từng phương án còn lại.
- **3 tổ hợp đề**, mỗi đề đúng **40 câu trắc nghiệm và 3 câu tự luận**.
- Ma trận theo chủ đề/mức độ, đồng hồ, lưu bài đang làm và kết quả sau khi nộp.
- **9 bài tự luận tình huống**, có gợi ý, đáp án tham khảo và rubric để tự đánh giá.
- Thống kê theo chủ đề và danh sách câu sai để quay lại ôn đúng bài.

### Theo dõi việc học

Tìm kiếm toàn bộ bài học, lưu bài, đánh dấu đã học, ghi chú cá nhân và xuất/nhập dữ liệu sao lưu. Tiến độ lưu riêng trong trình duyệt trên từng thiết bị; hiện chưa đồng bộ qua tài khoản.

## Cách sử dụng

Bắt đầu từ mục tiêu chương → ôn tiên quyết → đọc và thử ví dụ → tự diễn giải vào ghi chú → luyện tập → thi thử → quay lại phần còn yếu.

Có thể học trên website hoặc tải repository về và mở `dist/index.html`. Trên Windows, `dist/Mo-CloudLab.cmd` mở bản local; người học không cần cài môi trường lập trình.

Slide là trục nội dung, sách dùng giải thích bổ trợ. Mỗi bài có tên file và số trang để đối chiếu. Số mục trong ứng dụng là số điều hướng theo cụm chủ đề, không tự coi là số mục gốc. Đề trong website phục vụ tự luyện, chưa được xác nhận là đề thi thật của giảng viên; phần tự luận dùng rubric tự chấm.

## Xuất bản và cập nhật

Workflow [Deploy CloudLab to GitHub Pages](.github/workflows/deploy-pages.yml) chạy kiểm thử rồi triển khai thư mục `dist` khi có thay đổi trên `main`; có thể chạy lại bằng **Run workflow** trong tab Actions.

Thiết lập lần đầu: vào **Settings → Pages → Build and deployment → Source → GitHub Actions**. Sau khi chọn nguồn, chạy workflow để xuất bản website.

Hướng dẫn bổ sung học liệu và giữ tiến độ theo ID: [CAP_NHAT.md](dist/docs/CAP_NHAT.md). Kiểm thử mã nguồn: `npm test` (cần Node.js khi bảo trì).
