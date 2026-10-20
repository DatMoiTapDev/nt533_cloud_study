"""Nguồn biên soạn học liệu. Chạy python tools/author.py từ thư mục CloudLab."""
import json,pathlib,re,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]/'dist'
C=[]; L=[]; Q=[]; G=[]
files={p.name:p for p in (ROOT/'sources').glob('*.pdf')}
BOOK=next(n for n in files if n.startswith('1. '))

def chapter(id,title,source,book,questions,goals,prior,context):
 C.append(dict(id=id,title=title,source=source,book=book,questions=questions.split('|'),goals=goals.split('|'),prior=prior,context=context))

def lesson(id,title,pages,book,problem,technical,plain,example,confusion,tradeoff,check,quiz,options,reasons,level='Hiểu',terms=''):
 c=C[-1];a,b=(pages if isinstance(pages,tuple) else (pages,pages))
 refs=[dict(file=c['source'],start=a,end=b,kind='slide')]
 if book:
  x,y=(book if isinstance(book,tuple) else (book,book));refs.append(dict(file=BOOK,start=x+19,end=y+19,printed=f'{x}–{y}',kind='book'))
 item=dict(id=id,chapter=c['id'],title=title,refs=refs,problem=problem,technical=technical,plain=plain,example=example,confusion=confusion,tradeoff=tradeoff,check=check,related=[],terms=terms.split('|') if terms else [])
 L.append(item)
 Q.append(dict(id='q-'+id,lesson=id,chapter=c['id'],level=level,prompt=quiz,options=options.split('|'),answer=0,reasons=reasons.split('|'),refs=refs))

def term(name,en,abbr,definition,plain,example,confusion,lesson):
 G.append(dict(id='t-'+hashlib.sha1(en.lower().encode()).hexdigest()[:12],name=name,en=en,abbr=abbr,definition=definition,plain=plain,example=example,confusion=confusion,lesson=lesson))

chapter('c01','Vì sao có điện toán đám mây?','01-motivation(1).pdf',(5,12),'Vì sao thuê dịch vụ thay vì mua máy?|Vì sao cloud cần nhiều máy và mạng?|Đám mây có làm ứng dụng tự chạy song song không?', 'Phân tích một dịch vụ dưới góc nhìn người thuê và nhà cung cấp|Giải thích quan hệ power wall, đa lõi và cluster|Vẽ đường đi yêu cầu qua bộ cân bằng tải và các máy phục vụ',[], 'Đặt nền cho co giãn ở chương 2, hạ tầng ở chương 4 và các mô hình lập trình ở chương 11–14.')
lesson('1.1','Từ sản phẩm CNTT đến dịch vụ',(1,12),(5,6),
'Một doanh nghiệp cần xử lý bảng lương nhưng không muốn tự vận hành cả phòng máy. Vấn đề không chỉ là đặt máy ở đâu, mà là ai chịu trách nhiệm cho từng lớp và tài nguyên được cấp phát như thế nào.',
'Điện toán đám mây (cloud computing) cung cấp khả năng tính toán, lưu trữ hoặc ứng dụng dưới dạng dịch vụ truy cập qua mạng. Người thuê (tenant) sử dụng phần tài nguyên hoặc chức năng được cấp; nhà cung cấp vận hành các lớp nền theo mô hình dịch vụ. Slide nêu sự chuyển dịch từ sản phẩm sang dịch vụ, rồi minh họa doanh nghiệp dùng cloud toàn phần hoặc một phần. Không phải mọi website có đăng nhập đều chứng minh hạ tầng phía sau là một cloud co giãn.',
'Bạn cần kết quả của việc tính toán, tương tự thuê một dịch vụ vận chuyển thay vì mua xe, tuyển tài xế và xây gara. Phép ví von chỉ nói về phân công trách nhiệm: dữ liệu và quyền truy cập vẫn cần bạn quản lý theo dịch vụ đã chọn.',
'Ví dụ tự xây dựng: nhóm làm trang đăng ký môn học. (1) Liệt kê việc cần làm: giao diện, xử lý đăng ký, cơ sở dữ liệu, sao lưu, máy chủ. (2) Nếu thuê máy ảo, nhóm vẫn cài ứng dụng và quản trị dữ liệu. (3) Nếu dùng phần mềm đăng ký có sẵn, nhà cung cấp vận hành nhiều lớp hơn. (4) Đánh giá bằng chức năng, chi phí và khả năng xuất dữ liệu, không chỉ bằng chữ “cloud”.',
'Truy cập qua Internet không đồng nghĩa được phép xem dữ liệu của mọi khách hàng. Public cloud nói về dịch vụ cung cấp cho nhiều khách hàng; quyền truy cập từng dữ liệu là vấn đề khác. Xem 3.1 và 17.3.',
'Thuê dịch vụ giảm một số công việc vận hành nhưng tạo phụ thuộc vào mạng, nhà cung cấp và điều khoản dịch vụ. Thiết bị di động có thể đẩy tác vụ nặng lên cloud nhưng vẫn chịu độ trễ và mất kết nối.',
'Hãy lấy một ứng dụng bạn dùng, liệt kê ba việc nhà cung cấp làm và hai việc bạn vẫn phải làm. Nếu mất mạng, chức năng nào còn chạy được?',
'Nhóm thuê một máy ảo để chạy trang đăng ký môn học. Điều nào có thể kết luận?',
'Nhà cung cấp vận hành hạ tầng vật lý, nhóm vẫn có trách nhiệm với ứng dụng|Nhóm không cần quản lý mật khẩu ứng dụng nữa|Mọi dữ liệu trên máy ảo trở thành công khai|Ứng dụng tự động chạy song song trên mọi máy',
'Đúng: thuê một lớp tài nguyên không chuyển hết trách nhiệm ở lớp trên.|Sai: tài khoản và quyền trong ứng dụng vẫn cần quản lý.|Sai: public cloud không có nghĩa public data.|Sai: kiến trúc và phân chia công việc quyết định khả năng song song.',terms='cloud computing|tenant')
lesson('1.2','Power wall, đa lõi và giới hạn một máy',(13,20),(7,8),
'Vì sao không cứ tăng xung nhịp CPU để đáp ứng nhu cầu lớn hơn? Công suất và nhiệt làm cách tăng tốc này gặp giới hạn.',
'Bức tường công suất (power wall) mô tả giới hạn thực tế khi tăng hiệu năng đơn luồng bằng cách tăng xung nhịp và độ phức tạp gây tiêu thụ điện, sinh nhiệt cao. Đa lõi cung cấp thêm đơn vị thực thi, nhưng phần mềm phải có công việc độc lập để dùng chúng. Slide dùng các thế hệ siêu máy tính minh họa chuyển từ bộ xử lý chuyên biệt sang nhiều thành phần phổ thông; đây là ví dụ lịch sử, không phải bảng xếp hạng hiện tại.',
'Một đầu bếp không thể liên tục nấu nhanh gấp đôi chỉ bằng làm việc nhanh hơn. Có thêm đầu bếp chỉ hữu ích nếu có thể chia việc; một nồi phải nấu theo thứ tự vẫn là giới hạn.',
'Ví dụ tự xây dựng: xử lý 1.000 ảnh độc lập có thể chia cho 8 lõi. Ngược lại, bước tính kết quả thứ i bắt buộc đợi kết quả i−1 không thể chia theo cách đó. Đo thời gian toàn chương trình, kể cả đọc ảnh và gom kết quả; đừng chỉ đo đoạn tính trên lõi.',
'Đa lõi không đồng nghĩa chương trình đơn luồng tự tăng tốc. Số lõi và hiệu năng mỗi lõi là hai đại lượng khác nhau. Xem định luật Amdahl ở F1.4.',
'Tăng số lõi có thể làm lộ nút thắt bộ nhớ, khóa đồng bộ hoặc I/O. Cần đo tải và chọn cách phân rã phù hợp.',
'Vì sao chương trình có một khóa toàn cục có thể tăng tốc rất ít dù dùng CPU nhiều lõi?',
'Thêm lõi CPU ít giúp chương trình khi nào?',
'Phần lớn công việc phải thực hiện tuần tự|Có nhiều ảnh độc lập cùng kích thước|Mỗi tác vụ dùng dữ liệu riêng và không chờ nhau|Công việc được chia đều và chi phí đồng bộ nhỏ',
'Đúng: phần tuần tự giới hạn tăng tốc.|Đây thường là cơ hội chia tải.|Tính độc lập thuận lợi cho song song.|Đây là điều kiện thuận lợi, không giải thích tăng tốc ít.',terms='power wall|multicore')
lesson('1.3','Cluster và máy chủ dạng rack',(21,29),(8,10),
'Khi một máy không đủ, cần kết nối nhiều máy mà vẫn quản lý được không gian, dây mạng, điện và làm mát.',
'Cụm máy tính (cluster) kết hợp các nút độc lập qua mạng để cùng cung cấp dịch vụ hoặc xử lý công việc. Mỗi nút có CPU, bộ nhớ và hệ điều hành riêng. Rack chuẩn hóa chỗ lắp thiết bị theo đơn vị U; switch kết nối các máy. Chuẩn hóa cơ khí không làm mất chi phí mạng: dữ liệu giữa máy phải đi qua giao diện và liên kết có băng thông, độ trễ hữu hạn.',
'Có thêm nhiều bàn làm việc trong cùng văn phòng không có nghĩa mọi người dùng chung một cuốn sổ tức thì. Họ phải trao đổi thông tin; mạng chính là phương tiện trao đổi ấy.',
'Ví dụ tự xây dựng: 4 máy, mỗi máy xử lý một phần tập ảnh. (1) Chia danh sách ảnh. (2) Gửi công việc. (3) Mỗi nút xử lý bằng bộ nhớ của nó. (4) Gom kết quả qua mạng. Nếu tất cả phải tải cùng lúc từ một ổ đĩa chậm thì ổ đĩa là nút thắt, dù CPU còn rảnh.',
'Cluster không phải một CPU khổng lồ với bộ nhớ truy cập đồng nhất. Rack là cách bố trí vật lý; Kubernetes Pod ở chương 10 là đơn vị phần mềm, khác pod hạ tầng ở chương 4.',
'Chi phí mua từng máy phổ thông có thể thấp nhưng còn chi phí mạng, vận hành và phần mềm phân tán. Hỏng một nút không tự động được xử lý nếu chưa có cơ chế phục hồi.',
'Vẽ bốn nút và chỉ ra đường đi dữ liệu từ nơi lưu ảnh đến từng nút. Chỗ nào có thể bị nghẽn?',
'Trong cluster bộ nhớ phân tán, dữ liệu ở nút A cần được nút B dùng thì thường phải làm gì?',
'Trao đổi dữ liệu qua mạng hoặc một dịch vụ lưu trữ chung|Đọc trực tiếp RAM của A như RAM cục bộ không mất chi phí|Chỉ tăng số rack|Chỉ cài cùng hệ điều hành là dữ liệu tự xuất hiện',
'Đúng: phải có đường truyền dữ liệu cụ thể.|Sai: không gian bộ nhớ độc lập, mạng có chi phí.|Sai: rack không chuyển dữ liệu.|Sai: cùng OS không tạo bộ nhớ dùng chung.',terms='cluster|rack')
lesson('1.4','Kinh tế quy mô và nhiều người thuê',(30,37),(10,12),
'Một phòng máy riêng thường được mua theo tải đỉnh nhưng có nhiều giờ nhàn rỗi. Làm sao dùng năng lực đó hiệu quả hơn?',
'Tập trung máy phổ thông tạo cơ hội mua theo số lượng, chuẩn hóa vận hành và dùng đội ngũ chuyên môn chung. Cloud chia sẻ hạ tầng cho nhiều tenant để gộp nhu cầu khác nhau và nâng tỷ lệ sử dụng. Chi phí vốn (CAPEX, Capital Expenditure) khác chi phí vận hành (OPEX, Operating Expenditure). Lợi ích kinh tế phụ thuộc mức dùng, giá thuê, truyền dữ liệu, công sức quản trị và khả năng cách ly.',
'Nhiều hộ dùng chung hệ thống cấp nước có thể tránh mỗi hộ xây một hệ thống riêng. Nhưng phải đo lượng dùng và ngăn một hộ ảnh hưởng hộ khác; chia sẻ tài nguyên tính toán cũng cần đo đếm và cách ly.',
'Ví dụ tự xây dựng: hai nhóm cần 8 máy, một nhóm cao điểm ban ngày, nhóm kia ban đêm. Nếu không trùng đỉnh và được phép chia sẻ, một pool 8 máy có thể phục vụ cả hai theo thời gian. Nếu cùng tăng lên 8 máy một lúc, pool đó không đủ: cần dự phòng, xếp hàng hoặc thêm tài nguyên.',
'Gộp nhu cầu không làm tổng năng lực trở nên vô hạn. Giá mỗi giờ thấp không đủ kết luận tổng chi phí thấp. Cần so cùng mức dịch vụ và thời gian sử dụng.',
'Chia sẻ có thể tạo noisy neighbor và rủi ro cách ly. Không phải mọi tải đều tiết kiệm hơn trên public cloud, nhất là tải ổn định dùng hết máy dài hạn.',
'Bạn cần biết thêm những khoản chi nào ngoài tiền CPU để so sánh thuê và tự mua?',
'Hai tenant cùng có tải đỉnh trùng giờ. Tại sao không thể luôn giảm một nửa năng lực bằng gộp tải?',
'Vì tổng nhu cầu đồng thời vẫn có thể bằng tổng hai tải đỉnh|Vì cloud không hỗ trợ nhiều tenant|Vì CAPEX và OPEX là cùng một khoản|Vì máy phổ thông không thể chạy dịch vụ web',
'Đúng: thống kê lệch đỉnh là điều kiện, không phải bảo đảm.|Sai: multi-tenancy là động lực chính.|Sai: mua tài sản và vận hành khác nhau.|Sai: máy phổ thông có thể phục vụ web.',level='Vận dụng',terms='multi-tenancy|CAPEX|OPEX')
lesson('1.5','Ứng dụng phân tán và cân bằng tải',(38,44),(8,9),
'Nhiều máy có sẵn nhưng một chương trình duy nhất vẫn quá tải. Cần tổ chức yêu cầu và trạng thái để thêm máy thực sự hữu ích.',
'Bộ cân bằng tải (load balancer) nhận yêu cầu và chọn một bản sao phục vụ phía sau. Các bản sao có thể xử lý yêu cầu độc lập khi trạng thái được chia sẻ đúng hoặc không phụ thuộc vào bộ nhớ riêng của một bản sao. Dịch vụ web phân tán còn có cơ sở dữ liệu, cache và các thành phần giao tiếp. Năng lực toàn hệ thống bị giới hạn bởi nút thắt chậm nhất, không chỉ tầng web.',
'Quầy hướng dẫn phân khách sang các quầy phục vụ. Nếu mọi quầy đều phải xin một người duyệt duy nhất thì thêm quầy vẫn có thể không tăng tốc.',
'Ví dụ tự xây dựng: 1 máy web xử lý 100 yêu cầu/giây; cơ sở dữ liệu chịu được 150 yêu cầu/giây với một truy vấn mỗi yêu cầu. Thêm 1 máy web làm trần web lên khoảng 200, nhưng toàn hệ vẫn tối đa khoảng 150 theo giả định. Nếu phiên đăng nhập chỉ ở RAM máy đầu tiên, yêu cầu sang máy thứ hai có thể mất phiên; phải thiết kế lưu phiên hoặc định tuyến phù hợp.',
'Cân bằng tải chia yêu cầu; nó không tự chia nhỏ một tác vụ CPU đơn lẻ. Replication không thay thế backup và không tự giải quyết nhất quán dữ liệu.',
'Cần kiểm tra sức khỏe bản sao, xử lý lỗi và quyết định nơi giữ trạng thái. Lợi ích mở rộng có thể bị lấn bởi chi phí phối hợp.',
'Với ví dụ 150 yêu cầu/giây ở cơ sở dữ liệu, thêm 10 máy web có làm hệ thống xử lý 1.000 yêu cầu/giây được không? Nêu giả định.',
'Web có 4 bản sao, mỗi bản sao 100 yêu cầu/giây; DB giới hạn 180 yêu cầu/giây. Mỗi yêu cầu dùng DB một lần. Trần hợp lý là bao nhiêu?',
'Không quá khoảng 180 yêu cầu/giây theo các giả định|400 yêu cầu/giây bất kể DB|720 yêu cầu/giây|Vô hạn vì có load balancer',
'Đúng: DB là nút thắt.|Sai: chỉ tính tầng web bỏ qua DB.|Sai: không nhân năng lực hai tầng.|Sai: cân bằng tải không tạo năng lực vô hạn.',level='Vận dụng',terms='load balancer|distributed application')

chapter('c02','Co giãn và các mô hình dịch vụ','02-elastic-computing(1).pdf',(15,22),'Co giãn khác mở rộng thế nào?|Ảo hóa giúp cấp phát nhanh ra sao?|Ai quản lý lớp nào trong IaaS, PaaS, SaaS?', 'Phân biệt scalability với elasticity bằng đồ thị tải|Phân chia trách nhiệm cho ba mô hình dịch vụ|Phân tích lợi ích và giới hạn của cấp phát bằng phần mềm',['1.1','1.4'], 'Liên kết VM, container và orchestration; mô hình dịch vụ quyết định việc bạn phải vận hành.')
lesson('2.1','Co giãn theo nhu cầu',(1,7),(15,17),'Tải thay đổi theo giờ khiến mua máy theo đỉnh gây lãng phí còn mua theo trung bình gây quá tải.',
'Tính co giãn (elasticity) là khả năng tăng và giảm tài nguyên cấp phát khi nhu cầu thay đổi. Khả năng mở rộng (scalability) nói hệ thống có thể tận dụng thêm tài nguyên để phục vụ tải lớn hơn. Ảo hóa cung cấp đối tượng có thể tạo, xóa và cấu hình bằng phần mềm; bộ điều khiển và chính sách mới quyết định khi nào thay đổi. Co giãn có độ trễ và cần năng lực vật lý còn trống.',
'Có thể kê thêm bàn là khả năng mở rộng; kê vào và dọn ra đúng lúc theo lượng khách là co giãn.',
'Ví dụ tự xây dựng: tải tăng từ 100 lên 500 yêu cầu/giây lúc 8 giờ. Một bản sao chịu 100 nhưng mất 2 phút để sẵn sàng. Tăng số lượng sau khi quá tải bắt đầu có thể làm hàng đợi tăng trong 2 phút; nếu biết lịch, có thể cấp trước. Khi tải giảm, thu hồi máy phải chờ yêu cầu đang chạy.',
'Scale-out là thêm bản sao; scale-up là tăng năng lực một máy. Không phải cứ bật autoscaling là ứng dụng stateful mở rộng an toàn.',
'Tăng giảm quá nhạy gây dao động; phản ứng quá chậm bỏ lỡ đỉnh tải. Xem 13.2 về độ trễ vòng điều khiển.',
'Vì sao một ứng dụng mở rộng tốt vẫn có thể co giãn kém?',
'Ứng dụng tăng từ 2 lên 8 bản sao khi tải cao và về 2 khi tải thấp. Thuộc tính nổi bật là gì?',
'Co giãn theo nhu cầu|Chỉ tăng xung nhịp|Loại bỏ hoàn toàn độ trễ|Không còn cần hạ tầng vật lý',
'Đúng: cả tăng lẫn giảm theo tải.|Sai: đang thay số bản sao.|Sai: tạo bản sao vẫn mất thời gian.|Sai: mọi bản sao dùng tài nguyên thật.',terms='elasticity|scalability')
lesson('2.2','Ảo hóa phục vụ nhà cung cấp và khách hàng',(8,16),(17,18),'Phân bổ lại máy vật lý cho từng khách hàng bằng tay mất nhiều thời gian và gây gián đoạn.',
'Máy ảo (Virtual Machine, VM) đóng gói trạng thái máy tính và được hypervisor cấp CPU, RAM, I/O. Nhà cung cấp bố trí nhiều VM trên một máy, giám sát và di chuyển chúng để cân tải hoặc bảo trì. Khách hàng chọn hệ điều hành và ứng dụng trong giới hạn dịch vụ. Cách ly là mục tiêu thiết kế quan trọng; không phải lời bảo đảm tuyệt đối trước mọi lỗi phần mềm.',
'Khách thuê thấy một “máy riêng” có các tài nguyên đã cấp, dù bên dưới máy chủ đang phục vụ nhiều khách.',
'Ví dụ tự xây dựng: máy A quá tải, máy B còn RAM. Trước khi chuyển VM từ A sang B phải xét CPU tương thích, lượng RAM, khả năng truy cập đĩa và kết nối mạng; chỉ thấy B rảnh CPU chưa đủ.',
'VM không đồng nghĩa emulator phải dịch từng lệnh. Ảo hóa hỗ trợ phần cứng có thể chạy nhiều lệnh trực tiếp. Live migration không có nghĩa không có bất cứ khoảng dừng nào.',
'Overcommit có thể tăng mức sử dụng nhưng gây tranh chấp. Di chuyển VM tiêu tốn băng thông và không cứu được mọi lỗi đột ngột.',
'Liệt kê ba điều kiện cần xem trước khi chuyển một VM sang máy khác.',
'Nhà cung cấp muốn chuyển VM sang máy B. Thông tin nào ngoài CPU rảnh là thiết yếu?',
'RAM, khả năng truy cập lưu trữ và kết nối mạng của VM|Màu vỏ máy B|Tên đăng nhập của mọi người dùng web|Độ phân giải màn hình người quản trị',
'Đúng: VM cần đủ các tài nguyên và duy trì đường I/O.|Không quyết định khả năng chạy VM.|Không phải điều kiện kỹ thuật của migration.|Không liên quan.',level='Vận dụng',terms='VM|hypervisor')
lesson('2.3','Hạ tầng như dịch vụ — IaaS',(17,24),(18,19),'Nhóm muốn tự chọn OS và cài phần mềm nhưng không muốn mua, đấu nối và sửa máy vật lý.',
'Hạ tầng như dịch vụ (Infrastructure as a Service, IaaS) cung cấp tài nguyên như máy ảo, mạng và lưu trữ. Nhà cung cấp vận hành các lớp hạ tầng theo hợp đồng; khách hàng thường quản trị hệ điều hành khách, middleware, ứng dụng và dữ liệu. Slide xếp các mô hình theo lớp để giải thích trách nhiệm; ranh giới có thể chồng lấn ở dịch vụ cụ thể.',
'Thuê mặt bằng với điện nước có sẵn: bạn còn phải bố trí và vận hành công việc bên trong. Ví von không mô tả đầy đủ trách nhiệm an ninh.',
'Ví dụ tự xây dựng: thuê VM Linux rồi cài web server và DB. Nhà cung cấp sửa phần cứng, còn bạn cập nhật gói trong guest OS, đặt quyền DB và sao lưu dữ liệu.',
'IaaS không phải thuê phần mềm hoàn thiện. Có firewall ở hạ tầng cũng không vá lỗi SQL injection trong ứng dụng.',
'Linh hoạt cao đi cùng nhiều việc vận hành. Cần cộng thời gian quản trị vào tổng chi phí.',
'Nếu guest OS chưa vá bảo mật, vì sao không thể mặc định nhà cung cấp IaaS sẽ tự vá giúp?',
'Trong cách phân lớp IaaS ở bài học, việc nào thường do khách hàng đảm nhận?',
'Cập nhật hệ điều hành khách và ứng dụng|Thay quạt máy chủ vật lý|Bảo trì nguồn điện trung tâm dữ liệu|Sửa cáp mạng vật lý trong rack',
'Đúng: đó là lớp khách hàng quản lý.|Thường thuộc nhà cung cấp.|Thường thuộc nhà cung cấp.|Thường thuộc nhà cung cấp.',terms='IaaS')
lesson('2.4','Nền tảng như dịch vụ — PaaS',(25,29),(19,20),'Nhóm chỉ muốn đưa mã ứng dụng lên môi trường chạy đã được vận hành sẵn.',
'Nền tảng như dịch vụ (Platform as a Service, PaaS) cung cấp runtime, thư viện, công cụ triển khai và quản lý một phần hạ tầng. Nhà phát triển tập trung vào mã và dữ liệu nhưng phải tuân theo các ngôn ngữ, giao diện và giới hạn nền tảng. Slide dùng Elastic Beanstalk minh họa theo phiên bản tài liệu, không phải danh mục tính năng hiện tại.',
'Có sẵn một nhà bếp vận hành theo quy định; bạn mang công thức phù hợp vào nấu thay vì tự xây cả bếp.',
'Ví dụ tự xây dựng: ứng dụng cần một module kernel tùy biến. PaaS không cho sửa kernel có thể không phù hợp; chọn IaaS hoặc thay yêu cầu, thay vì chỉ so giá mỗi giờ.',
'PaaS không miễn mọi trách nhiệm bảo mật: logic ứng dụng, bí mật và quyền dữ liệu vẫn cần quản lý. PaaS cũng không đồng nghĩa không dùng VM ở bên dưới.',
'Giảm việc vận hành đổi lấy ít quyền kiểm soát và nguy cơ phụ thuộc API riêng.',
'Vì sao một ứng dụng cũ chạy trên VM chưa chắc chuyển nguyên trạng lên PaaS được?',
'Ứng dụng bắt buộc sửa kernel, còn PaaS cấm sửa kernel. Kết luận phù hợp là gì?',
'Cần đổi thiết kế hoặc chọn lớp dịch vụ cho phép yêu cầu đó|PaaS chắc chắn chạy được mọi chương trình|Chỉ cần thêm RAM là sửa được giới hạn API|SaaS luôn cho quyền kernel cao hơn IaaS',
'Đúng: phải kiểm tra tính phù hợp nền tảng.|Sai: PaaS có phạm vi hỗ trợ.|Sai: tài nguyên không thay đổi quyền quản trị.|Sai: SaaS thường giảm quyền can thiệp.',level='Vận dụng',terms='PaaS|vendor lock-in')
lesson('2.5','Phần mềm như dịch vụ — SaaS và ranh giới trách nhiệm',(30,33),(20,22),'Người dùng cần chức năng hoàn chỉnh như thư điện tử, không cần tự phát triển ứng dụng.',
'Phần mềm như dịch vụ (Software as a Service, SaaS) cung cấp ứng dụng hoàn chỉnh, thường truy cập qua web hoặc ứng dụng khách. Khách hàng quản lý tài khoản, quyền và dữ liệu theo khả năng dịch vụ. Trang 30–31 của slide ghi “Service as a Service”; ở đây dùng tên chuẩn Software as a Service, phù hợp sách mục 2.10. Đồng bộ và sẵn sàng là tính năng cần được triển khai, không tự được bảo đảm chỉ nhờ gắn nhãn SaaS.',
'Bạn sử dụng một dịch vụ hoàn chỉnh thay vì tự lắp các lớp để có chức năng đó. Vẫn phải kiểm soát ai được dùng và dữ liệu nào được chia sẻ.',
'Ví dụ tự xây dựng: nhóm dùng trình soạn thảo cộng tác. Hai người sửa cùng đoạn cần cơ chế xử lý đồng thời; việc ứng dụng chạy trên IaaS không tự loại bỏ xung đột.',
'SaaS không phải “mọi dữ liệu luôn giống nhau và không bao giờ xung đột”. DaaS trong sách là Desktop as a Service: cung cấp môi trường desktop từ xa; không phải mọi cách dùng chữ DaaS đều mang nghĩa này.',
'Tùy chỉnh, xuất dữ liệu và tích hợp có thể bị giới hạn. Cần thử quy trình sao lưu và rời dịch vụ.',
'Vẽ bảng trách nhiệm OS, runtime, ứng dụng, tài khoản cho IaaS, PaaS, SaaS.',
'Phát biểu nào về SaaS cần tránh?',
'Chỉ cần chạy trên IaaS thì tự động không có xung đột dữ liệu|Nhà cung cấp vận hành ứng dụng hoàn chỉnh|Người dùng vẫn cần đặt quyền chia sẻ|Khả năng xuất dữ liệu cần được đánh giá',
'Đúng: đây là suy luận sai; nhất quán cần cơ chế riêng.|Đây là đặc trưng hợp lý.|Đây là trách nhiệm thực tế.|Đây là đánh đổi cần xem xét.',terms='SaaS|DaaS')

chapter('c03','Public, private, hybrid và multi-cloud','03-clouds(1).pdf',(25,32),'Ai sở hữu và vận hành hạ tầng?|Khi nào cần kết hợp nhiều môi trường?', 'Phân loại một kiến trúc theo mô hình triển khai|Phân tích lợi ích kinh tế, chuyên môn và phụ thuộc nhà cung cấp',['2.3','2.4','2.5'], 'Dùng cùng mô hình dịch vụ trên nhiều kiểu triển khai; chuẩn bị cho edge và bảo mật.')
lesson('3.1','Private cloud và public cloud',(1,13),(25,29),'Tổ chức cần cân bằng kiểm soát, năng lực vận hành và khả năng thuê tài nguyên.',
'Private cloud dành cho một tổ chức, tập trung tài nguyên và quản lý theo mô hình cloud. Public cloud cung cấp dịch vụ cho nhiều khách hàng từ hạ tầng nhà cung cấp. Vị trí trong hay ngoài tòa nhà không phải tiêu chí duy nhất. Private cloud có thể giữ kiểm soát và khả năng quan sát, nhưng tổ chức phải có năng lực và quy trình để sử dụng quyền kiểm soát đó.',
'“Riêng” nói về phạm vi phục vụ tổ chức; “công cộng” nói về thị trường cung cấp dịch vụ, không nói dữ liệu được mở công khai.',
'Ví dụ tự xây dựng: trường tự vận hành một pool VM phục vụ các khoa bằng cổng tự cấp phát là private cloud. Thuê VM từ nhà cung cấp là public cloud, dù các VM chỉ có địa chỉ IP riêng.',
'Mạng riêng trong public cloud không tự biến toàn bộ dịch vụ thành private cloud. Một phòng máy quản lý thủ công cũng chưa thể hiện đầy đủ tính chất cloud.',
'Private giữ quyền điều chỉnh nhưng phải đầu tư nhân lực và dự phòng. Public giảm việc quản lý vật lý nhưng phụ thuộc kết nối và nhà cung cấp.',
'Phân biệt phạm vi sử dụng hạ tầng với phạm vi truy cập một cơ sở dữ liệu.',
'VM thuê từ public cloud chỉ có IP riêng. Đây có tự trở thành private cloud của doanh nghiệp không?',
'Không; địa chỉ riêng không đổi mô hình cung cấp hạ tầng|Có; mọi IP riêng đều là private cloud|Có; cứ có mật khẩu là private cloud|Không; vì public cloud bắt buộc công khai dữ liệu',
'Đúng: cần phân biệt mô hình triển khai với địa chỉ mạng.|Sai: IP là lớp mạng.|Sai: mật khẩu là cơ chế xác thực.|Sai: public cloud vẫn hỗ trợ dữ liệu riêng.',terms='private cloud|public cloud')
lesson('3.2','Lợi thế và khóa chặt nhà cung cấp',(14,24),(27,29),'Một dịch vụ hấp dẫn lúc bắt đầu có thể rất khó rời đi khi dữ liệu và ứng dụng đã phụ thuộc vào nó.',
'Public cloud có thể tận dụng kinh tế quy mô, đội ngũ chuyên môn và dịch vụ cấp cao. Khóa chặt nhà cung cấp (vendor lock-in) xuất hiện khi việc chuyển đổi tốn kém vì API, định dạng dữ liệu, dịch vụ phụ thuộc hoặc chi phí di chuyển. Ưu thế chuyên môn làm giảm một số rủi ro nhưng không loại bỏ sự cố; slide dẫn báo cáo hậu sự cố để minh họa.',
'Dùng một bộ dụng cụ chuyên dụng giúp làm việc nhanh nhưng có thể khiến phụ kiện khó thay bằng hãng khác.',
'Ví dụ tự xây dựng: ứng dụng gọi một API truy vấn riêng và lưu 10 TB dữ liệu. Kế hoạch rời dịch vụ phải tính chuyển truy vấn, xuất dữ liệu, truyền mạng và chạy thử kết quả, không chỉ chép mã nguồn.',
'Open source không tự động loại bỏ lock-in nếu kiến trúc phụ thuộc dịch vụ hoặc quy trình riêng. Chạy container cũng chưa bảo đảm DB và IAM tương thích.',
'Tính di động thường cần đầu tư lớp trừu tượng và kiểm thử nhiều môi trường; đôi khi dùng tính năng riêng vẫn đáng giá nếu lợi ích đủ lớn.',
'Nêu ba phép thử để biết bạn thực sự có thể chuyển nhà cung cấp.',
'Biện pháp nào kiểm chứng tốt nhất khả năng rời một dịch vụ lưu trữ?',
'Thử xuất dữ liệu và khôi phục trên môi trường thay thế|Chỉ đọc tên định dạng trong quảng cáo|Chỉ đóng gói frontend vào container|Mua thêm dung lượng ở cùng nhà cung cấp',
'Đúng: kiểm chứng cả dữ liệu, công cụ và quy trình.|Chưa chứng minh khả năng dùng lại.|Không xử lý phụ thuộc lưu trữ.|Không làm giảm phụ thuộc.',level='Vận dụng',terms='vendor lock-in')
lesson('3.3','Hybrid cloud và multi-cloud',(25,31),(30,32),'Một môi trường có thể không đáp ứng cùng lúc yêu cầu về kiểm soát và tải tăng đột biến.',
'Hybrid cloud kết hợp private và public để phục vụ các phần công việc có quan hệ. Multi-cloud sử dụng nhiều nhà cung cấp cloud. Hai khái niệm không loại trừ nhau. Cloud bursting đẩy phần tải vượt năng lực riêng sang public cloud nhưng cần dữ liệu, kết nối, định danh và cách triển khai tương thích.',
'Có thể làm việc thường ngày tại cơ sở riêng và thuê thêm nơi xử lý khi bận. Chỉ thuê hai hãng ngoài không tự có nghĩa đã kết hợp private với public.',
'Ví dụ tự xây dựng: dữ liệu gốc ở private, tác vụ phân tích đã được phép sử dụng chạy ở public. Phải tính thời gian chuyển dữ liệu và giới hạn truy cập. Nếu phân tích cần đọc liên tục dữ liệu xa thì mạng có thể xóa lợi ích tăng CPU.',
'Có hai cloud không tự có failover. Nếu DNS, khóa bí mật hoặc DB chung bị lỗi, cả hai bên vẫn dừng.',
'Tăng lựa chọn và dự phòng đi kèm chi phí đồng bộ, kỹ năng nhiều nền tảng và vận hành phức tạp.',
'Một hệ thống dùng private cùng hai public cloud có thể đồng thời là hybrid và multi-cloud không? Giải thích.',
'Dùng hai public cloud nhưng không dùng private cloud được mô tả rõ nhất là gì?',
'Multi-cloud|Bắt buộc hybrid cloud|Một VM có hai card mạng|SaaS vì có hai nhà cung cấp',
'Đúng: nhiều nhà cung cấp cloud.|Sai: hybrid ở bài này cần kết hợp private và public.|Sai: đó là cấu hình mạng một máy.|Sai: mô hình dịch vụ là trục phân loại khác.',terms='hybrid cloud|multi-cloud')

chapter('c04','Bên trong trung tâm dữ liệu','04-infrastructure(1).pdf',(37,51),'Rack, pod vật lý và mạng liên kết ra sao?|Điện, nhiệt và lưu lượng giới hạn mở rộng như thế nào?', 'Phân biệt pod hạ tầng với Pod Kubernetes|Theo vết east-west và north-south|Giải thích leaf-spine, liên kết gộp và dự phòng',['1.3'], 'Đây là nền vật lý của mạng ảo, lưu trữ và mọi cơ chế co giãn.')
lesson('4.1','Rack, aisle và pod hạ tầng',(1,15),(37,38),'Quản lý từng máy riêng lẻ không đủ khi mở rộng lên hàng nghìn máy.',
'Rack giữ thiết bị; aisle là lối giữa hàng rack. Pod hạ tầng nhóm rack, mạng, điện và làm mát thành đơn vị thiết kế có khả năng mở rộng dự đoán được. Kích thước pod phụ thuộc công suất, mạng và tổ chức công việc. Tài nguyên trong pod vẫn hữu hạn.',
'Pod giống một khối nhà có các đường cấp dịch vụ riêng, giúp mở rộng theo khối thay vì thêm từng chi tiết tùy tiện.',
'Ví dụ tự xây dựng: thêm 10 rack làm CPU đủ nhưng nguồn điện pod đã đạt giới hạn. Không thể chỉ cắm thêm máy; phải thiết kế lại cấp nguồn hoặc thêm pod.',
'Pod vật lý ở đây khác Pod Kubernetes gồm container. Không dùng tên giống nhau để suy ra cấu tạo giống nhau.',
'Pod lớn tận dụng tập trung nhưng tăng phạm vi ảnh hưởng khi lỗi. Pod nhỏ dễ cô lập nhưng có thể giảm khả năng chia sẻ.',
'Vì sao khả năng lắp thêm rack không đủ chứng minh có thể mở rộng trung tâm dữ liệu?',
'Pod hạ tầng dùng để làm gì?',
'Tổ chức một nhóm rack cùng các năng lực điện, làm mát và mạng|Thay thế kernel cho container|Định nghĩa một địa chỉ IP|Biểu diễn một file trên đĩa',
'Đúng: đơn vị hạ tầng.|Sai: đó không phải nhiệm vụ pod vật lý.|Sai: không phải khái niệm địa chỉ.|Sai: không phải đơn vị lưu trữ.',terms='infrastructure pod')
lesson('4.2','Điện, luồng khí và làm mát',(16,28),(38,42),'Điện tiêu thụ phần lớn chuyển thành nhiệt; nhiệt tích tụ làm giảm độ tin cậy.',
'Trung tâm dữ liệu dùng nguồn dự phòng và phân phối điện phù hợp. Máy thường hút khí lạnh phía trước, đẩy khí nóng phía sau. Hot aisle/cold aisle và containment giảm trộn khí nóng lạnh. Sàn nâng và đường dẫn khí hỗ trợ phân phối; làm mát chất lỏng là một phương án khác, không áp dụng giống nhau cho mọi thiết kế.',
'Mở thêm máy như thêm bếp vào phòng kín: phải tính cả điện vào lẫn nhiệt cần đưa ra ngoài.',
'Ví dụ tự xây dựng: 20 máy × 500 W = 10 kW tải IT giả định. Hệ thống cấp điện và tản nhiệt phải đáp ứng tải này cộng phần phụ trợ theo thiết kế; con số 10 kW không phải tổng điện cả cơ sở.',
'Khí lạnh nhiều không bảo đảm hết hot spot nếu luồng khí đi sai đường. Công suất định mức nguồn không phải số đo công suất tiêu thụ thực tế.',
'Dự phòng tăng độ sẵn sàng nhưng tốn chi phí. Làm mát hiệu quả đòi hỏi bố trí và giám sát, không chỉ tăng công suất điều hòa.',
'Tại sao đặt hai hàng máy thổi khí nóng vào cửa hút của nhau là bất lợi?',
'20 máy tiêu thụ thực tế 500 W mỗi máy. Tổng công suất IT là bao nhiêu?',
'10 kW|10 kWh bất kể thời gian|1 kW|100 kW',
'Đúng: 20×500 W = 10.000 W.|Sai: kWh là năng lượng, cần thời gian.|Sai: thiếu hệ số 10.|Sai: thừa hệ số 10.',level='Vận dụng',terms='hot aisle|cold aisle')
lesson('4.3','Lưu lượng và phân cấp mạng',(29,40),(43,46),'Nhiều máy gửi dữ liệu lên tầng cao làm đường uplink bị nghẽn.',
'North-south là lưu lượng đi vào hoặc ra trung tâm dữ liệu; east-west là giữa các thành phần bên trong. Switch top-of-rack (ToR) nối các máy trong rack lên mạng tầng trên. Khi nhiều đường xuống cùng chia uplink nhỏ hơn tổng năng lực, xuất hiện oversubscription. Link aggregation ghép nhiều liên kết để tăng năng lực tổng và dự phòng; một luồng thường vẫn bị giới hạn bởi cách phân phối lên các liên kết thành viên.',
'Đường nhỏ trong khu phố đổ vào một cổng hẹp: có nhiều cổng nhà không làm cổng khu phố rộng hơn.',
'Ví dụ tự xây dựng: 20 máy có cổng 10 Gb/s chia uplink 40 Gb/s. Tỷ lệ danh nghĩa 200:40 = 5:1. Đây là tỷ lệ năng lực cổng, không khẳng định tất cả máy luôn gửi 10 Gb/s.',
'East-west không nhất thiết nằm trong cùng rack. Ghép 4 đường 10 Gb/s không tự làm một luồng thành 40 Gb/s.',
'Giảm oversubscription tăng chi phí cổng và dây; thiết kế cần dựa trên mẫu lưu lượng.',
'Vì sao microservices có thể tạo nhiều east-west traffic hơn một ứng dụng đơn khối?',
'20 cổng xuống 10 Gb/s chia uplink tổng 40 Gb/s có tỷ lệ oversubscription danh nghĩa nào?',
'5:1|1:5|20:1|40:10',
'Đúng: tổng cổng xuống 200 chia 40.|Sai: đảo tỷ lệ.|Sai: bỏ tốc độ cổng.|Sai: chưa cộng các cổng xuống.',level='Vận dụng',terms='east-west|north-south|ToR|link aggregation')
lesson('4.4','Leaf-spine, super-spine và kết nối ngoài',(41,51),(47,50),'Ứng dụng phân tán cần băng thông cao giữa nhiều rack và tiếp tục hoạt động khi một đường hỏng.',
'Trong leaf-spine, mỗi leaf nối tới các spine để tạo nhiều đường giữa các leaf. Hai máy ở leaf khác nhau có thể qua một spine. Giới hạn cổng thúc đẩy thêm tầng super-spine khi mở rộng. Đường dự phòng phải thực sự độc lập ở những thành phần cần bảo vệ; kết nối Internet có thể dùng nhiều router và nhà cung cấp.',
'Có nhiều tuyến ngang mức giữa các khu vực giúp tránh dồn mọi xe vào một đường trục duy nhất.',
'Ví dụ tự xây dựng: leaf L1 và L2 cùng nối S1, S2. Nếu S1 hỏng, đường L1–S2–L2 còn tồn tại, với điều kiện các liên kết đó hoạt động và cơ chế chuyển tiếp sử dụng được.',
'Nhiều đường không có nghĩa mọi gói tự động dùng mọi đường hoặc không bao giờ mất gói khi hội tụ. Dự phòng chung nguồn vẫn có lỗi chung.',
'Thêm spine tăng số cổng, dây và chi phí; phải xem năng lực còn lại trong trạng thái mất một thành phần.',
'Hãy kiểm tra mạng có còn đủ năng lực sau khi mất một spine, thay vì chỉ kiểm tra có còn đường.',
'Hai leaf cùng nối hai spine. Một spine hỏng. Điều gì có thể giữ liên lạc giữa hai leaf?',
'Sử dụng đường qua spine còn hoạt động|Chỉ tăng RAM các máy chủ|Tắt spine còn lại|Đổi tên các leaf',
'Đúng: còn tuyến dự phòng nếu liên kết và điều khiển chuyển tiếp hoạt động.|Không tạo đường mạng.|Sẽ loại bỏ đường còn lại.|Không thay đổi topology.',level='Vận dụng',terms='leaf-spine')
lesson('4.5','Tách lưu trữ khỏi máy tính',(52,54),(50,51),'Nếu dữ liệu gắn chặt vào đĩa một máy, đổi máy chạy ứng dụng có thể làm mất đường truy cập dữ liệu.',
'Lưu trữ trong trung tâm dữ liệu có thể được ảo hóa và truy cập qua mạng. Tài nguyên tính toán nhìn thấy volume hoặc giao diện dịch vụ thay vì một đĩa vật lý cố định. Lớp ánh xạ bên dưới quyết định dữ liệu thực sự nằm ở đâu; mạng là phần của đường I/O.',
'Thay bàn làm việc mà vẫn mở được hồ sơ ở kho dùng chung, miễn còn đường đến kho và có quyền truy cập.',
'Ví dụ tự xây dựng: VM chuyển máy nhưng volume remote vẫn được truy cập qua mạng. Nếu volume là file cục bộ chỉ trên máy cũ, cần thêm cơ chế di chuyển hoặc chia sẻ.',
'Lưu trữ remote không đồng nghĩa dữ liệu đã được sao lưu hoặc nhân bản. Volume ảo và disk vật lý không có quan hệ một-một bắt buộc.',
'Tăng tính linh hoạt nhưng phụ thuộc độ trễ, băng thông và khả năng chịu lỗi của đường lưu trữ.',
'Vì sao mạng lưu trữ mất kết nối có thể khiến CPU ứng dụng rảnh nhưng yêu cầu vẫn chậm?',
'Lợi ích trực tiếp của tách compute khỏi remote storage là gì?',
'Có thể đổi nơi chạy compute mà vẫn truy cập cùng dữ liệu nếu hệ thống hỗ trợ|Không cần mạng nữa|Không cần sao lưu nữa|Mọi thao tác đĩa có độ trễ bằng không',
'Đúng: giảm gắn chặt dữ liệu với máy chạy.|Sai: remote storage dùng mạng.|Sai: vẫn cần backup.|Sai: I/O vẫn có chi phí.',terms='remote storage')

chapter('c05','Máy ảo và hypervisor','05-virtual-machines(1).pdf',(55,68),'Làm sao nhiều kernel cùng dùng phần cứng an toàn?|VM được di chuyển như thế nào?', 'So sánh emulation, paravirtualization và full virtualization|Theo vết dịch địa chỉ và I/O ảo|Giải thích ba pha live migration',['2.2'], 'VM là nền IaaS; so sánh với container ở chương 6.')
lesson('5.1','Emulation và bộ thông dịch bytecode',(1,7),(55,57),'Phần mềm cho một kiến trúc có thể cần chạy trên kiến trúc khác.',
'Giả lập (emulation) tái hiện hoạt động máy hoặc tập lệnh bằng phần mềm. Mỗi lệnh khách có thể cần nhiều lệnh trên host. Bộ thông dịch bytecode thực thi mã trung gian của môi trường ngôn ngữ; không phải VM ngôn ngữ nào cũng là máy ảo hệ thống chạy guest OS. Slide minh họa trường hợp thông dịch; hiệu năng thực tế còn tùy kỹ thuật tối ưu.',
'Một người dịch từng chỉ dẫn sang ngôn ngữ khác làm được việc nhưng có thêm bước trung gian.',
'Ví dụ tự xây dựng: một thao tác khách cần 30 lệnh host. Chỉ so 100 MHz khách với 2 GHz host chưa đủ chứng minh nhanh hơn; phải xét số lệnh và hành vi lệnh.',
'JVM và VM thuê từ IaaS là hai cách dùng chữ virtual machine khác nhau. Đừng suy từ ví dụ thông dịch rằng mọi full virtualization đều dịch từng lệnh.',
'Emulation linh hoạt về kiến trúc nhưng có thể tốn chi phí lớn; phù hợp khi tương thích quan trọng hơn tốc độ.',
'Điều gì phải đo ngoài tần số hai CPU khi đánh giá giả lập?',
'Điểm phân biệt emulation với full virtualization cùng kiến trúc trong bài là gì?',
'Emulation có thể tái hiện tập lệnh bằng nhiều lệnh host|Emulation luôn chạy native mọi lệnh không trung gian|Full virtualization không có guest OS|JVM luôn là hypervisor IaaS',
'Đúng: đây là nguồn overhead tiềm năng.|Sai: trái cơ chế mô tả.|Sai: có guest OS.|Sai: hai nghĩa VM khác nhau.',terms='emulation|bytecode')
lesson('5.2','Đặc quyền, CPU và bộ nhớ',(8,21),(58,61),'Guest OS cũng muốn điều khiển phần cứng; nếu để nó toàn quyền thật, các VM khác có thể bị xâm phạm.',
'CPU có mức đặc quyền để hạn chế thao tác nhạy cảm. Hệ điều hành quản lý tiến trình, thời gian CPU và không gian địa chỉ. Memory Management Unit (MMU) dịch địa chỉ và thực thi bảo vệ. Trong hệ thống VM, hypervisor phải giữ quyền kiểm soát cuối cùng; guest không được tự ý đọc RAM hoặc sửa thiết bị của tenant khác.',
'Người quản lý từng phòng không được tự mở khóa toàn bộ tòa nhà; phải có cấp kiểm soát bên ngoài.',
'Ví dụ tự xây dựng: guest nghĩ địa chỉ vật lý 0x1000 thuộc mình. Hypervisor có thể ánh xạ nó đến vùng khác trên host; guest không được chọn tùy ý RAM vật lý của VM bên cạnh.',
'Địa chỉ ảo tiến trình, địa chỉ vật lý theo guest và địa chỉ vật lý máy là các lớp khác nhau. Không gộp chúng thành một.',
'Cách ly phụ thuộc phần cứng, hypervisor và cấu hình. Tài nguyên chia sẻ vẫn có thể gây tranh chấp hiệu năng.',
'Vì sao chỉ dùng cơ chế user/kernel trong guest chưa đủ bảo vệ các VM khỏi nhau?',
'Thành phần nào cần giữ quyền kiểm soát tài nguyên phần cứng cuối cùng giữa các VM?',
'Hypervisor cùng cơ chế hỗ trợ phần cứng|Một ứng dụng bất kỳ trong guest|Mọi guest kernel cùng có toàn quyền host|Trình duyệt của người thuê',
'Đúng: guest không thể tự cấp quyền vượt lớp cách ly.|Sai: ứng dụng không có vai trò đó.|Sai: phá vỡ cách ly.|Sai: không quản lý phần cứng host.',terms='MMU|privilege level')
lesson('5.3','Paravirtualization và full virtualization',(22,39),(55,60),'Làm sao chạy hiệu quả mà vẫn kiểm soát thao tác đặc quyền?',
'Ảo hóa bán phần (paravirtualization) sửa guest để yêu cầu hypervisor thực hiện thao tác nhạy cảm qua hypercall. Ảo hóa toàn phần (full virtualization) hướng đến guest không cần sửa, cách ly và hiệu quả; hỗ trợ CPU cho phép nhiều lệnh chạy trực tiếp trong chế độ guest, thao tác cần quản lý chuyển về hypervisor. Lập lịch vCPU và ánh xạ bộ nhớ vẫn do lớp ảo hóa kiểm soát.',
'Guest biết mình ở môi trường ảo có thể dùng cửa giao tiếp riêng; guest không sửa cần môi trường trông như máy mà nó vốn hỗ trợ.',
'Ví dụ tự xây dựng: truy cập bộ nhớ của tiến trình qua bảng trang guest, rồi ánh xạ cấp hai đến RAM host. Việc guest đổi ánh xạ của mình không được cho phép vượt ra RAM đã cấp.',
'Full virtualization không đồng nghĩa hiệu năng luôn chính xác 100% native. Một VM có thể dùng driver I/O paravirtualized mà vẫn chạy OS không sửa kernel theo mô hình full virtualization.',
'Sửa guest làm giảm tính tương thích; hỗ trợ phần cứng và thiết bị ảo vẫn có chi phí, nhất là I/O.',
'Vì sao tên “full” không có nghĩa VM được toàn quyền đối với host?',
'Cách nào trực tiếp mô tả paravirtualization trong slide?',
'Sửa guest để gọi hypervisor cho thao tác đặc quyền|Dịch mọi lệnh từ kiến trúc khác|Cho guest kernel ghi mọi RAM host|Chạy container chung kernel mà không có VM',
'Đúng: hypercall thay thao tác nhạy cảm.|Đây là emulation.|Sai: vi phạm cách ly.|Đây là mô hình container.',terms='paravirtualization|full virtualization|hypercall')
lesson('5.4','I/O ảo và đĩa ảo',(40,52),(61,63),'Guest cần thấy thiết bị quen thuộc dù không sở hữu trực tiếp thiết bị vật lý.',
'Hypervisor cung cấp thiết bị ảo và chuyển thao tác I/O sang phần cứng hoặc backend. Mô phỏng thiết bị quen thuộc tận dụng driver sẵn có nhưng phải tái hiện chi tiết phức tạp. Giao diện mới tối ưu có thể đơn giản hơn nhưng cần driver phù hợp. Đĩa ảo có thể là file host hoặc volume remote, không nhất thiết là một đĩa vật lý.',
'Guest gửi đơn qua một quầy tiếp nhận; phía sau quầy có thể xử lý bằng nhiều loại kho khác nhau.',
'Ví dụ tự xây dựng: guest ghi block 100 của đĩa ảo. Hypervisor ánh xạ sang vị trí trong file host; hệ thống file host lại ánh xạ file sang block đĩa thật. Đừng nhầm hai lớp ánh xạ.',
'Có driver trong guest không có nghĩa guest đang điều khiển thiết bị vật lý độc quyền. Passthrough là trường hợp thiết kế khác cần kiểm soát riêng.',
'Mô phỏng tăng tương thích nhưng thêm đường xử lý. Hiệu năng phụ thuộc kiểu backend, cache và tải chia sẻ.',
'Nêu hai nơi đĩa ảo có thể được lưu và ảnh hưởng đến migration.',
'Guest nhìn thấy một ổ đĩa ảo. Điều gì chưa thể kết luận?',
'Ổ đó tương ứng độc quyền với đúng một đĩa vật lý|Guest sử dụng giao diện block|Hypervisor có thể ánh xạ I/O|Backend có thể là một file',
'Đúng: ánh xạ không bắt buộc một-một.|Đây là giao diện thường thấy.|Đây là cơ chế hợp lý.|Đây là ví dụ slide.',terms='virtual I/O|virtual disk')
lesson('5.5','VM như đối tượng và live migration',(53,66),(63,66),'Cần chuyển máy để bảo trì hoặc cân tải nhưng muốn giữ dịch vụ hoạt động.',
'Trạng thái VM gồm CPU, RAM, thiết bị ảo và thông tin lưu trữ cần thiết. Stop-copy-restart dừng VM, chuyển trạng thái rồi chạy lại. Live migration kiểu pre-copy thường chuyển RAM khi VM còn chạy, lặp gửi các trang bị ghi bẩn, rồi dừng ngắn để chuyển phần còn lại và trạng thái CPU trước khi khôi phục ở đích. Lưu trữ và mạng cần được xử lý phù hợp.',
'Chuyển nhà trong khi còn làm việc: chở phần ít thay đổi trước, chốt phần đang dùng cuối cùng. Có một lúc phải bàn giao quyền hoạt động.',
'Ví dụ tự xây dựng: RAM 8 GiB, tốc độ truyền hiệu dụng 1 GiB/s, ứng dụng ghi bẩn 0,1 GiB/s. Pha đầu cần tối thiểu khoảng 8 giây theo giả định; pha lặp xử lý phần đổi. Nếu tốc độ ghi bẩn lớn hơn tốc độ chuyển, pre-copy khó hội tụ nếu không có biện pháp giới hạn.',
'“Live” không có nghĩa downtime bằng 0. Migration tránh một máy sắp bảo trì; khi máy đã hỏng đột ngột và RAM mất thì không thể chép trạng thái RAM đó.',
'Tốn mạng, có thể kéo dài dưới tải ghi cao; cần tương thích CPU và duy trì khả năng truy cập dữ liệu.',
'Vì sao chỉ sao chép RAM một lần khi VM đang chạy có thể tạo trạng thái không nhất quán?',
'Điều gì làm pre-copy migration khó hội tụ?',
'Tốc độ làm bẩn RAM lớn hơn tốc độ truyền trạng thái|VM gần như không ghi bộ nhớ|Đường truyền nhanh hơn nhiều tốc độ thay đổi RAM|Ứng dụng đang nhàn rỗi',
'Đúng: phần đổi mới sinh nhanh hơn khả năng chuyển.|Trường hợp này thường thuận lợi.|Điều này giúp hội tụ.|Thường ít thay đổi nên thuận lợi.',level='Vận dụng',terms='live migration|dirty page')
lesson('5.6','Hypervisor trực tiếp và hosted',(67,70),(66,68),'Người học cần chạy VM trên laptop trong khi trung tâm dữ liệu tối ưu cho vận hành quy mô lớn.',
'Hypervisor loại 1 vận hành trực tiếp trên lớp phần cứng theo mô hình phân loại khái niệm. Hypervisor hosted, thường gọi loại 2, dựa vào host OS để cung cấp một số chức năng và giao diện. Một số hệ thống thực tế kết hợp các thành phần khiến cách phân loại không tuyệt đối; mục đích là hiểu đường điều khiển và vai trò host.',
'Một mô hình thiết kế tòa nhà chuyên dụng cho nhiều phòng thuê; mô hình khác bố trí phòng thuê trong cơ sở đã có hệ điều hành chủ.',
'Ví dụ tự xây dựng: dùng phần mềm VM trên Windows để tạo một máy Linux thực hành. Bạn vẫn cần RAM cho Windows host; không thể cấp toàn bộ RAM laptop cho guest rồi bỏ qua host.',
'Guest Linux trên Windows không có nghĩa ứng dụng Linux trở thành tiến trình Windows thuần. Host và guest là hai OS khác nhau.',
'Hosted thuận tiện học tập nhưng cần chia tài nguyên với tác vụ desktop. Loại hypervisor không tự quyết định toàn bộ hiệu năng hay độ an toàn.',
'Vẽ lớp host OS, hypervisor, guest OS và ứng dụng trong mô hình hosted.',
'Khi cấp RAM cho VM hosted trên laptop, phải chừa RAM cho ai?',
'Host OS và các tiến trình của host|Không ai vì VM thay thế toàn bộ host|Chỉ màn hình|Chỉ firmware mạng',
'Đúng: host vẫn hoạt động và dùng RAM.|Sai: hosted không xóa host.|Sai: không đủ.|Sai: bỏ qua OS và ứng dụng.',terms='hosted hypervisor')

chapter('c06','Container và Docker','06-containers(1).pdf',(71,83),'Vì sao container khởi động nhanh?|Cách ly tiến trình khác máy ảo ở đâu?|Từ Dockerfile đến container chạy ra sao?', 'Theo vết build–image–run|Phân biệt namespace với giới hạn tài nguyên|Chọn VM hay container cho một tình huống',['5.3','5.4'], 'Chuẩn bị cho orchestration và các nền tảng FaaS.')
lesson('6.1','Chi phí VM và quản lý tiến trình',(1,14),(71,74),'Tạo nhiều bản sao ứng dụng nhỏ bằng cách boot nhiều OS làm tăng thời gian và bộ nhớ nền.',
'Mỗi VM có kernel, tiến trình nền và lập lịch riêng. Chi phí đó có thể chấp nhận khi chạy lâu hoặc cần OS riêng, nhưng gây bất lợi với tác vụ ngắn và co giãn nhanh. OS vốn quản lý CPU, bộ nhớ và nhiều tài nguyên dùng chung giữa tiến trình; container mở rộng khả năng tạo các góc nhìn được cách ly.',
'Nếu chỉ cần một bàn làm việc trong thời gian ngắn, dựng cả một văn phòng độc lập cho mỗi người có thể quá tốn.',
'Ví dụ tự xây dựng: 100 tác vụ dài 2 giây nhưng mỗi VM cần 30 giây boot. Nếu mỗi tác vụ boot một VM mới, thời gian chờ và chi phí nền chiếm ưu thế. Pool VM hoặc container có thể cải thiện, nhưng phải đo cả thời gian tải image.',
'Khởi động nhanh không có nghĩa tác vụ tính toán bên trong tự chạy nhanh hơn. Chi phí boot khác chi phí xử lý một yêu cầu.',
'VM vẫn phù hợp khi cần kernel hoặc OS khác; container ưu tiên nhẹ và triển khai nhanh.',
'Phân biệt latency khởi động với throughput xử lý ổn định.',
'Lợi ích nổi bật của container cho tác vụ ngắn so với mỗi tác vụ boot một VM là gì?',
'Giảm chi phí tạo môi trường vì dùng kernel host|Tự động tăng tốc mọi thuật toán|Không cần bộ nhớ|Không còn cần cách ly',
'Đúng: tránh boot guest OS riêng.|Sai: thuật toán không tự đổi.|Sai: vẫn dùng RAM.|Sai: cách ly vẫn cần.',terms='container')
lesson('6.2','Namespace, cách ly và chia sẻ có kiểm soát',(15,23),(74,76),'Các ứng dụng chung kernel cần thấy không gian tiến trình, mạng và file phù hợp thay vì tự do nhìn tài nguyên nhau.',
'Namespace cung cấp góc nhìn cách ly cho các nhóm tài nguyên như PID, mạng, mount và user. Cgroup kiểm soát hoặc hạch toán mức sử dụng tài nguyên; đây là phần diễn giải bổ sung để phân biệt giới hạn với góc nhìn. Container vẫn chia sẻ kernel host và có thể chia sẻ volume hoặc mạng theo cấu hình. Câu “không chia sẻ bất kỳ tài nguyên nào” trên slide 17–19 cần hiểu là minh họa các không gian riêng, không phải khẳng định có kernel và phần cứng riêng.',
'Mỗi phòng có bảng tên và tủ hồ sơ riêng nhưng vẫn chung nền móng; quản trị viên tòa nhà có khả năng quan sát và can thiệp.',
'Ví dụ tự xây dựng: hai container đều thấy tiến trình PID 1, nhưng đó là hai góc nhìn PID namespace. Mount cùng volume vào cả hai lại cho phép chia sẻ dữ liệu một cách chủ đích.',
'Namespace không tự bảo đảm giới hạn CPU/RAM. File base image Linux không chứa một kernel Linux riêng cho mỗi container.',
'Chung kernel làm giảm chi phí nhưng có ranh giới cách ly khác VM. Đặc quyền và volume host cấu hình sai có thể phá mục tiêu cách ly.',
'Vì sao container Linux không thể dùng một tính năng kernel chỉ có ở Windows nếu không có lớp OS/VM phù hợp?',
'Phát biểu chính xác về container là gì?',
'Chia sẻ kernel host nhưng có thể có namespace riêng|Mỗi container bắt buộc boot kernel riêng|Namespace tự giới hạn RAM ở mọi cấu hình|Có image Debian nghĩa host kernel trở thành Debian riêng trong container',
'Đúng: phân biệt kernel chung với góc nhìn riêng.|Sai: đó gần mô hình VM.|Sai: giới hạn tài nguyên là cơ chế khác.|Sai: user space image không thay kernel host.',terms='namespace|cgroup|kernel')
lesson('6.3','Dockerfile, image và registry',(24,34),(76,83),'Cần tái tạo môi trường ứng dụng thay vì cài thủ công khác nhau trên từng máy.',
'Dockerfile là công thức build. Image là kết quả đóng gói các lớp file và metadata; container là một phiên chạy tạo từ image. Registry lưu và phân phối image. Các bước như chọn base, cài thư viện và chép mã ảnh hưởng khả năng tái lập. Image chứa user space và phụ thuộc cần thiết, không mặc định chứa kernel riêng.',
'Công thức là Dockerfile, bánh đã làm theo công thức là image, một lần mang bánh ra phục vụ tương ứng một phiên chạy; ví von chỉ phân biệt các giai đoạn, không mô tả lớp ghi của container.',
'Ví dụ tự xây dựng:\nFROM python:3-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD ["python", "app.py"]\nĐây là mã minh họa cách đọc, không khẳng định tag hoặc phụ thuộc đã cố định để tái lập tuyệt đối. Máy offline phải có image và phụ thuộc từ trước.',
'Build không đồng nghĩa run. Xóa container có thể làm mất dữ liệu ở lớp ghi nếu chưa đưa ra volume. Tag thay đổi không giống digest cố định.',
'Image nhỏ giảm tải nhưng quá tối giản có thể khó chẩn đoán. Không ghi bí mật lâu dài vào image.',
'Thay mã app.py cần build lại image trong quy trình này hay chỉ restart container cũ?',
'Đâu là quan hệ đúng?',
'Dockerfile tạo image khi build; image được dùng để tạo container khi run|Container luôn tạo Dockerfile khi tắt|Registry là kernel host|Image đang lưu tự phục vụ HTTP dù chưa chạy',
'Đúng: phân biệt ba đối tượng và hai giai đoạn.|Sai: không có quan hệ bắt buộc đó.|Sai: registry phân phối image.|Sai: cần tiến trình chạy.',terms='Dockerfile|image|registry')
lesson('6.4','Runtime, chuẩn hóa và LXC',(35,37),(77,80),'Cần lớp thực thi biến mô tả container thành tiến trình với cấu hình cách ly cụ thể.',
'Container runtime tạo và quản lý môi trường tiến trình, namespace, mạng và volume theo yêu cầu công cụ quản lý. Docker là bộ công cụ; containerd là một thành phần runtime được nêu trong slide. LXC cũng dựa trên cơ chế cách ly OS nhưng thường phục vụ môi trường hệ thống với nhiều ứng dụng theo cách tiếp cận trong tài liệu.',
'Bản thiết kế không tự dựng phòng: runtime là lớp thực hiện việc thiết lập rồi cho ứng dụng hoạt động.',
'Ví dụ tự xây dựng: yêu cầu chạy image với một volume. Runtime phải tạo môi trường, gắn volume, thiết lập mạng rồi bắt đầu tiến trình. Nếu volume thiếu quyền, lỗi có thể xuất hiện trước khi logic ứng dụng chạy.',
'Kubernetes không đồng nghĩa Docker CLI; orchestration quản lý vòng đời nhiều đơn vị, còn runtime thực thi container. Container không buộc chỉ có đúng một tiến trình dù thiết kế một ứng dụng là khuyến nghị phổ biến.',
'Chuẩn hóa giúp thay công cụ nhưng không loại bỏ khác biệt mạng, volume và tính năng OS.',
'Liệt kê phần thuộc image và phần chỉ được quyết định khi run.',
'Thành phần nào trực tiếp thiết lập môi trường để tiến trình container chạy?',
'Container runtime|Chỉ registry|Chỉ file README|Chỉ trình biên dịch của ứng dụng',
'Đúng: thực thi cấu hình chạy.|Registry chỉ phân phối image.|Tài liệu không thực thi.|Biên dịch không tạo đầy đủ môi trường runtime.',terms='container runtime|LXC')

chapter('c07','Mạng ảo, overlay và NAT','07-virtual-networks(1).pdf',(87,96),'Làm sao vừa kết nối linh hoạt vừa cách ly tenant?|Gói tin đi qua VLAN, VXLAN và NAT thế nào?', 'Theo vết địa chỉ trong gói encapsulation và NAT|Phân biệt underlay, overlay, VLAN, VXLAN|Giải thích quản lý mạng khi VM di chuyển',['4.3','5.4'], 'Nối kiến thức mạng vật lý với mạng của VM, bảo mật và điều phối.')
lesson('7.1','Mục tiêu và các lớp mạng',(1,24),(87,89),'VM cần được đặt linh hoạt ở nhiều rack nhưng chỉ được giao tiếp theo chính sách tenant.',
'Mạng nền (underlay) cung cấp kết nối giữa thiết bị vật lý. Mạng phủ (overlay) xây kết nối logic trên mạng nền bằng cơ chế như đóng gói. Mạng ảo là góc nhìn kết nối dành cho workload/tenant; không nhất thiết phản ánh vị trí dây thật. Cách ly phải được thực thi bằng cấu hình và cơ chế chuyển tiếp, không chỉ vẽ các nhóm riêng trên sơ đồ.',
'Hai công ty dùng chung đường vận chuyển nhưng có các hệ thống phân loại kiện hàng riêng. Đường thật vẫn phải nối được các kho.',
'Ví dụ tự xây dựng: VM1 và VM2 cùng tenant nằm ở hai rack. Overlay tạo kết nối logic giữa chúng; underlay phải chuyển được gói giữa hai host. Nếu underlay mất kết nối, overlay không tạo ra đường vật lý thay thế.',
'Overlay không thay thế underlay. Kết nối được không đồng nghĩa được cấp quyền truy cập ứng dụng.',
'Overlay tăng linh hoạt nhưng thêm header, trạng thái ánh xạ và chi phí chẩn đoán nhiều lớp.',
'Nêu hai nguyên nhân khác nhau khiến hai VM cùng overlay không liên lạc được.',
'Underlay bị đứt mọi đường giữa hai host. Overlay có tự duy trì truyền dữ liệu giữa hai host không?',
'Không; overlay vẫn cần đường truyền nền|Có vì overlay không dùng phần cứng|Có vì VM cùng subnet luôn dùng chung RAM|Có nếu đổi tên VXLAN',
'Đúng: lớp logic dựa vào kết nối thật.|Sai: vẫn truyền gói thật.|Sai: không có bộ nhớ chung như vậy.|Sai: tên không tạo đường truyền.',terms='underlay|overlay|virtual network')
lesson('7.2','VLAN và switch ảo',(25,38),(89,91),'Nhiều nhóm dùng chung switch nhưng cần tách miền quảng bá.',
'Mạng LAN ảo (Virtual Local Area Network, VLAN) phân nhóm kết nối lớp 2 bằng cấu hình cổng và thẻ VLAN. Trường định danh 12 bit cho khoảng 4.094 VLAN dùng thông thường, không phải số tenant vô hạn. Switch ảo trong host nối vNIC của VM và uplink vật lý. Cấu hình trunk/access và ánh xạ VM đến nhóm mạng phải nhất quán.',
'Thẻ nhóm trên kiện hàng giúp switch phân loại chuyển tiếp, nhưng người quản trị phải quy định cổng nào chấp nhận thẻ nào.',
'Ví dụ tự xây dựng: VM A và B cùng VLAN 10 ở hai host. Nếu uplink thứ hai không cho VLAN 10 đi qua, cùng nhãn logic vẫn không đủ để liên lạc.',
'VLAN không mã hóa payload. Người có quyền sửa cấu hình mạng có thể thay ranh giới; không dùng VLAN thay xác thực và phân quyền ứng dụng.',
'Đơn giản trong mạng nhỏ nhưng không gian định danh và phạm vi lớp 2 hạn chế ở cloud quy mô lớn.',
'Vì sao cùng VLAN ID trên hai mạng hoàn toàn tách biệt không có nghĩa chúng tự nối vào nhau?',
'VLAN chủ yếu cung cấp điều gì?',
'Phân đoạn lớp 2 theo cấu hình và thẻ|Mã hóa bắt buộc mọi payload|Định danh 24 bit như VXLAN VNI|Xác thực người dùng ứng dụng',
'Đúng: đây là mục tiêu phân đoạn.|Sai: tagging không phải encryption.|Sai: VLAN dùng trường 12 bit.|Sai: thuộc lớp ứng dụng/danh tính.',terms='VLAN|virtual switch')
lesson('7.3','VXLAN và đóng gói gói tin',(39,55),(90,91),'Không gian VLAN và phụ thuộc mạng lớp 2 làm khó quản lý nhiều mạng tenant trên datacenter lớn.',
'Virtual eXtensible LAN (VXLAN) đóng khung Ethernet của tenant trong UDP/IP để mạng IP nền vận chuyển. VXLAN Network Identifier (VNI) dài 24 bit phân biệt mạng logic. Điểm đầu cuối tunnel (VTEP) thêm/bỏ header ngoài. Địa chỉ ngoài định tuyến đến host/VTEP; địa chỉ trong vẫn thuộc workload. Đường đi nền không cần hiểu địa chỉ nội bộ từng VM theo cùng cách.',
'Cho phong bì của tenant vào một phong bì vận chuyển có địa chỉ kho. Đến kho đích bỏ phong bì ngoài rồi giao phong bì trong.',
'Ví dụ tự xây dựng: VM A gửi đến VM B. (1) Switch/VTEP xác định VNI và host đích. (2) Thêm UDP/IP ngoài. (3) Underlay định tuyến theo IP ngoài. (4) VTEP đích bỏ header và giao khung trong. Thêm header có thể đòi hỏi điều chỉnh MTU.',
'VXLAN đóng gói, không mặc định mã hóa. VNI có nhiều giá trị hơn VLAN nhưng vẫn hữu hạn và cần quản lý.',
'Tăng quy mô và linh hoạt đổi lấy overhead header, tra cứu endpoint và khó gỡ lỗi nhiều lớp.',
'Khi bắt gói ở underlay, IP nào là địa chỉ dùng để vận chuyển giữa các VTEP?',
'Router underlay thường dùng gì để chuyển tiếp gói VXLAN giữa các host?',
'Địa chỉ IP ngoài của tunnel|Tên file trong VM|VNI thay toàn bộ bảng định tuyến IP|Mật khẩu người dùng ứng dụng',
'Đúng: header ngoài phục vụ mạng nền.|Sai: không liên quan.|Sai: VNI phân biệt mạng logic, không thay IP route ngoài.|Sai: không phải thông tin chuyển tiếp.',level='Vận dụng',terms='VXLAN|VNI|VTEP')
lesson('7.4','NAT, cổng và địa chỉ riêng',(56,76),(91,92),'Địa chỉ riêng có thể trùng giữa các tenant và không dùng trực tiếp để định tuyến toàn Internet.',
'Dịch địa chỉ mạng (Network Address Translation, NAT) thay địa chỉ và thường cả cổng tại biên. Ánh xạ trạng thái cho phép gói phản hồi quay về đúng endpoint nội bộ. Địa chỉ private chỉ có ý nghĩa trong phạm vi định tuyến tương ứng. NAT cho kết nối đi ra không tự tạo quyền cho kết nối đi vào chưa có ánh xạ hoặc quy tắc phù hợp.',
'Tổng đài đổi nhiều số máy lẻ sang một số ngoài kèm thông tin để nối cuộc gọi trở về đúng người.',
'Ví dụ tự xây dựng: 10.0.0.2:5000 → 203.0.113.10:41001, gửi đến 198.51.100.20:443. Khi phản hồi về cổng 41001, NAT tra ánh xạ rồi chuyển đến 10.0.0.2:5000. Các IP ngoài là địa chỉ minh họa.',
'NAT không đồng nghĩa firewall và không phải mã hóa. Có địa chỉ public không có nghĩa mọi dịch vụ đều được phép truy cập.',
'NAT có bảng trạng thái, giới hạn cổng và thời gian hết hạn; kết nối chủ động từ ngoài cần thiết kế rõ.',
'Vì sao hai VM cùng dùng 10.0.0.2 vẫn có thể tồn tại ở hai mạng tenant độc lập?',
'NAT dùng ánh xạ cổng khi nhiều kết nối chia một IP ngoài nhằm mục đích gì?',
'Phân biệt các luồng để chuyển gói trả về đúng endpoint|Mã hóa nội dung HTTP|Tăng số lõi CPU|Làm private IP định tuyến toàn cầu mà không cần ánh xạ',
'Đúng: trạng thái ánh xạ giữ quan hệ trong/ngoài.|Sai: không cung cấp encryption.|Sai: không liên quan.|Sai: vẫn cần ánh xạ và định tuyến.',level='Vận dụng',terms='NAT|private IP')
lesson('7.5','Di chuyển VM và điều khiển mạng',(77,82),(92,96),'Endpoint và đường đi thay đổi khi VM được tạo, xóa hoặc di chuyển.',
'Quản lý mạng cần cập nhật ánh xạ endpoint, chính sách và đường chuyển tiếp. Routing phân tán như OSPF hay BGP và điều khiển tập trung có các vai trò khác nhau. Sách bổ trợ Software Defined Networking (SDN) tách logic điều khiển khỏi chức năng chuyển tiếp; OpenFlow là một giao diện điều khiển bảng luồng trong cách tiếp cận cụ thể, không phải tên khác của mọi SDN.',
'Danh bạ giao hàng phải cập nhật khi người nhận chuyển chỗ; địa chỉ logic ổn định không có nghĩa đường đến vị trí vật lý không đổi.',
'Ví dụ tự xây dựng: VM chuyển host H1 sang H2 nhưng giữ IP logic. VTEP hoặc hệ thống điều khiển phải cập nhật đích tunnel; ánh xạ cũ khiến gói đến H1.',
'SDN không có nghĩa chỉ một máy điều khiển duy nhất không dự phòng. OpenFlow không thay thế mọi giao thức định tuyến và chính sách.',
'Tự động hóa giảm thao tác nhưng cấu hình sai có thể lan rộng; cần kiểm chứng và rollback.',
'Nếu migration thành công ở CPU/RAM mà gói vẫn tới host cũ, còn lớp nào chưa được cập nhật?',
'VM giữ IP nhưng chuyển host. Việc nào cần được hệ thống mạng hỗ trợ?',
'Cập nhật thông tin vị trí endpoint và chuyển tiếp thích hợp|Giữ mọi ánh xạ cũ mãi mãi|Xóa mọi kiểm soát truy cập|Coi IP logic là dây nối vật lý cố định',
'Đúng: giữ tên logic cần đổi đường tới vị trí thật.|Sai: dẫn tới gửi sai host.|Sai: không cần và nguy hiểm.|Sai: mạng ảo tách hai khái niệm.',terms='SDN|OpenFlow')

chapter('c08','Lưu trữ ảo: block, file và object','08-virtual-storage(1).pdf',(99,108),'Ứng dụng thực sự đọc ghi qua giao diện nào?|NAS, SAN và object khác nhau ở đâu?', 'Theo vết file đến block|Chọn giao diện lưu trữ theo yêu cầu|Phân biệt nhân bản với sao lưu',['4.5','5.4'], 'Dữ liệu tồn tại độc lập với vòng đời compute là nền cho ứng dụng co giãn.')
lesson('8.1','Giao diện block và file',(1,8),(99,101),'Thiết bị lưu trữ không tự hiểu tên file và thư mục như ứng dụng.',
'Giao diện block đọc/ghi các khối có kích thước cố định theo số thứ tự. Hệ thống file ánh xạ tên file và offset sang block, quản lý metadata và không gian trống. Đổi một byte trên giao diện block có thể cần đọc–sửa–ghi cả block theo mô hình đơn giản của slide; các lớp cache và thiết bị thực tế có thể tối ưu khác nhau.',
'Kho có các ô được đánh số; hệ thống file giữ mục lục cho biết hồ sơ nào nằm trong các ô nào.',
'Ví dụ tự xây dựng: file 10 KiB với block 4 KiB cần ít nhất 3 block dữ liệu trong mô hình không nén, chưa tính metadata. Block cuối có phần chưa dùng.',
'File không phải block. KiB = 1.024 byte còn kB = 1.000 byte; bảng slide bổ sung ghi hai cách tính dưới cùng tên nên ứng dụng dùng ký hiệu tách bạch.',
'Block linh hoạt cho hệ thống file/DB nhưng ứng dụng phải dùng lớp tổ chức dữ liệu; file thuận tiện nhưng có semantics và metadata riêng.',
'Tại sao một file nhỏ vẫn có thể chiếm một block đầy theo cách cấp phát đơn giản?',
'File 10 KiB, block 4 KiB, không nén. Số block dữ liệu tối thiểu là bao nhiêu?',
'3|2|2,5 block được cấp phát|10',
'Đúng: làm tròn lên 10/4.|Sai: không đủ dung lượng.|Sai: cấp phát theo nguyên block.|Sai: nhầm KiB với số block.',level='Vận dụng',terms='block storage|file system|KiB')
lesson('8.2','Local, remote và ánh xạ đĩa ảo',(9,22),(101,106),'Đĩa gắn cùng host ràng buộc dữ liệu với nơi chạy; đĩa remote thay đổi đường I/O.',
'Lưu trữ cục bộ truy cập thiết bị ở máy; lưu trữ từ xa truyền yêu cầu qua mạng. Remote có thể cung cấp giao diện file hoặc block. Volume ảo ánh xạ không gian địa chỉ logic sang các vùng vật lý, có thể phân bố trên nhiều đĩa. Hạ tầng siêu hội tụ (Hyper-Converged Infrastructure, HCI) trong sách gộp tài nguyên tính toán và lưu trữ theo cụm quản lý chung.',
'Bạn thấy một ngăn hồ sơ ổn định trong khi hệ thống bên dưới có thể đổi kho lưu thực tế.',
'Ví dụ tự xây dựng: ứng dụng chậm khi đợi I/O remote dù CPU thấp. Kiểm tra độ trễ mạng, hàng đợi dịch vụ lưu trữ và giới hạn volume trước khi thêm CPU.',
'Remote block không phải remote file: ở block, phía sử dụng thường quản lý hệ thống file; ở file, máy chủ file quản lý lớp đó.',
'Tách dữ liệu tăng tính linh hoạt nhưng thêm phụ thuộc mạng. Nhân bản có thể tăng chịu lỗi nhưng không bảo vệ khỏi xóa nhầm được nhân bản ngay.',
'Vì sao bản sao đồng bộ không thay thế lịch sử backup?',
'Với remote block storage, lớp nào thường tổ chức tên file trên volume?',
'Hệ thống file ở phía sử dụng volume|VNI của VXLAN|Bộ cân bằng tải HTTP|Tên rack của máy lưu trữ',
'Đúng: block chỉ cung cấp các khối.|Sai: thuộc mạng ảo.|Sai: không tổ chức file trên volume.|Sai: không có vai trò đó.',terms='HCI|remote storage')
lesson('8.3','NAS và SAN',(23,30),(103,107),'Tổ chức cần chọn cách chia sẻ dữ liệu qua mạng phù hợp với ứng dụng.',
'Network Attached Storage (NAS) cung cấp truy cập file qua mạng như NFS/SMB. Storage Area Network (SAN) thường cung cấp truy cập block qua một mạng lưu trữ, ví dụ Fibre Channel hoặc iSCSI. Trong mô hình so sánh, client NAS dùng dịch vụ file còn client SAN nhìn thấy block và tự tổ chức hệ thống file. Không suy rằng SAN luôn dùng một công nghệ dây duy nhất.',
'NAS đưa bạn hồ sơ theo tên; SAN đưa bạn các ô kho để tự tổ chức hồ sơ.',
'Ví dụ tự xây dựng: nhóm muốn nhiều máy cùng mở thư mục chia sẻ bằng tên file: NAS phù hợp trực tiếp hơn. DB cần volume block có thể dùng SAN hoặc dịch vụ block khác. Nếu nhiều host cùng ghi block một volume, cần cơ chế phối hợp phù hợp, không tùy tiện mount ghi đồng thời.',
'NAS không có nghĩa chỉ dành cho gia đình; SAN không bảo đảm nhanh hơn trong mọi tải. Chọn theo giao diện và semantics trước quảng cáo tốc độ.',
'NAS thuận tiện chia sẻ file; SAN linh hoạt cho block nhưng quản lý phức tạp hơn và cần kiểm soát đồng thời.',
'Vì sao cho hai máy cùng ghi một volume block không có hệ thống file cluster có thể hỏng dữ liệu?',
'Ứng dụng cần dịch vụ truy cập file theo tên từ nhiều máy. Giao diện nào phù hợp trực tiếp?',
'NAS|Một block device không có lớp file|NAT|Một hypercall CPU',
'Đúng: NAS cung cấp file semantics.|Chưa có lớp tên file/chia sẻ cần thiết.|Sai: dịch địa chỉ mạng.|Sai: không cung cấp dịch vụ file.',terms='NAS|SAN')
lesson('8.4','Object storage và lựa chọn giao diện',(31,35),(107,108),'Dữ liệu như ảnh và bản sao lưu thường cần truy cập từng đối tượng qua API thay vì thao tác đĩa.',
'Lưu trữ đối tượng (object storage) quản lý nội dung theo khóa/định danh và metadata, thường qua API get/put. Nó không mặc định có đầy đủ ngữ nghĩa cập nhật ngẫu nhiên theo byte, khóa file hoặc rename của hệ thống file. Slide liệt kê EFS, EBS, S3 như ví dụ các giao diện tại thời điểm tài liệu; bài học tập trung vào loại giao diện.',
'Gửi một kiện hàng có nhãn rồi lấy lại theo nhãn; không phải mở trực tiếp một sector của đĩa.',
'Ví dụ tự xây dựng: website ảnh lưu mỗi ảnh thành một object với khóa do ứng dụng tạo. Metadata trong DB trỏ tới khóa. Nếu đổi ảnh, phải xác định chính sách ghi đè, version hoặc tạo khóa mới theo dịch vụ.',
'Object không phải file POSIX chỉ vì có ký tự “/” trong khóa. Object storage cũng không tự là nơi chạy DB cần giao diện block.',
'Phù hợp đối tượng lớn và phân phối nhưng cần hiểu nhất quán, version, phí thao tác và vòng đời theo dịch vụ cụ thể.',
'Ứng dụng yêu cầu cập nhật ngẫu nhiên 4 KiB giữa file thường xuyên. Vì sao không thể thay object API vào mà không đổi thiết kế?',
'Khóa object có dấu “/”. Điều gì không thể tự suy ra?',
'Dịch vụ hỗ trợ đầy đủ semantics thư mục và file POSIX|Object có định danh để lấy lại|Ứng dụng có thể tự đặt quy ước khóa|Metadata có thể được dùng nếu dịch vụ hỗ trợ',
'Đúng: cấu trúc ký tự không bảo đảm file semantics.|Đây là đặc điểm cơ bản.|Đây là khả năng thiết kế ứng dụng.|Đây là phát biểu có điều kiện hợp lý.',terms='object storage')

chapter('c09','Tự động hóa và hạ tầng dưới dạng mã','09-automation(1).pdf',(113,123),'Tại sao quy mô cloud cần automation?|Mô tả kết quả khác mô tả thao tác thế nào?', 'Liệt kê phụ thuộc của quy trình tạo VM|Phân biệt declarative, imperative và intent|Phân tích push/pull cùng rủi ro tự động hóa',['2.2','7.5'], 'Automation thực hiện tác vụ; orchestration phối hợp vòng đời nhiều tác vụ.')
lesson('9.1','Bối cảnh và nhu cầu tự động hóa',(1,19),(113,115),'Tài nguyên ảo thay đổi nhanh khiến quản trị thủ công dễ sai và không theo kịp.',
'Người dùng cuối thấy automation qua SaaS; doanh nghiệp tự động triển khai và cấu hình; nhà cung cấp vận hành các lớp hạ tầng quy mô lớn. Automation thực hiện các thao tác lặp lại bằng phần mềm. Tốc độ, tính nhất quán và khả năng kiểm tra là động lực; tự động hóa sai quy trình chỉ làm sai nhanh hơn.',
'Biểu mẫu được kiểm tra và điền nhất quán tốt hơn chép tay hàng nghìn lần, nhưng quy tắc sai vẫn tạo hàng nghìn kết quả sai.',
'Ví dụ tự xây dựng: cùng một mẫu cấu hình được áp dụng cho 1.000 VM. Phải kiểm tra ở tập nhỏ trước và lưu phiên bản để quay lại khi lỗi.',
'Automation không đồng nghĩa AI. Một script theo quy tắc rõ ràng cũng là tự động hóa.',
'Chi phí xây dựng và bảo trì quy trình cần được tính; mở rộng quyền của công cụ có thể tăng phạm vi ảnh hưởng khi lỗi.',
'Nêu một lỗi cấu hình mà tự động hóa có thể khuếch đại và cách giới hạn phạm vi.',
'Lý do nào chính đáng nhất để tự động hóa quản lý nhiều VM?',
'Tăng khả năng lặp lại và giảm sai lệch thao tác ở quy mô lớn|Loại bỏ nhu cầu kiểm tra cấu hình|Đảm bảo mọi script luôn đúng|Chỉ để được gọi là AI',
'Đúng: quy mô và nhất quán là động lực.|Sai: vẫn phải kiểm tra.|Sai: script có thể sai.|Sai: automation không buộc dùng AI.',terms='automation')
lesson('9.2','Tạo VM là một quy trình có phụ thuộc',(20,31),(115,116),'Bấm “tạo VM” che giấu nhiều bước liên quan compute, đĩa, mạng và định danh.',
'Quy trình cần chọn host, cấp bộ nhớ/CPU, tạo hoặc gắn đĩa, cấu hình vNIC và mạng, thiết lập image và thông tin truy cập, khởi động rồi xác nhận sức khỏe. Một bước thất bại có thể để lại tài nguyên đã tạo ở các bước trước. Thực thi an toàn cần trạng thái, kiểm tra kết quả và dọn dẹp hoặc bù trừ.',
'Đặt phòng có thêm chìa khóa, điện nước và quyền vào cửa; tạo căn phòng mà chưa có đường vào chưa phải phục vụ được.',
'Ví dụ tự xây dựng: đã tạo volume nhưng tạo VM thất bại. Ghi lại ID volume để thử lại có kiểm soát hoặc xóa volume không dùng; không tạo mới vô hạn mỗi lần retry.',
'API trả “đã nhận yêu cầu” không đồng nghĩa tài nguyên đã sẵn sàng. Idempotency giúp retry không tạo tác dụng lặp ngoài ý muốn.',
'Cần timeout, theo dõi trạng thái và xử lý thất bại từng phần; khó hơn một script nối lệnh đơn giản.',
'Ở bước nào bạn kiểm tra máy thực sự phục vụ ứng dụng, thay vì chỉ đang bật?',
'Tạo volume thành công rồi tạo VM thất bại. Cách xử lý phù hợp là gì?',
'Theo dõi tài nguyên đã tạo để retry hoặc dọn dẹp có kiểm soát|Tạo thêm volume mới vô hạn|Coi toàn bộ quy trình đã thành công|Xóa mọi volume của mọi tenant',
'Đúng: xử lý thất bại từng phần.|Sai: gây rò tài nguyên.|Sai: VM chưa có.|Sai: vượt phạm vi và phá dữ liệu.',level='Vận dụng',terms='idempotency')
lesson('9.3','Phạm vi và các mức automation',(32,53),(116,119),'Tự động cấp phát chỉ là một phần; hệ thống còn phải theo dõi và duy trì trạng thái dài hạn.',
'Các tác vụ có thể tự động gồm quản lý tài nguyên, đo đếm, tối ưu vị trí, sao lưu/khôi phục, cập nhật và thực thi chính sách. Mức độ có thể tăng từ triển khai/cấu hình sang giám sát, phân tích và ra quyết định. AIOps là dùng kỹ thuật dữ liệu/AI hỗ trợ vận hành trong sách, không phải điều kiện bắt buộc để có automation.',
'Không chỉ dựng nhà tự động; còn phải phát hiện và phản ứng khi thiết bị hỏng hoặc nhu cầu thay đổi.',
'Ví dụ tự xây dựng: đo CPU → phát hiện quá tải liên tiếp → đề xuất thêm bản sao → áp dụng có giới hạn → đo lại. Nếu chỉ có dashboard, hệ thống mới tự động thu thập/hiển thị chứ chưa tự điều chỉnh.',
'Giám sát khác hành động khắc phục. Có bản backup định kỳ chưa chứng minh restore thành công.',
'Tự quyết định cao cần cơ chế giới hạn, quan sát và con người can thiệp khi vượt ngưỡng.',
'Bạn sẽ đo điều gì để kiểm chứng tác vụ backup tự động có ích?',
'Hệ thống chỉ vẽ biểu đồ CPU, không đổi tài nguyên. Điều gì đúng?',
'Đã tự động giám sát nhưng chưa tự động điều chỉnh tài nguyên|Đã tự động sửa mọi lỗi|Không phải automation ở bất kỳ mức nào|Đã bảo đảm backup khôi phục được',
'Đúng: phân biệt thu thập với điều khiển.|Sai: chưa có hành động.|Sai: thu thập có thể tự động.|Sai: không liên quan.',terms='AIOps|monitoring')
lesson('9.4','IaC, khai báo, mệnh lệnh và intent',(54,63),(119,123),'Lệnh thủ công rời rạc khó kiểm tra lịch sử và tái lập trạng thái.',
'Infrastructure as Code (IaC) quản lý mô tả hạ tầng bằng tệp có thể lưu phiên bản và kiểm tra. Mệnh lệnh (imperative) chỉ các bước cần thực hiện. Khai báo (declarative) mô tả trạng thái mong muốn và giao cho công cụ lập hành động. Intent mô tả mục tiêu cấp cao hơn; công cụ phải chuyển mục tiêu thành cấu hình. Tệp YAML tự nó không bảo đảm tính khai báo hoặc idempotent.',
'“Đi thêm ba bước” là mệnh lệnh; “hãy ở vị trí X” là mục tiêu trạng thái. Muốn đạt X vẫn cần người hoặc công cụ biết hiện tại đang ở đâu.',
'Ví dụ tự xây dựng: “có đúng 3 bản sao” khác “thêm 3 bản sao”. Chạy lặp lệnh thêm có thể thành 6; bộ điều khiển khai báo phải đọc hiện trạng và chỉ bù thiếu.',
'Declarative không có nghĩa không còn thuật toán. Công cụ vẫn cần xử lý drift, lỗi API và thứ tự phụ thuộc.',
'Kiểm soát phiên bản giúp xem thay đổi nhưng không tự hoàn tác dữ liệu đã biến đổi. Cần plan/review và kiểm thử.',
'Nếu một người xóa VM ngoài công cụ IaC, cơ chế nào phát hiện khác trạng thái mong muốn?',
'Hiện có 2 bản sao, mục tiêu khai báo là 3. Hành động hội tụ tối thiểu là gì?',
'Tạo thêm 1 bản sao|Tạo thêm 3 bản sao|Xóa cả 2 mà không thay thế|Chỉ đổi tên file YAML',
'Đúng: bù chênh lệch actual/desired.|Sai: nhầm “có 3” với “thêm 3”.|Sai: không hội tụ mục tiêu.|Sai: không tác động tài nguyên.',level='Vận dụng',terms='IaC|declarative|imperative')
lesson('9.5','Push và pull',(64,68),(122,123),'Công cụ trung tâm và các máy được quản lý cần thống nhất cách phân phối cấu hình.',
'Push là bộ điều khiển chủ động gửi/áp cấu hình đến thiết bị. Pull là agent phía thiết bị chủ động lấy mô tả/cấu hình từ nơi quản lý theo chu kỳ hoặc sự kiện. Cả hai cần xác thực, quyền truy cập, xử lý phiên bản và báo trạng thái. Chiều lấy cấu hình không quyết định ngôn ngữ khai báo hay mệnh lệnh.',
'Người quản lý đến từng phòng giao bản hướng dẫn là push; mỗi phòng đến lấy phiên bản mới là pull.',
'Ví dụ tự xây dựng: 1.000 agent pull mỗi phút cùng một giây tạo đỉnh tải. Thêm độ lệch ngẫu nhiên chu kỳ có thể phân tán tải, nhưng vẫn phải kiểm tra giới hạn dịch vụ cấu hình.',
'Pull không đồng nghĩa không cần mạng; push không có nghĩa phản hồi sức khỏe tự quay về.',
'Push cần tiếp cận thiết bị; pull phụ thuộc agent và độ trễ lấy cập nhật. Thiết kế cần xử lý khi nguồn cấu hình không truy cập được.',
'Vì sao cập nhật pull có thể đến các máy ở thời điểm khác nhau?',
'Agent trên mỗi máy chủ động định kỳ lấy cấu hình. Đây là mô hình nào?',
'Pull|Push|Emulation|SAN',
'Đúng: thiết bị khởi phát lấy cấu hình.|Sai: push là trung tâm khởi phát gửi/áp.|Sai: giả lập CPU.|Sai: mạng lưu trữ.',terms='push|pull')

chapter('c10','Điều phối và Kubernetes','10-orchestration(1).pdf',(127,140),'Ai phối hợp triển khai, mở rộng và phục hồi?|Pod và các thành phần Kubernetes làm gì?', 'Phân biệt automation với orchestration|Phân tích placement, scaling, rollout và discovery|Theo vết yêu cầu từ API đến node chạy Pod',['6.4','9.4'], 'Cơ chế điều phối được duy trì bằng controller ở chương 13.')
lesson('10.1','Điều phối vòng đời dịch vụ',(1,14),(127,130),'Dịch vụ cần nhiều thành phần được triển khai đúng quan hệ và liên tục thích ứng.',
'Điều phối (orchestration) phối hợp nhiều tác vụ tự động trên phạm vi dịch vụ: triển khai, cấu hình, theo dõi, mở rộng và phục hồi. Các khối phần mềm có thể tạm thời, được thay thế thay vì sửa tại chỗ. Kubernetes là ví dụ điều phối container; không tự thiết kế logic ứng dụng, không thay mọi công cụ build hoặc quản lý dữ liệu.',
'Từng nhạc cụ có thể chơi tự động; điều phối quyết định chúng phối hợp vào lúc nào và phản ứng khi một phần ngừng.',
'Ví dụ tự xây dựng: frontend phụ thuộc API và DB. Quy trình tạo từng container phải đi kèm kiểm tra ready, cấu hình địa chỉ, phân phối lưu lượng và xử lý khi DB chưa sẵn sàng.',
'Orchestration không chỉ là chạy nhiều lệnh liên tiếp một lần. Một thành phần sống ngắn không có nghĩa dữ liệu của nó không quan trọng.',
'Tăng khả năng vận hành nhưng thêm hệ thống điều khiển cần bảo vệ và chẩn đoán.',
'Khi một container chết sau triển khai 3 giờ, điều phối cần xử lý gì mà script cài đặt một lần có thể không làm?',
'Điểm nổi bật của orchestration so với một tác vụ automation đơn lẻ là gì?',
'Phối hợp nhiều tác vụ và phụ thuộc trong vòng đời dịch vụ|Chỉ biên dịch một file|Thay thế thiết kế ứng dụng|Loại bỏ nhu cầu giám sát',
'Đúng: phạm vi và phối hợp là khác biệt.|Đây là tác vụ đơn.|Sai: kiến trúc vẫn cần thiết.|Sai: giám sát là đầu vào điều khiển.',terms='orchestration')
lesson('10.2','Placement, requests và autoscaling',(15,29),(138,140),'Bản sao cần được đặt trên node đủ tài nguyên; số bản sao cần phù hợp tải.',
'Placement chọn nơi chạy theo nhu cầu và ràng buộc. Ước lượng/request tài nguyên giúp scheduler tránh xếp quá nhiều workload lên một node. Monitoring đo sử dụng thật; autoscaling điều chỉnh số bản sao hoặc năng lực theo chỉ số và chính sách. Không gian CPU, RAM, quy tắc vị trí và trạng thái sẵn sàng đều ảnh hưởng quyết định.',
'Xếp vali vào khoang phải xét cả thể tích lẫn giới hạn cân nặng; chỉ xem CPU rảnh bỏ qua RAM cũng giống vậy.',
'Ví dụ tự xây dựng: node còn 2 CPU và 1 GiB RAM; Pod request 1 CPU, 2 GiB RAM không vừa. Thêm bản sao ở mức desired không có nghĩa scheduler có node để đặt.',
'CPU thực dùng thấp không chứng minh requests đã nhỏ. Tăng số Pod không tự thêm node nếu không có cơ chế khác.',
'Đặt chặt nâng sử dụng nhưng giảm khoảng trống dự phòng. Autoscaling cần thời gian đo và khởi động.',
'Vì sao desired replicas là 10 nhưng ready replicas có thể chỉ là 6?',
'Node còn 2 CPU và 1 GiB RAM. Pod request 1 CPU và 2 GiB RAM. Kết luận nào đúng?',
'Không vừa theo RAM dù CPU còn đủ|Vừa vì chỉ cần so CPU|Vừa vì RAM request luôn bị bỏ qua|Chắc chắn chạy nếu đổi tên Pod',
'Đúng: phải thỏa tất cả tài nguyên yêu cầu.|Sai: bỏ một chiều ràng buộc.|Sai: trái mô hình placement.|Sai: tên không tăng tài nguyên.',level='Vận dụng',terms='scheduler|autoscaling')
lesson('10.3','Cân bằng tải, phục hồi, rollout và discovery',(30,49),(138,140),'Bản sao thay đổi địa chỉ và phiên bản trong lúc người dùng vẫn gửi yêu cầu.',
'Load balancing phân yêu cầu vào endpoint khỏe. Phục hồi thay bản sao lỗi để đạt mục tiêu. Rolling update thay dần phiên bản; rollback quay về phiên bản phù hợp khi phát hiện lỗi. Discovery cung cấp cách tìm dịch vụ mà không đóng đinh IP từng Pod. Readiness phải phản ánh khả năng phục vụ, không chỉ tiến trình đã tồn tại.',
'Quầy đang thay nhân viên vẫn có thể phục vụ nếu còn đủ quầy khỏe và khách được hướng đến đúng chỗ.',
'Ví dụ tự xây dựng: cập nhật 4 bản sao từng chiếc. Nếu bản mới trả lỗi, dừng rollout và quay lại. Migration schema DB không tương thích ngược có thể khiến chỉ rollback container là chưa đủ.',
'Restart không sửa được lỗi dữ liệu hay lỗi lặp lại trong image. Rollback mã không bảo đảm rollback side effect.',
'Cần đủ tài nguyên cho phần cũ và mới cùng tồn tại; xác định chỉ số lỗi và điều kiện dừng trước khi cập nhật.',
'Vì sao chạy được process không phải bằng chứng endpoint đã ready?',
'Để tránh đưa lưu lượng vào bản sao đang khởi tạo, hệ thống cần đánh giá gì?',
'Khả năng sẵn sàng phục vụ của endpoint|Chỉ tên image ngắn hay dài|Chỉ số dòng Dockerfile|Chỉ thời gian máy vật lý đã bật',
'Đúng: readiness gắn với phục vụ.|Sai: không đo sức khỏe.|Sai: không quyết định ready.|Sai: host uptime không chứng minh app ready.',level='Vận dụng',terms='rollout|rollback|service discovery|readiness')
lesson('10.4','Cluster, Pod, template và init container',(50,60),(129,135),'Nhiều container gắn bó cần một đơn vị triển khai và vòng đời chung.',
'Kubernetes quản lý Pod làm đơn vị chạy có thể gồm một hoặc nhiều container liên quan, chia sẻ mạng của Pod và các volume được khai báo. Template mô tả cách tạo Pod. Init container thông thường chạy hoàn tất theo thứ tự trước app container để chuẩn bị môi trường; đây là mô hình trong tài liệu, không khảo sát các tính năng mới ngoài phạm vi.',
'Pod là một nhóm người làm cùng trạm với địa chỉ chung; không phải một rack vật lý và không phải toàn bộ microservice.',
'Ví dụ tự xây dựng: init container kiểm tra file cấu hình rồi kết thúc; app container bắt đầu phục vụ. Nếu init cứ lỗi, Pod có thể chưa đưa ứng dụng lên dù đã có node.',
'Pod không phải một máy ảo có OS riêng. Nhiều Pod của cùng dịch vụ không mặc định cùng một IP hoặc cùng đĩa ghi.',
'Gộp quá nhiều container không liên quan làm mất khả năng scale độc lập; tách những phần luôn cần chung vòng đời lại tăng phối hợp.',
'Vì sao đặt frontend và tác vụ phân tích không liên quan vào cùng Pod có thể gây khó scale?',
'Vai trò của init container theo mô hình bài học là gì?',
'Hoàn tất việc chuẩn bị trước khi app container bắt đầu|Thay mọi control plane|Luôn nhận toàn bộ lưu lượng web|Là tên khác của rack vật lý',
'Đúng: thực hiện điều kiện khởi tạo.|Sai: ở cấp Pod.|Sai: không phải chức năng bắt buộc.|Sai: khác khái niệm.',terms='Kubernetes Pod|init container|template')
lesson('10.5','Control plane và worker node',(61,67),(135,138),'Ai lưu mục tiêu, ai chọn node và ai thực sự chạy container?',
'API server cung cấp giao diện quản lý. Kho trạng thái lưu dữ liệu điều khiển; scheduler chọn node cho Pod chưa gán; controller theo dõi và điều chỉnh để hội tụ. Trên worker, kubelet phối hợp trạng thái Pod với container runtime; thành phần mạng phục vụ kết nối theo cấu hình. Các thành phần giao tiếp qua API thay vì một chuỗi gọi trực tiếp duy nhất.',
'Ban điều phối giữ đơn và phân công; tổ tại hiện trường tạo môi trường và làm công việc. Ban điều phối không trực tiếp chạy logic ứng dụng thay mọi worker.',
'Ví dụ tự xây dựng: gửi Deployment qua API → controller tạo Pod cần thiết → scheduler gán node → kubelet nhận yêu cầu và runtime chạy container → trạng thái được báo lại. Đây là lược đồ khái niệm, không phải mọi chi tiết mạng và retry.',
'Scheduler không tự build image. Controller manager không phải tập hợp container ứng dụng.',
'Control plane cần được vận hành tin cậy và bảo vệ quyền API; mất điều khiển không nhất thiết khiến mọi process worker dừng ngay, nhưng ngăn nhiều thao tác quản lý.',
'Theo vết một Pod Pending: thiếu node đủ tài nguyên khác lỗi image pull như thế nào?',
'Thành phần nào chọn node cho Pod chưa được gán?',
'Scheduler|Registry image|Hệ thống file trong app|Trình duyệt người dùng',
'Đúng: scheduler thực hiện placement.|Sai: registry phân phối image.|Sai: không chọn node.|Sai: chỉ gửi tương tác tới ứng dụng.',terms='control plane|kubelet|scheduler')

chapter('c11','MapReduce và Hadoop','11-mapreduce(1).pdf',(145,160),'Bài toán nào chia dữ liệu được?|Shuffle làm gì?|HDFS hỗ trợ tính toán ra sao?', 'Tự chạy ví dụ đếm từ qua map–group–reduce|Phân tích skew và chi phí truyền dữ liệu|Phân biệt NameNode với DataNode',['1.5','8.1'], 'Đối chiếu với Amdahl và kiến trúc microservices: song song dữ liệu không giống chia chức năng.')
lesson('11.1','Cloud-native và song song dữ liệu',(1,14),(145,149),'Nhiều CPU không giúp nếu không tìm được phần việc độc lập.',
'Cloud-native trong bài chỉ phần mềm thiết kế để tận dụng môi trường cloud thay vì chỉ đưa một ứng dụng cũ lên VM. Data parallelism áp cùng loại thao tác lên nhiều phần dữ liệu. Chia việc phải tính bước chuẩn bị, truyền dữ liệu, phối hợp và gộp kết quả. Không phải bài toán nào cũng có phần dữ liệu độc lập.',
'Nhiều người có thể chấm các phiếu độc lập, nhưng nếu phiếu sau phải chờ quyết định phiếu trước thì cách chia đó không còn đúng.',
'Ví dụ tự xây dựng: tính histogram của 1 triệu ảnh có thể chia theo ảnh và cộng histogram. Một chuỗi tính toán phụ thuộc kết quả liền trước cần mô hình khác.',
'Chạy trên cloud không tự thành cloud-native. Thêm worker có thể làm chậm bài toán nhỏ vì overhead.',
'Lợi ích phụ thuộc tỷ lệ tính toán/truyền dữ liệu và độ cân bằng tải; đo thời gian toàn pipeline.',
'Bạn cần chứng minh tính chất gì để cộng kết quả histogram từng phần?',
'Tại sao 100 worker có thể chậm hơn 4 worker với tập dữ liệu nhỏ?',
'Chi phí chia, truyền và gộp có thể lớn hơn phần tính tiết kiệm|Vì cloud không có CPU|Vì song song không bao giờ có ích|Vì mọi worker dùng chung một thanh RAM vật lý',
'Đúng: overhead có thể chi phối.|Sai: có tài nguyên thật.|Sai: tùy bài toán và kích thước.|Sai: không đúng mô hình phân tán.',terms='cloud-native|data parallelism')
lesson('11.2','Map, shuffle/group và reduce',(15,30),(149,153),'Cần một cách biểu diễn chung để phân tán tính toán theo khóa.',
'Map biến mỗi phần tử đầu vào thành không hoặc nhiều cặp khóa–giá trị. Shuffle/group gom các giá trị cùng khóa để reducer xử lý; reduce tạo đầu ra theo nhóm. Chia input và chia khóa là hai bước khác nhau. Đếm từ dùng map phát (từ,1), group theo từ rồi reduce cộng số đếm.',
'Nhiều người đọc các trang, ghi phiếu theo từ; gom tất cả phiếu cùng từ vào một chồng rồi đếm từng chồng.',
'Ví dụ tự xây dựng: “mây nhanh mây”. Map → (mây,1),(nhanh,1),(mây,1). Group → mây:[1,1], nhanh:[1]. Reduce → mây:2, nhanh:1. Nếu hai mapper phát cùng từ, các giá trị đó phải cùng tới nhóm khóa tương ứng.',
'Reduce không nhận một giá trị duy nhất cho mỗi khóa trước khi gom. Hash partition không tự gộp hay cộng giá trị.',
'Shuffle có thể dùng nhiều mạng và đĩa. Reducer chậm hoặc khóa lệch tải có thể quyết định thời gian hoàn thành.',
'Nếu không group trước reduce, đếm một từ xuất hiện ở nhiều mapper bị sai như thế nào?',
'Ở word count, bước nào gom các số 1 của cùng một từ từ nhiều mapper?',
'Shuffle/group|Chỉ đọc file đầu vào|Chỉ đặt tên worker|Chỉ tạo VM',
'Đúng: tập hợp theo khóa.|Sai: chưa gom kết quả map.|Sai: không xử lý khóa.|Sai: mới cấp compute.',terms='MapReduce|shuffle|reducer')
lesson('11.3','Chia tải, hash, skew và overhead',(31,35),(152,154),'Chia đều số phần tử chưa chắc chia đều thời gian xử lý hoặc số giá trị trên khóa.',
'Partition bằng hash ánh xạ khóa tới reducer để phân bố. Hash tốt không đảm bảo cân bằng khi một khóa có số lần xuất hiện vượt trội hoặc các bản ghi có chi phí xử lý khác nhau. Data locality đặt tác vụ gần dữ liệu để giảm truyền; tách/gộp và lập lịch vẫn tạo overhead.',
'Chia hồ sơ theo chữ đầu tên không giúp nếu một nhóm có quá nhiều hồ sơ. Đếm số tập giấy chưa đủ, phải xét cả độ dày.',
'Ví dụ tự xây dựng: 90% log có khóa “OK”. Hash gửi mọi bản ghi của khóa này vào một reducer; thêm mapper không làm reducer đó nhẹ hơn. Có thể cần tổng hợp cục bộ hợp lệ hoặc chia khóa có thiết kế và gộp lại.',
'Hash không làm một khóa phổ biến biến mất. “Số worker lớn” không là bằng chứng cân tải.',
'Đổi chiến lược partition phải giữ đúng ngữ nghĩa; chia một khóa tùy tiện có thể làm mất tổng cuối cùng.',
'Khi một reducer xử lý 90% dữ liệu, bạn đo gì trước khi tăng số mapper?',
'90% bản ghi có cùng khóa, mỗi khóa đi một reducer. Nút thắt dễ xuất hiện ở đâu?',
'Reducer nhận khóa phổ biến|Chỉ ở màn hình quản trị|Không thể có nút thắt vì dùng hash|Chỉ ở tên file cấu hình',
'Đúng: skew theo khóa.|Không thuộc đường xử lý.|Sai: hash không chia một khóa theo mặc định.|Không giải thích tải dữ liệu.',level='Vận dụng',terms='data skew|data locality|hash partition')
lesson('11.4','Hadoop, HDFS và chịu lỗi',(36,50),(154,160),'Tập dữ liệu lớn phải được lưu và xử lý trên nhiều máy mà không sao chép toàn bộ vào một máy.',
'Hadoop kết hợp các thành phần lưu trữ và xử lý phân tán. Hadoop Distributed File System (HDFS) chia file thành block lớn; NameNode quản lý metadata vị trí/tên, DataNode lưu block. Nhân bản block hỗ trợ chịu lỗi và cho phép chọn nơi xử lý gần bản sao dữ liệu. Slide dùng block 128 MB và hệ số 3 làm cấu hình ví dụ/mặc định trong phạm vi tài liệu, không phải hằng số bắt buộc mọi triển khai.',
'NameNode giữ mục lục kho, DataNode giữ các kiện dữ liệu. Mục lục không phải nơi chứa mọi kiện.',
'Ví dụ tự xây dựng: 10 block, replication factor 3 cần 30 bản block nếu không xét overhead và cơ chế khác. Mất một DataNode không nhất thiết mất dữ liệu nếu mỗi block còn bản sao truy cập được.',
'Nhân bản không là backup lịch sử; xóa nhầm có thể được thực hiện nhất quán trên hệ thống. HDFS không có nghĩa mọi mapper phải tải dữ liệu qua mạng xa.',
'Đọc lớn tuần tự phù hợp hơn nhiều ghi nhỏ cập nhật ngẫu nhiên; phải quản lý cả metadata và độ sẵn sàng của hệ thống điều khiển.',
'Nếu mọi bản sao một block cùng nằm trong một miền lỗi, hệ số nhân bản cao có giúp khi miền đó hỏng không?',
'Trong mô hình HDFS, NameNode chủ yếu giữ gì?',
'Metadata và thông tin vị trí block|Toàn bộ nội dung mọi block thay DataNode|Mọi khóa NAT|Kernel riêng cho từng mapper',
'Đúng: phân biệt metadata và dữ liệu.|Sai: DataNode lưu block.|Sai: thuộc mạng.|Sai: không phải nhiệm vụ HDFS.',terms='Hadoop|HDFS|NameNode|DataNode')

chapter('c12','Microservices và giao tiếp','12-microservices(1).pdf',(163,178),'Chia chức năng đến mức nào là hợp lý?|Giao tiếp từ xa tạo những đánh đổi gì?', 'So sánh monolith và microservices theo tình huống|Phân biệt đồng bộ/bất đồng bộ với mẫu giao tiếp|Giải thích vai trò proxy service mesh',['10.3','11.1'], 'Nhiều thành phần độc lập tạo nhu cầu discovery, giám sát và điều khiển.')
lesson('12.1','Ứng dụng nguyên khối và phân rã',(1,20),(163,167),'Một phần ứng dụng cần scale hoặc cập nhật riêng nhưng bị gắn với toàn bộ gói.',
'Nguyên khối (monolith) đóng nhiều chức năng trong một đơn vị triển khai; các thành phần vẫn có thể được thiết kế module tốt. Microservices tách các chức năng liên quan thành dịch vụ có thể phát triển, triển khai và scale độc lập qua giao diện. Lợi ích gồm phạm vi nhóm nhỏ và scale theo chức năng; không tự có nếu các dịch vụ vẫn phải phát hành đồng thời.',
'Tách các bộ phận thành quầy có hợp đồng giao nhận rõ ràng giúp thay đổi một quầy mà không bắt mọi quầy đổi cùng lúc.',
'Ví dụ tự xây dựng: xử lý ảnh gồm upload, filter, export. Nếu filter nặng CPU, chỉ tăng bản sao filter thay vì nhân cả ứng dụng có thể tiết kiệm. Phải xác định cách dữ liệu ảnh đi giữa các dịch vụ.',
'Monolith có module không phải mặc định thiết kế kém. Một container không tự là một microservice đúng ranh giới nghiệp vụ.',
'Microservices tăng độc lập cục bộ nhưng thêm mạng, vận hành và nhất quán dữ liệu.',
'Khi nào một nhóm nhỏ có thể chọn monolith hợp lý hơn?',
'Tại sao tách bộ lọc ảnh thành dịch vụ riêng có thể có lợi?',
'Có thể scale riêng phần nặng nếu ranh giới và giao tiếp phù hợp|Mọi yêu cầu tự mất độ trễ mạng|Không cần kiểm thử tích hợp|Dữ liệu tự nhất quán dù không có cơ chế',
'Đúng: độc lập mở rộng là lợi ích có điều kiện.|Sai: thường thêm giao tiếp.|Sai: tích hợp càng quan trọng.|Sai: phải thiết kế nhất quán.',terms='microservices|monolith')
lesson('12.2','Lỗi dây chuyền và kích thước dịch vụ',(21,36),(167,171),'Chia quá nhỏ làm nhiều lời gọi và phụ thuộc; chia quá lớn mất tính độc lập.',
'Lỗi dây chuyền xảy ra khi một dịch vụ chậm/lỗi làm các dịch vụ phụ thuộc cạn tài nguyên hoặc sinh tải retry. Độ hạt (granularity) cần dựa trên nghiệp vụ, phần dùng chung và khả năng tái cấu trúc. Những chức năng luôn thay đổi và giao tiếp dày đặc có thể nên ở cùng ranh giới thay vì tách theo mỗi hàm.',
'Quầy chậm có thể làm hàng chờ tràn sang lối đi và ảnh hưởng cả cửa hàng, dù quầy khác chưa hỏng.',
'Ví dụ tự xây dựng: A gọi B với timeout dài; B chậm, A giữ 1.000 request chờ rồi hết thread. Retry không giới hạn từ A làm B quá tải thêm. Phải hạn chế đồng thời, timeout và thiết kế retry phù hợp; đây là diễn giải bổ sung từ rủi ro lỗi dây chuyền.',
'Chia nhỏ không bảo đảm cô lập lỗi. Lỗi logic có thể truyền qua dữ liệu hoặc hợp đồng API.',
'Ranh giới dịch vụ là lựa chọn có thể cần sửa theo số liệu; không có số dòng mã “chuẩn” cho mọi microservice.',
'Vì sao thêm retry có thể làm sự cố nặng hơn?',
'B đang quá tải; A retry tức thì vô hạn mỗi lỗi. Hệ quả có khả năng xảy ra là gì?',
'Tải tăng thêm và lỗi có thể lan sang A|B chắc chắn phục hồi ngay|Mọi request tự được xử lý đúng một lần|Độ trễ mạng bằng không',
'Đúng: retry có thể khuếch đại quá tải.|Sai: không có bảo đảm.|Sai: retry còn có nguy cơ tác dụng lặp.|Sai: không đổi vật lý mạng.',level='Vận dụng',terms='cascading failure|granularity')
lesson('12.3','Đồng bộ, bất đồng bộ và mẫu giao tiếp',(37,57),(171,175),'Dịch vụ cần trao đổi nhưng lựa chọn chờ/không chờ ảnh hưởng tài nguyên và thiết kế lỗi.',
'Giao tiếp đồng bộ khiến tiến trình xử lý phụ thuộc vào việc chờ kết quả theo luồng điều khiển. Bất đồng bộ tách việc gửi với lúc nhận/xử lý kết quả. Request/response, streaming và message passing là các mẫu giao tiếp; chúng không khớp một-một tuyệt đối với một cách lập trình đồng bộ. Hàng đợi có thể đệm tải nhưng cần quy tắc xác nhận, lỗi và giao lại.',
'Gọi điện chờ trả lời khác gửi thư rồi làm việc khác; gửi thư không bảo đảm thư được xử lý ngay hoặc chỉ một lần.',
'Ví dụ tự xây dựng: API nhận job chỉnh ảnh trả mã job. Worker xử lý sau, client xem trạng thái. Cần lưu trạng thái bền vững và thiết kế khi job được giao lại, không chỉ đổi hàm thành async.',
'Bất đồng bộ không tự nhanh hơn về thời gian hoàn thành công việc. HTTP request/response có thể được dùng với client I/O bất đồng bộ.',
'Giảm thời gian chặn có thể tăng phức tạp theo dõi và nhất quán cuối cùng; chọn theo hợp đồng người dùng.',
'Khi trả “đã nhận job”, ứng dụng có thể nói “đã xử lý thành công” chưa?',
'API trả mã job trước khi worker hoàn thành. Client nên hiểu gì?',
'Yêu cầu đã được tiếp nhận theo hợp đồng, cần theo dõi kết quả|Ảnh chắc chắn đã xử lý xong|Không còn cần lưu trạng thái job|Job không bao giờ có thể lỗi',
'Đúng: tách tiếp nhận khỏi hoàn tất.|Sai: worker chưa xong.|Sai: cần nơi theo dõi.|Sai: xử lý vẫn có thể lỗi.',terms='synchronous|asynchronous|message queue')
lesson('12.4','Mã hóa dữ liệu và hợp đồng giao tiếp',(58,60),(171,174),'Hai dịch vụ phải thống nhất cách biểu diễn dữ liệu thay vì gửi đối tượng bộ nhớ tùy ý.',
'JSON, XML, YAML, CSV là các ví dụ biểu diễn dạng văn bản; Protocol Buffers và các định dạng nhị phân có quy tắc riêng. Hợp đồng gồm kiểu dữ liệu, trường bắt buộc, phiên bản và xử lý trường không biết. Dễ đọc bằng mắt khác với hiệu quả kích thước và khả năng tiến hóa schema.',
'Gửi biểu mẫu cần thống nhất mỗi ô nghĩa gì; viết chữ hay mã số không thay thế việc thống nhất ngữ nghĩa.',
'Ví dụ tự xây dựng: dịch vụ A gửi trường price theo đồng, B đọc theo nghìn đồng. JSON vẫn hợp lệ về cú pháp nhưng kết quả sai 1.000 lần; phải ghi đơn vị trong hợp đồng.',
'Nhị phân không đồng nghĩa mã hóa bảo mật. Dữ liệu deserialize được chưa chứng minh an toàn hoặc đúng ngữ nghĩa.',
'Văn bản thuận tiện gỡ lỗi nhưng có thể lớn; schema chặt hỗ trợ kiểm tra nhưng cần quy trình tương thích phiên bản.',
'Khi đổi trường từ bắt buộc sang tùy chọn, những client nào cần kiểm tra lại?',
'JSON hợp lệ nhưng hai bên hiểu đơn vị giá khác nhau. Lỗi thuộc đâu?',
'Hợp đồng ngữ nghĩa dữ liệu|Chắc chắn do VLAN ID|Do JSON luôn mã hóa sai|Do CPU không có đa lõi',
'Đúng: cú pháp đúng không bảo đảm cùng ý nghĩa.|Không có bằng chứng lỗi mạng.|Sai: vấn đề thỏa thuận đơn vị.|Không liên quan.',level='Vận dụng',terms='serialization|schema')
lesson('12.5','Service mesh và proxy',(61,67),(175,178),'Các dịch vụ đều cần discovery, cân bằng tải, bảo mật và quan sát giao tiếp.',
'Service mesh quản lý giao tiếp giữa dịch vụ bằng lớp proxy và điều khiển chính sách. Proxy trung gian có thể chọn endpoint, thu thập telemetry và thực thi chính sách bảo mật. Mẫu sidecar là một cách bố trí, không phải định nghĩa bắt buộc mọi mesh. Logic nghiệp vụ vẫn ở dịch vụ, không tự chuyển sang proxy.',
'Một mạng các quầy điều phối giao nhận giúp các nhóm dùng chung quy tắc vận chuyển thay vì nhóm nào cũng tự viết lại.',
'Ví dụ tự xây dựng: nhiều bản sao filter thay IP khi scale. Proxy nhận thông tin endpoint mới rồi phân tải; nếu danh sách endpoint cũ, proxy vẫn có thể gửi sai.',
'Mesh không sửa lỗi thuật toán hoặc bảo đảm giao dịch nghiệp vụ xuyên nhiều DB. Mã hóa giữa proxy không tự bảo vệ mọi đoạn trước/sau proxy.',
'Thêm proxy và control plane gây overhead, cần cấu hình và quan sát chính nó.',
'Phân biệt lỗi chọn endpoint ở mesh với lỗi giá tiền do logic ứng dụng.',
'Việc nào phù hợp trực tiếp với service mesh?',
'Thực thi chính sách giao tiếp và phân tải giữa dịch vụ|Tự sửa mọi schema nghiệp vụ|Thay thế toàn bộ DB|Tăng tốc mọi thuật toán trong app',
'Đúng: thuộc lớp giao tiếp.|Sai: cần thay ứng dụng/hợp đồng.|Sai: không phải lưu trữ nghiệp vụ.|Sai: không sửa thuật toán.',terms='service mesh|proxy')

chapter('c13','Controller và vòng điều khiển','13-controllers(1).pdf',(181,192),'Hệ thống biết cần sửa gì như thế nào?|Vì sao autoscaling dao động?', 'Mô tả vòng observe–compare–act|Phân tích độ trễ và cường độ điều chỉnh|Phân biệt event-driven với phản ứng tức thời tuyệt đối',['9.4','10.5'], 'Nền tư duy cho autoscaling, tự phục hồi và operator.')
lesson('13.1','Giám sát hệ phân tán và trạng thái mong muốn',(1,20),(181,185),'Số lượng bản sao và vị trí động làm cách chờ người sửa từng node không đủ.',
'Vòng điều khiển lấy trạng thái quan sát, so với trạng thái mong muốn rồi thực hiện hành động điều chỉnh. Monitoring có đánh đổi giữa độ đầy đủ, tần suất và overhead. Mục tiêu khai báo như “có 3 bản sao khỏe” khác một lệnh “thêm 3”. Bộ điều khiển phải tiếp tục quan sát vì hệ thống có thể thay đổi sau một lần hành động.',
'Bộ điều nhiệt đo nhiệt độ, so với mục tiêu rồi bật/tắt thiết bị; không chỉ bật một lần và bỏ đi.',
'Ví dụ tự xây dựng: desired 3, actual healthy 2. Controller tạo một bản sao và chờ quan sát mới. Nếu dùng số object tồn tại thay số ready không đúng mục tiêu, nó có thể nghĩ đủ dù dịch vụ chưa sẵn sàng.',
'Quan sát là ảnh chụp có độ trễ, không phải toàn bộ sự thật tức thời. Timeout probe không chứng minh chắc chắn node đã chết.',
'Probe quá thường xuyên tốn tài nguyên; quá thưa kéo dài phát hiện lỗi.',
'Định nghĩa healthy bạn dùng có kiểm tra được phụ thuộc thật của dịch vụ không?',
'Desired 3 bản sao khỏe, hiện có 2. Vòng điều khiển nên hướng tới điều gì?',
'Bù phần thiếu và quan sát lại cho tới hội tụ|Chỉ chạy một lần rồi không theo dõi|Luôn thêm đúng 3 bất kể actual|Coi probe timeout là bằng chứng chắc chắn máy hỏng vật lý',
'Đúng: hành động theo chênh lệch, tiếp tục đo.|Sai: trạng thái có thể đổi.|Sai: nhầm mục tiêu với tăng thêm.|Sai: timeout còn có thể do mạng/chậm.',terms='controller|control loop|desired state')
lesson('13.2','Độ trễ, hysteresis và dao động',(21,43),(185,186),'Đo quá sớm sau hành động dễ khiến bộ điều khiển nghĩ tác động chưa đủ rồi tiếp tục điều chỉnh quá mức.',
'Từ lúc quyết định thêm bản sao đến khi bản sao ready, nhận tải và được phản ánh trong metric có nhiều độ trễ. Slide dùng từ hysteresis để nói ảnh hưởng phản ứng trễ; trong cách dùng kỹ thuật rộng, hysteresis còn chỉ đáp ứng phụ thuộc lịch sử/ngưỡng khác nhau. Cửa sổ ổn định và mức điều chỉnh phù hợp giúp giảm scale ra/vào liên tục. Phải phân biệt dao động tự gây với tải đầu vào thực sự thay đổi.',
'Vặn vòi nước nóng quá mạnh vì chưa chờ nước tới rồi vặn ngược có thể làm nhiệt độ dao động.',
'Ví dụ tự xây dựng: metric lấy mỗi 10 giây nhưng instance cần 60 giây sẵn sàng. Sáu lần tăng liên tiếp có thể được ra lệnh trước khi lần đầu có tác dụng. Theo dõi tài nguyên đang khởi tạo và giới hạn tốc độ đổi giúp tránh điều đó.',
'Chu kỳ ngắn hơn không luôn tốt hơn. Cửa sổ ổn định không tạo thêm năng lực mà đổi cách phản ứng.',
'Chậm quá bỏ lỡ tải tăng; mạnh quá vượt mục tiêu. Tham số phải dựa trên độ trễ thực tế và ràng buộc dịch vụ.',
'Vì sao ngưỡng scale-in và scale-out khác nhau có thể giảm đổi chiều liên tục?',
'Instance cần 60 giây để phục vụ nhưng controller tăng thêm mỗi 10 giây theo số đo cũ. Rủi ro chính là gì?',
'Điều chỉnh quá mức trước khi hiệu ứng cũ xuất hiện|RAM tự nhân đôi không cần máy|Tự loại bỏ mọi độ trễ|Bảo đảm không bao giờ scale-in',
'Đúng: phản hồi trễ gây hành động dồn.|Sai: không có cơ chế đó.|Sai: thời gian khởi tạo vẫn có.|Sai: không có bảo đảm.',level='Vận dụng',terms='hysteresis|stabilization window')
lesson('13.3','Controller sự kiện, custom resource và operator',(44,54),(186,192),'Polling toàn bộ trạng thái liên tục tốn kém; nghiệp vụ vận hành đặc thù cần thêm mô tả cấp cao.',
'Controller Kubernetes theo dõi tài nguyên qua sự kiện/watch và đưa đối tượng cần xử lý vào vòng reconcile. Sự kiện là tín hiệu cần kiểm tra lại trạng thái, không bảo đảm mỗi chuyển đổi chỉ xảy ra đúng một lần. Custom Resource Definition (CRD) mở rộng kiểu tài nguyên; custom controller thêm hành vi xử lý. Operator đóng gói tri thức vận hành một dịch vụ bằng controller và tài nguyên tùy chỉnh theo sách bổ trợ.',
'Chuông báo có thay đổi giúp bạn biết khi nào xem lại danh sách công việc; vẫn cần kiểm tra tình trạng hiện tại trước khi làm.',
'Ví dụ tự xây dựng: tài nguyên mô tả “cụm DB có 3 bản sao và backup hằng ngày”. Chỉ khai báo CRD mới tạo kiểu API; controller/operator phải hiện thực việc tạo và duy trì DB cùng lịch backup.',
'CRD một mình không làm tài nguyên vật lý xuất hiện. Event-driven không có nghĩa không có retry, hàng đợi hoặc độ trễ.',
'Controller cần idempotent, phân quyền và quan sát trạng thái; tự động hóa tác vụ DB sai có thể gây hại lớn.',
'Nếu controller nhận lại cùng một sự kiện, vì sao tạo tài nguyên mới vô điều kiện là sai?',
'CRD đã được cài nhưng chưa có controller tương ứng. Điều gì đúng?',
'Có kiểu API mới nhưng chưa tự có logic vận hành dịch vụ|DB tự chạy đủ 3 bản sao|Mọi backup đã được kiểm thử|Scheduler tự hiểu toàn bộ nghiệp vụ DB',
'Đúng: schema và hành vi là hai phần.|Sai: cần bộ thực thi.|Sai: không có bằng chứng.|Sai: scheduler không tự có logic nghiệp vụ.',terms='reconciliation|CRD|operator')

chapter('c14','Serverless và xử lý sự kiện','14-serverless(1).pdf',(195,204),'Ai chạy server khi lập trình viên chỉ viết hàm?|Stateless có nghĩa không có dữ liệu không?', 'Theo vết một sự kiện từ API đến hàm và DB|Phân tích cold start và giới hạn runtime|Chọn FaaS cho tải gián đoạn',['10.1','12.3'], 'Tài liệu FaaS được liên kết ở mô-đun F3 để soi kiến trúc OpenFaaS/OpenWhisk.')
lesson('14.1','Từ client-server đến chi phí bản sao thường trực',(1,15),(195,198),'Một server xử lý nhiều client cần concurrency; nhiều server lại cần phân tải, trạng thái và quản lý.',
'Server thường khởi động trước và chờ client kết nối. Có thể xử lý tuần tự, nhiều luồng hoặc I/O bất đồng bộ theo thiết kế. Mở rộng qua nhiều VM/Pod đòi hỏi load balancer và các phụ thuộc dùng chung. Giữ tối thiểu nhiều bản sao thường trực phát sinh chi phí ngay cả khi ít yêu cầu.',
'Mở sẵn nhiều quầy để không để khách chờ nhưng vẫn phải trả chi phí khi không có khách.',
'Ví dụ tự xây dựng: app todo có nội dung tĩnh, REST API và DB. Scale API không làm DB tự scale. Nếu cả ngày chỉ có vài sự kiện, chi phí giữ API thường trực có thể không tương xứng.',
'Chuyển sang microservices không tự loại bỏ số bản sao nhàn rỗi. Một server có thể phục vụ nhiều client chứ không bắt buộc chỉ một.',
'Bản sao ấm giảm latency khởi tạo nhưng tốn năng lực nền. Chọn theo tải và yêu cầu phản hồi.',
'Vì sao scale tầng API vẫn có thể gặp trần hiệu năng DB?',
'Chi phí nào FaaS có thể giúp giảm trong tải gián đoạn?',
'Compute nhàn rỗi do phải giữ server ứng dụng thường trực|Mọi chi phí lưu dữ liệu vĩnh viễn|Mọi chi phí mạng trong mọi trường hợp|Mọi chi phí phát triển phần mềm',
'Đúng: scale-to-zero có thể giảm phần compute không dùng.|Sai: lưu trữ vẫn cần.|Sai: truyền dữ liệu vẫn có thể tính phí.|Sai: vẫn phải thiết kế và phát triển.',terms='client-server')
lesson('14.2','Hàm, sự kiện, runtime và stateless',(16,28),(198,202),'Nhà phát triển muốn xử lý một sự kiện mà không tự điều phối từng server.',
'Function as a Service (FaaS) nhận mã hàm và để nền tảng kích hoạt, bố trí, giám sát các phiên xử lý. Sự kiện có thể là HTTP, thông điệp hoặc thay đổi dữ liệu. Stateless nghĩa không dựa vào bộ nhớ cục bộ của một phiên hàm để giữ trạng thái bền qua các lần gọi; dữ liệu nghiệp vụ vẫn được lưu ở DB/object storage. Hàm có thể gây tác dụng phụ, nên retry cần idempotency.',
'Được gọi đến xử lý một phiếu công việc rồi rời đi; hồ sơ quan trọng phải lưu vào kho bền vững chứ không để trong túi người xử lý.',
'Ví dụ tự xây dựng: addTodo nhận event có id. Hàm kiểm tra/ghi DB và trả kết quả. Nếu nền tảng giao lại event sau lỗi mạng, khóa idempotency giúp tránh tạo hai todo. Không giả định mỗi sự kiện chỉ gọi hàm một lần.',
'Stateless không phải hàm thuần không side effect. “Serverless” không có nghĩa không có máy chủ; trách nhiệm vận hành được chuyển lên nền tảng.',
'Runtime quy định ngôn ngữ, tài nguyên, thời gian chạy và cách nhận sự kiện. Cần thiết kế cho retry và giao lại.',
'Nếu lưu danh sách todo chỉ ở biến toàn cục của hàm, điều gì xảy ra khi lần gọi sau đến instance khác?',
'Trong FaaS stateless, trạng thái nghiệp vụ cần tồn tại qua nhiều lần gọi nên đặt ở đâu?',
'Dịch vụ lưu trữ bền vững với thiết kế truy cập phù hợp|Chỉ biến cục bộ của một phiên hàm|Chỉ stdout không được thu thập|Chỉ tên container ngẫu nhiên',
'Đúng: không phụ thuộc một instance tạm thời.|Sai: mất khi phiên kết thúc hoặc đổi instance.|Sai: không là kho dữ liệu nghiệp vụ.|Sai: không chứa dữ liệu bền.',terms='FaaS|stateless|event-driven')
lesson('14.3','Cold start, scale-to-zero và đánh đổi',(29,30),(202,204),'Tiện lợi và tính phí theo sử dụng không có nghĩa luôn rẻ hoặc đáp ứng tức thời.',
'Cold start là phần chậm do chuẩn bị môi trường trước khi xử lý; mức độ tùy nền tảng và ứng dụng. Scale-to-zero cho phép không duy trì instance khi nhàn rỗi trong mô hình hỗ trợ. Concurrency quota, tốc độ tăng tài nguyên và phụ thuộc vẫn giới hạn. Slide 29 nói “infinite scalability”; ứng dụng hiểu đó là mục tiêu trừu tượng hóa mở rộng, không khẳng định năng lực thực tế vô hạn.',
'Gọi người đến làm theo việc giảm thời gian trả công nhàn rỗi, nhưng vẫn có thời gian chuẩn bị và số người hữu hạn.',
'Ví dụ tự xây dựng: hệ thống cần phản hồi dưới 100 ms, cold start đo được 800 ms. Phải xét giữ môi trường ấm, thay nền tảng hoặc mô hình compute khác; chỉ thấy chi phí request rẻ chưa đủ.',
'FaaS không luôn rẻ cho tải cao liên tục. Debug và quan sát có thể khó khi runtime do nhà cung cấp kiểm soát.',
'Đánh giá bằng phân bố latency, tổng chi phí và lỗi đầu cuối, không chỉ thời gian hàm khi đã ấm.',
'Vì sao đo trung bình latency có thể che các lần cold start gây khó chịu?',
'SLA ứng dụng đòi dưới 100 ms; cold start có thể 800 ms. Việc cần làm là gì?',
'Đánh giá và thay thiết kế để đáp ứng độ trễ, không chỉ so giá mỗi lần gọi|Khẳng định serverless luôn đáp ứng|Bỏ qua các request đầu tiên khi nghiệm thu|Cho rằng scale-to-zero giữ mọi instance ấm',
'Đúng: latency là điều kiện quyết định.|Sai: phải đo theo trường hợp.|Sai: người dùng vẫn gặp các lần đó.|Sai: zero nghĩa không giữ instance compute theo mô hình.',level='Vận dụng',terms='cold start|scale-to-zero')

chapter('c15','DevOps, CI/CD và SRE','15-devops(1).pdf',(207,214),'Vì sao dev và vận hành có thể xung đột?|Làm thế nào phát hành nhanh mà kiểm soát rủi ro?', 'Phân biệt CI, delivery và deployment|Chọn sandbox, canary hay blue-green|Tính error budget từ mục tiêu độ sẵn sàng',['10.3','12.1'], 'Kết nối kiểm thử, điều phối và quan sát thành vòng cải tiến phần mềm.')
lesson('15.1','Vòng đời thực và văn hóa DevOps',(1,22),(207,211),'Phần mềm tiếp tục thay đổi sau bàn giao vì lỗi, yêu cầu mới và môi trường phụ thuộc.',
'Nhóm phát triển muốn ra tính năng nhanh; QA ưu tiên chất lượng; vận hành ưu tiên ổn định và tài nguyên. DevOps là cách tổ chức/văn hóa chia sẻ trách nhiệm, phối hợp và tự động hóa vòng phát triển–vận hành, không chỉ một chức danh hay công cụ. Module nhỏ, kiểm thử rộng và quản lý phiên bản hỗ trợ thay đổi có kiểm soát.',
'Các nhóm cùng chịu trách nhiệm cho chuyến hàng tới người dùng, thay vì chỉ đẩy thùng qua ranh giới rồi coi như xong.',
'Ví dụ tự xây dựng: một lỗi chỉ xuất hiện sau triển khai. Dev và ops dùng cùng metric, log và quy trình hậu sự cố để sửa nguyên nhân, rồi thêm kiểm tra phù hợp vào pipeline.',
'DevOps không có nghĩa bỏ QA hoặc cho mọi người quyền production vô hạn. Tự động hóa không thay thế phối hợp mục tiêu.',
'Đổi cách làm có chi phí đào tạo và hạ tầng; phát hành nhanh thiếu kiểm tra có thể tăng sự cố toàn hệ.',
'Nêu một thay đổi về cách cộng tác và một thay đổi về công cụ; vì sao chỉ công cụ chưa đủ?',
'Định nghĩa nào phù hợp nhất với DevOps trong tài liệu?',
'Cách tổ chức và văn hóa phối hợp phát triển, QA, vận hành dựa nhiều vào tự động hóa|Một tên khác của Docker|Bỏ toàn bộ kiểm thử để ra nhanh|Chỉ thuê thêm một người trực đêm',
'Đúng: có cả tổ chức và kỹ thuật.|Sai: Docker chỉ là công cụ.|Sai: kiểm thử là điều kiện hỗ trợ.|Sai: không giải quyết vòng cộng tác.',terms='DevOps')
lesson('15.2','CI/CD và pipeline kiểm tra',(23,29),(211,213),'Thay đổi lớn, dồn lâu mới tích hợp làm lỗi khó tìm và khó khôi phục.',
'Continuous Integration (CI) tích hợp thay đổi thường xuyên kèm build và test tự động. Continuous Delivery giữ thay đổi ở trạng thái có thể triển khai, có thể còn bước quyết định phát hành. Continuous Deployment tự động đưa thay đổi đạt điều kiện lên môi trường đích theo quy trình. Trong tài liệu, CD được dùng chủ yếu theo nghĩa delivery; ứng dụng nêu rõ hai cách dùng để tránh nhầm.',
'Kiểm tra từng lô nhỏ trước khi nhập kho giúp tìm lô lỗi; đưa lô được duyệt ra cửa hàng là bước khác.',
'Ví dụ tự xây dựng: commit → build → unit test → integration test → tạo artifact → thử ở môi trường kiểm tra → phê duyệt phát hành. Đây có thể là CI và delivery dù chưa tự deploy production.',
'CI xanh không chứng minh không có lỗi tích hợp/production. Cùng một artifact đã kiểm tra nên được chuyển qua các môi trường thay vì build lại không kiểm soát.',
'Test nhanh cần cân với độ bao phủ; pipeline cũng có thể hỏng, lộ bí mật hoặc tạo artifact sai.',
'Bước nào phân biệt có thể phát hành với đã phát hành tự động?',
'Pipeline build/test xong nhưng cần người bấm duyệt production. Mô tả nào chính xác?',
'Có thể là continuous delivery; chưa phải tự động continuous deployment tới production|Không thể gọi là CI|Đã chắc chắn tự động deploy production|Không cần artifact đã kiểm tra',
'Đúng: tách sẵn sàng phát hành khỏi tự phát hành.|Sai: CI vẫn có thể tồn tại.|Sai: còn bước duyệt.|Sai: artifact là phần kiểm soát.',terms='CI|CD|continuous deployment')
lesson('15.3','Sandbox, canary và blue-green',(30,38),(212,214),'Thay phiên bản toàn bộ cùng lúc có thể gây ảnh hưởng lớn nếu có lỗi.',
'Sandbox thử ở môi trường tách biệt nhưng có thể khác thực tế. Canary đưa bản mới tới một phần lưu lượng/người dùng rồi quan sát trước khi tăng. Blue-green duy trì hai môi trường và chuyển lưu lượng sang bản mới sau kiểm tra. Cần tiêu chí dừng, quay lại và tương thích dữ liệu khi hai bản cùng tồn tại.',
'Thử món trong bếp thử, bán thử cho ít khách, hoặc chuẩn bị quầy mới rồi chuyển khách sang là ba cách kiểm soát khác nhau.',
'Ví dụ tự xây dựng: canary 5% request có tỷ lệ lỗi 8%, bản cũ 0,2%. Đừng tăng canary chỉ vì CPU thấp; so chỉ số phục vụ và kiểm tra khác biệt nhóm người dùng.',
'Blue-green không tự rollback DB. Canary không phải chia tải cố định mãi giữa hai phiên bản mà không đánh giá.',
'Cần thêm năng lực khi chạy song song và đủ lưu lượng để đo có ý nghĩa. Sandbox không bắt được mọi lỗi thực tế.',
'Nếu thay schema không tương thích bản cũ, kế hoạch quay lại cần chuẩn bị gì?',
'Bản mới được nhận 5% lưu lượng thật để so tỷ lệ lỗi trước khi mở rộng. Đây là gì?',
'Canary deployment|Chỉ unit test|Stop-copy migration|NAS',
'Đúng: thử dần trên phần lưu lượng thực.|Sai: đây đã có traffic triển khai.|Sai: thuộc VM migration.|Sai: giao diện lưu trữ.',terms='canary|blue-green|sandbox')
lesson('15.4','SRE, SLO và ngân sách lỗi',(39,44),None,'Nhóm cần cân bằng độ tin cậy với tốc độ thay đổi và tránh quá tải vận hành thủ công.',
'Site Reliability Engineering (SRE) áp dụng cách tiếp cận kỹ thuật phần mềm vào độ tin cậy và vận hành. Service Level Objective (SLO) đặt mục tiêu đo được; error budget là phần lỗi/không sẵn sàng cho phép trong khoảng đo theo định nghĩa. Slide nêu cách làm của Google như giới hạn thời gian việc vận hành; đây là ví dụ tổ chức, không là tiêu chuẩn bắt buộc mọi công ty.',
'Ngân sách lỗi là giới hạn sai lệch được chấp nhận để quyết định nhịp thay đổi, không phải quyền cố tình làm hỏng dịch vụ.',
'Ví dụ tự xây dựng: giả sử SLO theo thời gian là 99,9% cho 30 ngày. Tổng 43.200 phút, phần không đạt tối đa 0,1% = 43,2 phút theo mô hình đơn giản. SLO theo request cần tính số request lỗi, không đổi thẳng sang phút.',
'Error budget không phải số tiền sửa lỗi. Availability trung bình không mô tả đầy đủ latency, đúng dữ liệu hay mức ảnh hưởng từng người dùng.',
'Mục tiêu càng cao càng tốn kém; chọn metric phản ánh trải nghiệm và có playbook xử lý.',
'Tại sao không thể dùng công thức phút downtime cho mọi loại SLO?',
'SLO thời gian 99,9% trong 30 ngày có error budget đơn giản bao nhiêu phút?',
'43,2 phút|432 phút|4,32 phút|0 phút',
'Đúng: 30×24×60×0,001.|Sai: dùng 1% thay 0,1%.|Sai: nhầm thêm hệ số 10.|Sai: chỉ mục tiêu 100% mới cho 0 theo mô hình.',level='Vận dụng',terms='SRE|SLO|error budget')

chapter('c16','Edge, fog và dữ liệu gần người dùng','16-edge-computing(1).pdf',(219,229),'Vì sao trung tâm dữ liệu lớn vẫn chưa đủ?|Đẩy phần nào ra gần thiết bị?', 'Phân tích đường đi tạo latency|Phân biệt cache, edge và fog|Thiết kế phân chia local/edge/cloud có đánh đổi',['3.3','4.3'], 'Liên quan IoT, bandwidth, quyền riêng tư và kiến trúc phân cấp.')
lesson('16.1','Độ trễ đầu cuối và băng thông',(1,9),(219,221),'Máy xử lý nhanh không loại bỏ thời gian đi qua mạng đến trung tâm dữ liệu xa.',
'Độ trễ đầu cuối gồm truyền lan, truyền dữ liệu, hàng đợi và xử lý qua nhiều chặng. Băng thông giới hạn tốc độ truyền, không đồng nghĩa độ trễ mỗi thông điệp. Đặt nhiều region gần người dùng có thể giảm khoảng cách, nhưng ứng dụng thời gian nhạy vẫn cần xử lý gần hơn và thiết kế lỗi.',
'Đường cao tốc nhiều làn chở được nhiều xe nhưng không khiến một xe đi quãng đường 1.000 km tức thời.',
'Ví dụ tự xây dựng: gửi 20 MB trên đường hiệu dụng 10 MB/s cần tối thiểu khoảng 2 giây chỉ cho phần truyền dữ liệu, chưa tính RTT, xử lý và hàng đợi. Giảm payload có thể hữu ích hơn thêm CPU.',
'Băng thông lớn không bảo đảm RTT nhỏ. Video xem đệm và điều khiển tương tác có mức nhạy trễ khác nhau.',
'Di chuyển compute gần nguồn có thể giảm trễ nhưng giảm kinh tế quy mô và tăng số điểm vận hành.',
'Đâu là phần latency tăng CPU cloud không sửa trực tiếp được?',
'Tăng băng thông nhưng giữ nguyên khoảng cách vật lý có chắc giảm phần trễ truyền lan không?',
'Không; truyền lan và tốc độ truyền dữ liệu là hai thành phần khác nhau|Có; băng thông là tốc độ ánh sáng|Có; mọi RTT trở thành 0|Không vì CPU luôn là nút thắt duy nhất',
'Đúng: băng thông không đổi khoảng cách/tốc độ lan truyền.|Sai: nhầm đại lượng.|Sai: vẫn còn các thành phần trễ.|Sai: có nhiều nút thắt.',terms='latency|bandwidth')
lesson('16.2','Edge, cache trong ISP và fog',(10,16),(221,224),'Cần giảm lưu lượng đường xa và phục vụ một phần công việc gần nguồn dữ liệu.',
'Edge computing đưa tính toán/lưu trữ đến gần nơi phát sinh hoặc sử dụng dữ liệu. Cache trong ISP lưu nội dung thường được yêu cầu để tránh lấy xa; cache là một loại chức năng, không đại diện mọi edge. Fog mô tả phân cấp nhiều tầng trung gian giữa thiết bị và cloud theo phần sách bổ trợ.',
'Kho gần nhà giao nhanh cho mặt hàng sẵn có; với mặt hàng chưa có, vẫn phải lấy từ kho xa.',
'Ví dụ tự xây dựng: camera lọc khung hình tại edge, chỉ gửi sự kiện và đoạn cần phân tích sâu lên cloud. Cần xác định điều gì xảy ra khi mạng mất và khi mô hình lọc bỏ sót sự kiện.',
'Cache hit không bảo đảm dữ liệu mới nhất. Edge không chỉ là một data center nhỏ hơn mà là quyết định đặt chức năng.',
'Giảm truyền xa đổi lấy đồng bộ, cập nhật phần mềm và bảo vệ nhiều điểm hơn.',
'Chọn dữ liệu nào nên cache và cách xử lý khi cache miss.',
'Camera lọc tại chỗ, chỉ gửi sự kiện lên cloud. Lợi ích trực tiếp có thể là gì?',
'Giảm lượng dữ liệu phải truyền xa nếu bộ lọc phù hợp|Loại bỏ mọi rủi ro bỏ sót|Không cần bảo trì thiết bị edge|Mọi bản sao dữ liệu luôn mới tức thời',
'Đúng: giảm dữ liệu gửi là mục tiêu có điều kiện.|Sai: bộ lọc có thể sai.|Sai: edge vẫn cần vận hành.|Sai: đồng bộ vẫn cần cơ chế.',level='Vận dụng',terms='edge computing|fog computing|cache')
lesson('16.3','Tập trung, phân tán và IIoT',(17,25),(224,229),'Không nên đưa toàn bộ xử lý ra edge chỉ vì một bước cần phản hồi nhanh.',
'Tập trung đem lại chia sẻ tài nguyên và chuyên môn; phân tán gần nguồn giảm latency và truyền xa. Industrial Internet of Things (IIoT) trong sách liên quan thiết bị, cảm biến và quy trình công nghiệp. Kiến trúc có thể giữ phản ứng cục bộ ở thiết bị, tổng hợp ở edge và phân tích dài hạn tại cloud. Các ví dụ điều khiển quan trọng cần đánh giá yêu cầu hệ thống cụ thể, không dùng sơ đồ học làm thiết kế triển khai thực tế.',
'Quyết định cần ngay được đưa ra tại chỗ; báo cáo tổng hợp có thể gửi trung tâm sau.',
'Ví dụ tự xây dựng: cảm biến gửi dữ liệu đến gateway; gateway đệm khi mất mạng và tải lên khi nối lại. Cần ID, timestamp và quy tắc chống trùng khi gửi lại.',
'Phân tán không tự tăng độ tin cậy nếu các điểm đều cần cùng một cloud để ra quyết định. Cần xét đường phụ thuộc thực tế.',
'Bớt phụ thuộc WAN nhưng thêm thiết bị cần cập nhật và theo dõi; phân chia theo độ trễ, dữ liệu và năng lực vận hành.',
'Phần nào của một pipeline IoT cần tiếp tục hoạt động khi WAN mất?',
'Để xử lý mất WAN, gateway nên có thiết kế nào trong ví dụ lưu rồi gửi?',
'Đệm bền vững và quy tắc gửi lại/chống trùng|Chỉ bỏ mọi dữ liệu không thông báo|Giả định WAN không bao giờ mất|Dùng biến RAM rồi cam kết không mất dữ liệu qua reboot',
'Đúng: hỗ trợ lỗi kết nối và replay.|Không đáp ứng yêu cầu giữ dữ liệu.|Sai: bỏ qua một chế độ lỗi.|Sai: RAM không bền qua reboot.',level='Vận dụng',terms='IIoT')

chapter('c17','Bảo mật và quyền riêng tư trên cloud','17-security-privacy(1).pdf',(233,243),'Vì sao chỉ bảo vệ biên mạng chưa đủ?|Danh tính, mã hóa và VPN bảo vệ phần nào?', 'Phân biệt xác thực với phân quyền|Theo vết điểm kết thúc mã hóa|Giải thích giới hạn VPN và trách nhiệm phối hợp',['7.1','12.5'], 'Gắn với mọi lớp: workload, danh tính, dữ liệu và các công cụ điều khiển.')
lesson('17.1','Từ biên mạng truyền thống đến cloud',(1,13),(233,237),'Mô hình “bên trong đáng tin” suy yếu khi người dùng, dịch vụ và hạ tầng đều truy cập từ xa.',
'Firewall, vùng DMZ (Demilitarized Zone) và hệ thống phát hiện xâm nhập hỗ trợ phân vùng truyền thống. Cloud có ranh giới logic, hạ tầng nhiều tenant, workload động và khả năng quan sát vật lý hạn chế. Cần phối hợp với nhà cung cấp và quản lý quyền ở mức tài nguyên/dịch vụ, không chỉ địa chỉ nằm trong mạng nào.',
'Qua được cổng tòa nhà không nên được cầm mọi chìa khóa phòng.',
'Ví dụ tự xây dựng: một Pod bị chiếm quyền trong mạng nội bộ. Nếu mọi dịch vụ tin mọi IP nội bộ, kẻ tấn công có thể di chuyển ngang. Phân quyền từng dịch vụ và giới hạn quyền workload giảm phạm vi ảnh hưởng.',
'Private IP không là bằng chứng người gọi đáng tin. Cloud provider bảo vệ hạ tầng không thay kiểm soát quyền dữ liệu của tenant.',
'Tăng chi tiết chính sách làm quản lý phức tạp; cần kiểm tra và quan sát để tránh cấp quá rộng hoặc chặn nhầm.',
'Vì sao firewall biên không chặn được mọi cuộc gọi độc hại giữa microservices?',
'Pod nội bộ bị chiếm quyền. Giả định nào nguy hiểm nhất?',
'Mọi người gọi từ IP nội bộ đều được tin và cấp toàn quyền|Mỗi dịch vụ cần kiểm tra quyền phù hợp|Cần giới hạn phạm vi truy cập của workload|Cần quan sát giao tiếp nội bộ',
'Đúng: bỏ kiểm tra danh tính/quyền tạo di chuyển ngang.|Đây là kiểm soát hữu ích.|Đây là hạn chế ảnh hưởng.|Đây là đầu vào phát hiện.',terms='DMZ|attack surface')
lesson('17.2','Truy cập từ xa và điểm kết thúc mã hóa',(14,25),(240,243),'Dữ liệu có thể bị đọc ở đường truyền hoặc ở endpoint; cần xác định bảo vệ đến đâu.',
'Mã hóa khi truyền bảo vệ một đoạn kết nối giữa các điểm kết thúc. Nếu proxy kết thúc TLS rồi gửi plaintext tới backend, đoạn sau proxy không được bảo vệ bởi phiên TLS đầu tiên. Mã hóa đầu cuối cần định nghĩa rõ ai là hai đầu cuối và ai giữ khóa. Mã hóa thiết bị giảm rủi ro khi mất thiết bị nhưng không thay kiểm soát phiên đang mở.',
'Niêm phong thư đến bưu cục rồi mở và gửi trần tiếp khác với giữ niêm phong đến người nhận cuối cùng.',
'Ví dụ tự xây dựng: browser → TLS → load balancer → HTTP → API. Đường Internet được mã hóa, nhưng không thể nói toàn đường browser–API là một phiên mã hóa đầu cuối. Có thể bảo vệ thêm chặng nội bộ theo kiến trúc.',
'HTTPS không chứng minh dữ liệu đã mã hóa khi lưu. Mã hóa không tự ngăn người có quyền khóa đọc dữ liệu.',
'Cần quản lý khóa, xác thực peer và chọn ranh giới tin cậy; tăng mã hóa mà bỏ quyền truy cập vẫn để dữ liệu bị lạm dụng.',
'Vẽ đường đi request và đánh dấu nơi giải mã, ai đọc được plaintext ở mỗi đoạn.',
'TLS dừng ở proxy rồi proxy gửi HTTP đến backend. Phát biểu nào đúng?',
'Đoạn proxy–backend không được phiên TLS phía client bảo vệ|Mọi đoạn đều tự mã hóa vì URL đầu là HTTPS|Dữ liệu lưu trên đĩa tự mã hóa theo|Proxy không thể thấy plaintext dù nó kết thúc TLS',
'Đúng: cần xét từng đoạn và endpoint.|Sai: TLS không tự kéo dài qua phiên khác.|Sai: mã hóa lưu trữ là cơ chế riêng.|Sai: điểm kết thúc thường giải mã để xử lý.',level='Vận dụng',terms='encryption|TLS|end-to-end encryption')
lesson('17.3','Danh tính, zero trust và SSO',(26,36),(237,239),'Người dùng muốn đăng nhập ít lần nhưng dịch vụ vẫn phải kiểm tra quyền đúng mức.',
'Xác thực (authentication) kiểm tra danh tính; phân quyền (authorization) quyết định hành động được phép. Single Sign-On (SSO) tập trung/quy phối đăng nhập để dùng nhiều dịch vụ mà không nhập mật khẩu riêng mỗi nơi. Zero trust tránh tin mặc định theo vị trí mạng; cần xác minh danh tính, quyền và ngữ cảnh phù hợp. Có token hợp lệ chưa đủ để làm mọi thao tác.',
'Thẻ căn cước trả lời bạn là ai; danh sách quyền phòng trả lời bạn được vào đâu. Một lần đăng nhập không có nghĩa tất cả cửa đều mở.',
'Ví dụ tự xây dựng: sinh viên đăng nhập qua SSO, đọc được điểm của mình nhưng không được sửa điểm. API phải xác minh token và quyền đối với tài nguyên cụ thể, không chỉ thấy có token là cho qua.',
'SSO không tự là MFA. Zero trust không phải chỉ cài thêm một firewall hay mặc định từ chối mọi công việc mãi mãi.',
'Tập trung danh tính giúp quản lý nhưng cần bảo vệ dịch vụ định danh, quy trình thu hồi và quyền tối thiểu.',
'Khi người dùng rời nhóm, phiên/token còn sống cần được quản lý thế nào?',
'Đã xác thực sinh viên nhưng API vẫn từ chối sửa điểm. Điều này cho thấy gì?',
'Xác thực và phân quyền là hai bước khác nhau|SSO chắc chắn hỏng|Có tài khoản nghĩa có quyền quản trị|Zero trust không cho bất kỳ ai dùng ứng dụng',
'Đúng: biết danh tính chưa đủ có quyền.|Sai: có thể là hành vi đúng.|Sai: quyền phải được cấp riêng.|Sai: mục tiêu là cấp đúng quyền sau xác minh.',terms='authentication|authorization|SSO|zero trust|IAM')
lesson('17.4','VPN và SSH tunnel',(37,47),(240,242),'Ứng dụng cũ không bảo vệ truyền thông cần một kênh truy cập được kiểm soát.',
'Virtual Private Network (VPN) thiết lập kết nối mạng logic qua đường truyền trung gian và thường bảo vệ tunnel bằng mật mã theo giao thức. VPN gateway là điểm kết thúc; bảo vệ tunnel không tự kéo tới mọi ứng dụng phía sau gateway. SSH port forwarding ánh xạ các cặp địa chỉ:cổng qua phiên SSH, hẹp hơn mô hình một mạng VPN tổng quát trong ví dụ slide.',
'Đường hầm an toàn tới cổng khu nhà chưa quyết định ai được mở từng phòng sau cổng.',
'Ví dụ tự xây dựng: người dùng qua VPN tới gateway rồi truy cập một ứng dụng HTTP nội bộ. Kiểm tra đoạn gateway–ứng dụng và quyền ứng dụng; không coi VPN thay được cả hai.',
'VPN không bảo vệ endpoint đã bị chiếm quyền và không thay xác thực ứng dụng. SSH tunnel không mặc định nối toàn bộ mạng như mọi VPN.',
'Tunnel tạo thêm điểm điều khiển và quản lý khóa/quyền; phải giới hạn đường và tài nguyên được truy cập.',
'Nêu ba thứ VPN không tự giải quyết: endpoint, quyền ứng dụng và bảo vệ đoạn sau gateway.',
'VPN kết thúc ở gateway. Điều gì vẫn cần đánh giá?',
'Bảo vệ đoạn sau gateway và quyền truy cập ứng dụng|Không cần xác thực ứng dụng nữa|Mọi endpoint chắc chắn sạch mã độc|Mọi file trên đĩa đã được mã hóa',
'Đúng: tunnel chỉ bảo vệ phạm vi của nó.|Sai: lớp ứng dụng vẫn cần.|Sai: không kiểm chứng endpoint.|Sai: không suy ra mã hóa lưu trữ.',terms='VPN|SSH tunnel')

chapter('c18','Kiểm soát độ phức tạp','18-handling-complexity(1).pdf',(247,263),'Vì sao test nhiều vẫn có thể bỏ sót lỗi phân tán?|Mô hình giúp suy luận điều gì?', 'Phát hiện chu trình phụ thuộc có nguy cơ deadlock|Phân biệt safety và liveness|Kết hợp prototype, mô hình và test thay vì coi một cách là đủ',['12.2','13.2'], 'Chương slide ngắn được giải thích bằng các mô hình và ví dụ bổ trợ trong sách.')
lesson('18.1','Độ phức tạp công cụ và tương tác',(1,3),(247,249),'Hệ thống có nhiều lớp và nhiều thứ tự sự kiện hơn khả năng kiểm tra thủ công.',
'Có độ phức tạp do công cụ/framework, lớp ảo hóa và thay đổi liên tục; còn độ phức tạp nội tại do đồng thời, dữ liệu nhân bản, độ trễ và tương tác. Một lỗi chỉ xuất hiện ở thứ tự hiếm có thể khó tái hiện. Thêm công cụ quan sát giúp chẩn đoán nhưng cũng tạo thành phần phải quản lý.',
'Không chỉ có nhiều mảnh ghép; thứ tự các mảnh được chạm tới cũng thay đổi kết quả.',
'Ví dụ tự xây dựng: A cập nhật dữ liệu, B đọc bản sao chậm hơn rồi gửi quyết định trở lại A. Cả A/B đều vượt unit test riêng nhưng chuỗi thời gian tạo quyết định trên dữ liệu cũ.',
'Nhiều unit test không tương đương đã thử mọi lịch thực thi phân tán. Giảm số công cụ không loại bỏ đồng thời và lỗi mạng.',
'Cần chọn ranh giới đơn giản, log tương quan và mô hình giả định rõ; không thể chỉ tăng số máy để sửa độ phức tạp.',
'Tại sao hai dịch vụ đều đúng cục bộ vẫn có thể sai khi kết hợp?',
'Loại lỗi nào unit test từng dịch vụ có thể bỏ sót?',
'Lỗi do thứ tự tương tác và độ trễ giữa các dịch vụ|Mọi lỗi cú pháp trong hàm đã thực thi|Mọi trường hợp dữ liệu đã được test đầy đủ|Chỉ lỗi phông chữ',
'Đúng: hành vi toàn hệ vượt từng thành phần.|Không phải điểm phân tán cần nhấn mạnh.|Sai: không thể suy test đầy đủ mọi trường hợp.|Sai: quá hẹp và không đúng trọng tâm.',terms='distributed complexity')
lesson('18.2','Prototype, kiểm thử và mô hình',(4,4),(249,251),'Cần giảm bất ngờ trước khi xây và vận hành toàn hệ thống.',
'Prototype kiểm tra khả năng kết hợp công nghệ và giả định kiến trúc. Kiểm thử thực thi các trường hợp cụ thể. Mô hình mô tả phần được chọn của hệ thống để suy luận về tính chất, có thể là graph, mô phỏng hoặc đặc tả toán học. Một mô hình chỉ có giá trị trong các giả định và mức trừu tượng đã nêu.',
'Maquette giúp kiểm tra bố trí; tính toán chịu lực giúp kiểm tra một tính chất khác. Không cái nào một mình mô tả mọi điều ở tòa nhà thật.',
'Ví dụ tự xây dựng: mô hình hàng đợi dự đoán tải cao; prototype đo thời gian khởi tạo; test tích hợp thử lỗi mạng. Ghép ba loại bằng chứng giúp thấy cả giới hạn mô hình và hành vi triển khai.',
'Mô hình không phải bản sao đầy đủ hệ thống. Model checking một đặc tả không chứng minh mã sản phẩm đúng nếu ánh xạ đặc tả–mã chưa được kiểm chứng.',
'Trừu tượng bớt chi tiết giúp suy luận nhưng có thể bỏ sót tác động; phải ghi rõ thứ gì nằm ngoài mô hình.',
'Chọn một giả định của mô hình cần đo trên prototype trước khi tin kết quả.',
'Kết luận nào hợp lý khi một mô hình đã được kiểm tra?',
'Tính chất đã kiểm tra đúng trong phạm vi mô hình và giả định tương ứng|Mọi dòng mã sản phẩm chắc chắn không lỗi|Không cần test tích hợp nữa|Mọi môi trường triển khai đều giống mô hình',
'Đúng: giới hạn bằng chứng cần rõ.|Sai: còn khoảng cách đặc tả–triển khai.|Sai: hai cách bổ sung nhau.|Sai: giả định có thể không giữ.',terms='model|prototype')
lesson('18.3','Đồ thị phụ thuộc, safety, liveness và TLA+',(4,4),(251,263),'Cần nói chính xác “không xảy ra điều xấu” và “cuối cùng có tiến triển”.',
'Đồ thị có hướng biểu diễn quan hệ gọi hoặc chờ; chu trình là dấu hiệu cần phân tích, không tự chứng minh deadlock với mọi ngữ nghĩa. Safety diễn đạt điều không được xảy ra, như không có hai bên cùng sở hữu khóa độc quyền. Liveness diễn đạt tiến triển dưới giả định, như yêu cầu hợp lệ cuối cùng được trả lời. TLA+ trong sách dùng trạng thái ban đầu và quan hệ chuyển trạng thái để mô tả hành vi theo thời gian; đây là nội dung bổ trợ, không yêu cầu cài công cụ để học app.',
'An toàn: không có hai người giữ chìa khóa độc quyền cùng lúc. Tiến triển: người đang chờ rồi cũng có cơ hội nhận chìa khóa với điều kiện công bằng phù hợp.',
'Ví dụ tự xây dựng: A đợi B sẵn sàng, B đợi C, C đợi A; nếu tất cả chỉ khởi động sau điều kiện chờ đó thì không ai bắt đầu. Tách một bước khởi tạo hoặc đổi giao thức có thể phá chu trình. Với model khóa: trạng thái gồm owner và waiting; chuyển acquire/release phải giữ tối đa một owner.',
'Không deadlock chưa bảo đảm mọi yêu cầu được phục vụ: starvation vẫn có thể xảy ra. Một chu trình gọi không chặn không đồng nghĩa deadlock bắt buộc.',
'Đặc tả tốt cần nêu lỗi, lịch thực thi và fairness; bỏ giả định có thể làm mệnh đề liveness không còn đúng.',
'Nêu một safety và một liveness cho hàng đợi xử lý job, kèm giả định.',
'“Mỗi job hợp lệ cuối cùng được xử lý nếu worker tiếp tục hoạt động và được lập lịch công bằng” là loại tính chất nào?',
'Liveness có điều kiện|Chỉ là giới hạn dung lượng đĩa|Safety vì chỉ cấm một trạng thái|Một bằng chứng mọi code không lỗi',
'Đúng: nói về tiến triển theo thời gian cùng giả định.|Sai: không nói dung lượng.|Sai: safety cấm điều xấu, không yêu cầu “cuối cùng”.|Sai: không phải bằng chứng toàn bộ code.',terms='deadlock|safety|liveness|TLA+')

chapter('f1','Nền tảng bổ trợ: song song và giới hạn','slideset_01(2).pdf',None,'Chia công việc song song có giới hạn gì?|Client chịu trách nhiệm phần nào?', 'Tính speedup theo Amdahl và giải thích giả định|Phân biệt shared/distributed memory|Ước lượng điện năng theo công suất và thời gian',[], 'Mô-đun bổ trợ kết nối chương 1, 4 và 11; giữ nguồn khác biệt với trục 18 chương.')
lesson('F1.1','Thông tin khóa học, thế hệ máy tính và quyền kiểm soát',(1,19),None,'Tài liệu đặt cloud trong lịch sử hệ phân tán và đặt câu hỏi ai kiểm soát ứng dụng/dữ liệu.',
'Slide 1–6 là thông tin tổ chức và thử thách triển khai cloud đa node của khóa cũ. Slide 7–8 nêu các thế hệ công nghệ và chuyển sang mạng, đa lõi, ảo hóa. Slide 9–19 dùng các ví dụ nền tảng và nội dung số theo bối cảnh lịch sử để bàn về quyền tự chủ, khả năng thu hồi và phụ thuộc nhà cung cấp. Các ảnh báo cũ không được dùng để khẳng định chính sách sản phẩm hiện tại.',
'Sự thuận tiện của dịch vụ cần được xem cùng khả năng lấy dữ liệu ra và tiếp tục công việc khi quyền truy cập thay đổi.',
'Ví dụ tự xây dựng: trước khi chọn công cụ học online, thử xuất ghi chú sang định dạng mở và mở bản xuất khi mất mạng. Đó là kiểm tra cụ thể thay cho chỉ tin có nút “export”.',
'Phân loại thế hệ là mô hình lịch sử, không phải mọi máy trong một năm đều có cùng cấu trúc. Các phát biểu về iPhone/Kindle trong slide không phải hướng dẫn hiện hành.',
'Bài học tập trung quyền kiểm soát và khả năng di chuyển, không dự đoán chính sách hay luật hiện nay.',
'Nêu hai phép thử kiểm chứng quyền kiểm soát dữ liệu của bạn.',
'Cách dùng phù hợp các ảnh tin tức cũ trong bộ slide là gì?',
'Xem như ví dụ lịch sử về quyền kiểm soát, cần kiểm chứng riêng nếu hỏi hiện trạng|Coi mọi chính sách vẫn đúng hiện nay|Bỏ qua hoàn toàn vấn đề xuất dữ liệu|Suy ra mọi cloud đều cấm phần mềm tự do',
'Đúng: không chuyển ví dụ theo thời điểm thành hiện trạng.|Sai: có thể đã thay đổi.|Sai: đó là vấn đề quan trọng.|Sai: khái quát vượt nguồn.',terms='digital autonomy')
lesson('F1.2','Client-server và bốn kiểu client',(20,30),None,'Cùng ứng dụng nhưng xử lý, quản lý và lưu dữ liệu có thể được chia giữa client/server khác nhau.',
'Bộ slide tách năm nhiệm vụ: hiển thị UI, tính UI, xử lý dữ liệu, quản lý dữ liệu và lưu dữ liệu. Terminal chủ yếu hiển thị và gửi tương tác; thin client có thêm xử lý giao diện; applet/network client và fat client đẩy nhiều xử lý hơn về phía client theo phân loại của slide. Thực tế có nhiều kiến trúc lai, nên dùng bảng nhiệm vụ để phân tích thay vì chỉ nhìn loại thiết bị.',
'Chiếc màn hình trước mặt không cho biết toàn bộ công việc đang chạy ở đâu.',
'Ví dụ tự xây dựng: remote desktop truyền hình và thao tác khác web app có mã JavaScript tính toán tại trình duyệt. Hãy đánh dấu năm nhiệm vụ chạy tại phía nào, kể cả trường hợp lưu cache local.',
'Thin client không có nghĩa không có CPU; server không nhất thiết chứa mọi dữ liệu và logic trong mọi kiến trúc.',
'Đẩy xử lý về server tập trung quản lý nhưng tăng phụ thuộc mạng và năng lực server; client mạnh có thể làm offline tốt hơn nếu thiết kế hỗ trợ.',
'Ứng dụng web local đang học chạy chấm trắc nghiệm ở phía nào?',
'Phân tích kiểu client đáng tin cậy nhất dựa trên gì?',
'Phân bố nhiệm vụ UI, xử lý, quản lý và lưu dữ liệu|Chỉ màu thiết bị|Chỉ máy có màn hình lớn|Chỉ tên thương hiệu OS',
'Đúng: chức năng quyết định kiến trúc.|Không liên quan.|Không quyết định nơi xử lý.|Không quyết định phân bố nhiệm vụ.',terms='thin client|fat client')
lesson('F1.3','Điện năng và đơn vị dữ liệu',(31,39),None,'So sánh thiết bị cần tính cả thời gian sử dụng và phần server phục vụ phía sau.',
'Điện năng E = P × t; kW là công suất, kWh là năng lượng. Với thin client phải cộng màn hình và server cần thiết. Số server lấy tròn lên theo số client trên một server. Moore là quy luật quan sát lịch sử, không là định luật tự nhiên bảo đảm hiệu năng tăng mãi. Von Neumann bottleneck nhấn mạnh đường CPU–bộ nhớ có thể giới hạn hiệu năng.',
'Thiết bị ít điện ở bàn chưa chắc toàn hệ ít điện nếu quên máy chủ phía sau.',
'Ví dụ tự xây dựng: 500 thin client, mỗi cái 30 W, màn hình 80 W; một server 600 W cho 30 client. Cần ceil(500/30)=17 server. Công suất tổng 500×110 + 17×600 = 65.200 W. Chạy 24×365,25 giờ cho 571.543,2 kWh theo giả định, chưa tính làm mát và tổn hao.',
'Phép tính điện trong slide dùng mô hình đơn giản; phải ghi rõ công suất đo hay định mức và lịch chạy. Tăng số transistor không đồng nghĩa tăng tương ứng tốc độ ứng dụng.',
'Đánh giá tổng hệ thống và workload, không suy từ một linh kiện.',
'Nếu tắt thiết bị 12 giờ mỗi ngày, biến nào trong công thức thay đổi?',
'500 client, một server cho tối đa 30 client. Cần tối thiểu bao nhiêu server?',
'17|16|16,67 máy vật lý|30',
'Đúng: làm tròn lên.|Sai: 16 chỉ phục vụ 480.|Sai: không cấp một phần server theo giả định.|Sai: nhầm năng lực mỗi server với số server.',level='Vận dụng',terms='kWh|Moore law|Von Neumann bottleneck')
lesson('F1.4','Amdahl, granularity và overhead',(40,45),None,'Phần tuần tự khiến thêm CPU có lợi ích giảm dần.',
'Với khối lượng công việc cố định, phần song song p và N bộ xử lý lý tưởng, speedup S = 1/((1−p)+p/N). Khi N tăng vô hạn, trần lý tưởng 1/(1−p). Thêm overhead o(N) ở mẫu số có thể làm hiệu năng đạt đỉnh rồi giảm. Granularity là mức công việc trong mỗi tác vụ; quá mịn khiến giao tiếp/lập lịch chi phối.',
'Nhiều thợ không rút ngắn thời gian một bước bắt buộc làm lần lượt; quá nhiều thợ trong phòng nhỏ còn vướng nhau.',
'Ví dụ tự xây dựng: p=0,9, N=10 cho S=1/(0,1+0,09)=5,263. Trần lý tưởng là 10, không phải tốc độ luôn tăng đúng N lần. Nếu thêm overhead 0,05 thời gian chuẩn hóa, S chỉ còn 4,167.',
'Giữ kích thước bài toán cố định khác tăng kích thước theo số CPU. Trần lý tưởng không dự đoán chính xác mọi cache và hệ thống thực tế.',
'Chọn độ hạt đủ lớn để amortize overhead nhưng không quá lớn gây mất cân tải.',
'Vì sao p=0,5 không thể đạt speedup lý tưởng 4 dù có 100 CPU?',
'Với p=0,9, trần Amdahl khi N tiến tới vô hạn là bao nhiêu?',
'10|90|Vô hạn|0,9',
'Đúng: 1/(1−0,9).|Sai: lấy phần trăm làm speedup.|Sai: còn phần tuần tự.|Sai: đó là tỷ lệ song song.',level='Vận dụng',terms='Amdahl law|speedup|granularity')
lesson('F1.5','Gustafson, Monte Carlo và cách đọc kết quả',(46,56),None,'Hệ nhiều CPU còn có thể giải bài toán lớn hơn trong thời gian tương tự, không chỉ rút thời gian bài toán cũ.',
'Gustafson xét bài toán có thể tăng quy mô theo tài nguyên. Với thời gian trên N bộ xử lý chuẩn hóa, phần tuần tự s và song song 1−s, scaled speedup = N−s(N−1). Định nghĩa phần tỷ lệ phải gắn với mô hình thời gian, không lấy p của hai mô hình thay tùy tiện. Monte Carlo có nhiều mẫu độc lập nhưng gom kết quả và tạo mẫu vẫn có chi phí.',
'Amdahl hỏi nấu cùng bữa ăn nhanh hơn thế nào; Gustafson hỏi cùng thời gian, nhiều người nấu được bữa lớn hơn thế nào.',
'Ví dụ tự xây dựng: N=8, s=0,1 theo mô hình scaled cho S=8−0,7=7,3. Với Monte Carlo ước lượng π, tạo điểm đều trong hình vuông rồi ước π=4×tỷ lệ trong hình tròn; tăng mẫu chủ yếu tăng độ chính xác thống kê, không bảo đảm mỗi lần đều gần π hơn.',
'Hai định luật trả lời câu hỏi và chuẩn hóa khác nhau, không phải mâu thuẫn. Đồ thị benchmark Raspberry Pi trong slide là đo cụ thể, không hứa hẹn cho máy Windows của bạn.',
'Cần ghi số mẫu, seed, số core, thời gian toàn phần và sai số; cache và mạng ảnh hưởng kết quả.',
'Khi tăng CPU nhưng giữ thời gian, bạn đã đổi biến nào nếu tăng số mẫu?',
'Gustafson chủ yếu đổi góc nhìn nào so với Amdahl cố định workload?',
'Cho phép tăng kích thước công việc khi tăng tài nguyên|Giả định không có phần tuần tự trong mọi chương trình|Cấm chạy trên nhiều CPU|Đo dung lượng đĩa thay thời gian',
'Đúng: scaled workload là mấu chốt.|Sai: vẫn có s.|Sai: đang phân tích song song.|Sai: vẫn phân tích tăng tốc.',terms='Gustafson law|Monte Carlo')
lesson('F1.6','Dung lượng, shared memory, SMP và distributed memory',(57,69),None,'Chương trình song song phải biết dữ liệu có được truy cập qua địa chỉ chung hay gửi qua mạng.',
'Shared memory cho các bộ xử lý truy cập không gian địa chỉ chung; cần đồng bộ và nhất quán cache. Symmetric Multiprocessing (SMP) theo mô hình slide dùng các CPU có vai trò tương đương; asymmetric multiprocessing phân vai khác nhau. Distributed memory có bộ nhớ cục bộ riêng ở mỗi node, giao tiếp qua mạng. Slide 57 liệt kê cả bội thập phân và nhị phân; ứng dụng dùng GB=10⁹, GiB=2³⁰ để tránh nhập nhằng.',
'Cùng một bảng ghi cần quy tắc ai được sửa; mỗi người có sổ riêng cần quy tắc gửi thông tin. Cả hai đều có chi phí phối hợp.',
'Ví dụ tự xây dựng: 4 thread cùng tăng biến đếm shared cần atomic/khóa hoặc cách chia rồi cộng. Với 4 process ở 4 node, mỗi node đếm cục bộ rồi truyền tổng về; địa chỉ biến ở node A không dùng như con trỏ RAM ở node B.',
'Shared memory không có nghĩa truy cập luôn nhanh bằng nhau ở mọi hệ thực tế. SMP trong slide là mô hình đơn giản; không dùng nó để phủ nhận NUMA.',
'Chọn mô hình lập trình theo locality và đồng bộ. Khả năng phần cứng không tự làm chương trình thread-safe.',
'Nêu một lỗi race của shared memory và một chi phí của distributed memory.',
'4 node có RAM riêng. Cách tổng hợp đếm hợp lý là gì?',
'Đếm cục bộ rồi trao đổi/cộng kết quả qua cơ chế truyền thông|Đọc con trỏ cục bộ của node khác như cùng RAM|Không cần truyền thông vì cùng cluster|Chỉ đổi GB thành GiB',
'Đúng: thể hiện bộ nhớ phân tán.|Sai: không gian địa chỉ khác.|Sai: cluster vẫn cần mạng.|Sai: đơn vị không tổng hợp dữ liệu.',terms='shared memory|distributed memory|SMP|GiB')

chapter('f2','Nền tảng bổ trợ: cluster, HA và MPI','slideset_02(2).pdf',None,'Cluster tối ưu sẵn sàng hay thông lượng?|MPI phối hợp process như thế nào?', 'Phân biệt HA, HPC và HTC|Tính availability theo MTBF/MTTR với giả định|Đọc mẫu MPI theo rank, communicator và collective',['F1.4','F1.6'], 'Bổ trợ cho hạ tầng, MapReduce và vận hành có chịu lỗi.')
lesson('F2.1','Lịch sử, cấu trúc và vị trí cluster',(1,11),None,'Gộp máy độc lập cần chọn tính đồng nhất và cách bố trí.',
'Slide đi từ VAXcluster đến tận dụng workstation nhàn rỗi. Cluster gồm từ hai node độc lập giao tiếp qua mạng. Homogeneous dùng cấu hình tương đối đồng nhất; heterogeneous có khác biệt. Glass-house tập trung trong phòng/rack, campus-wide phân bố trong khuôn viên; vị trí tác động bảo trì, mạng và miền lỗi.',
'Tập trung dễ tiếp cận và nối mạng nhanh; phân tán địa điểm có thể giảm một số lỗi chung nhưng tăng khó vận hành.',
'Ví dụ tự xây dựng: tận dụng máy phòng lab ngoài giờ (COW/NOW) cần tính khi người dùng trở lại và máy rời pool. Cluster chuyên dụng có lịch tài nguyên ổn định hơn.',
'Cluster không bắt buộc mọi node cùng mạnh, nhưng khác năng lực làm cân tải khó hơn. “Chưa thấy” trong lời giảng không phải bằng chứng không thể tồn tại.',
'Đồng nhất đơn giản hóa cấu hình; không đồng nhất tận dụng tài nguyên nhưng cần lập lịch theo khả năng.',
'Bạn cần thay đổi giả định gì khi node chỉ rảnh ban đêm?',
'Nhược điểm quan trọng khi dùng workstation nhàn rỗi làm cluster là gì?',
'Tài nguyên có thể bị thu hồi khi người dùng quay lại|Không có CPU trên workstation|Mạng không bao giờ cần thiết|Mọi node bắt buộc giống hệt nhau',
'Đúng: tính sẵn có thay đổi.|Sai: có CPU thật.|Sai: các node cần giao tiếp.|Sai: có thể heterogeneous.',terms='COW|NOW|heterogeneous cluster')
lesson('F2.2','HA, availability, active/passive và split brain',(12,18),None,'Chịu lỗi cần tránh hệ thống vừa mất dịch vụ vừa gây ghi xung đột khi hiểu sai node đã hỏng.',
'High Availability (HA) ưu tiên khả năng phục vụ. Công thức mô hình steady-state đơn giản A = MTBF/(MTBF+MTTR), với cách hiểu MTBF là thời gian hoạt động trung bình như slide. Active/passive dùng node dự phòng tiếp nhận khi lỗi; active/active có nhiều node phục vụ. Heartbeat mất có thể do đường mạng chứ không phải node chết, gây split brain nếu hai bên cùng tự nhận quyền ghi. Fencing/quorum là diễn giải bổ sung về kiểm soát quyền hoạt động.',
'Không nghe người kia trả lời không chứng minh họ đã rời phòng; có thể điện thoại hỏng. Hai người cùng nhận quyền điều khiển độc quyền có thể làm sai dữ liệu.',
'Ví dụ tự xây dựng: MTBF=990 giờ, MTTR=10 giờ, A=0,99. Nếu MTTR giảm còn 1 giờ, A≈99,899%. Đây là mô hình trung bình, không hứa uptime của từng tuần.',
'HA không chỉ là số máy. Load balancer hoặc storage chung có thể vẫn là single point of failure.',
'Dự phòng cần kiểm thử chuyển vai và chống hai chủ; giảm downtime phải cân bằng tính đúng dữ liệu.',
'Vì sao failover chỉ dựa timeout mạng có nguy cơ ghi đồng thời?',
'MTBF=990 giờ, MTTR=10 giờ. Availability theo công thức bài học là bao nhiêu?',
'99%|90%|100%|10%',
'Đúng: 990/(990+10).|Sai: tính sai tỷ lệ.|Sai: vẫn có downtime.|Sai: nhầm MTTR thành tỷ lệ hoạt động.',level='Vận dụng',terms='HA|MTBF|MTTR|split brain|failover')
lesson('F2.3','Shared nothing, shared disk và DRBD',(19,24),None,'Các node cần cùng dữ liệu hoặc bản sao nhất quán để tiếp nhận dịch vụ khi lỗi.',
'Shared nothing trong mô hình HA dùng lưu trữ riêng và cơ chế truyền/nhân bản; shared disk dùng nơi lưu trữ chung với phối hợp truy cập. Distributed Replicated Block Device (DRBD) nhân bản ở lớp block; ví dụ slide primary gửi ghi sang secondary rồi xác nhận theo cấu hình đang minh họa. Phương thức acknowledgment cụ thể tùy cấu hình, không kết luận mọi DRBD luôn giống ví dụ.',
'Có hai tủ hồ sơ phải chép cập nhật khác với hai người dùng cùng một tủ; cả hai đều cần quy tắc ai được ghi.',
'Ví dụ tự xây dựng: primary hỏng sau khi trả thành công nhưng dữ liệu chưa tới replica trong chế độ không đồng bộ. Replica có thể thiếu cập nhật; cần chọn cam kết nhất quán và cơ chế failover phù hợp.',
'Nhân bản block không tự cung cấp hệ thống file cho nhiều writer. Shared disk vẫn có thể là điểm lỗi chung nếu không dự phòng.',
'Đồng bộ tăng đường chờ ghi; không đồng bộ có cửa sổ mất cập nhật. Cần xác định mục tiêu mất dữ liệu và khôi phục.',
'Vì sao nhân bản hoàn hảo vẫn không thay lịch sử backup khi người dùng xóa nhầm?',
'DRBD trong phạm vi bài nhân bản ở lớp nào?',
'Block device|HTML UI|Danh mục DNS công khai|VNI của VXLAN',
'Đúng: nhân bản block giữa thiết bị.|Sai: không phải giao diện web.|Sai: khác chức năng.|Sai: thuộc mạng ảo.',terms='DRBD|shared nothing|shared disk')
lesson('F2.4','HPC, HTC, Beowulf và chi phí quản lý',(25,38),None,'Hai cluster có cùng số máy có thể được thiết kế cho mục tiêu khác nhau.',
'High Performance Computing (HPC) ưu tiên thời gian giải bài toán tính toán lớn, thường có phối hợp chặt. High Throughput Computing (HTC) ưu tiên lượng công việc hoàn thành trong thời gian dài, thường có nhiều job độc lập. Beowulf được tài liệu dùng cho cluster tính toán chuyên dụng với phần cứng phổ thông và phần mềm tự do. Các ảnh cluster cũ minh họa tổ chức, không là khuyến nghị mua thiết bị hiện tại.',
'HPC là phối hợp để hoàn thành một công trình lớn nhanh; HTC là xử lý thật nhiều hồ sơ độc lập.',
'Ví dụ tự xây dựng: mô phỏng lưới cần trao đổi biên mỗi bước nhạy mạng hơn hàng nghìn ảnh resize độc lập. Cùng CPU tổng nhưng interconnect khác nhau dẫn tới kết quả khác.',
'HA, HPC, HTC là các mục tiêu có thể kết hợp, không phải ba nhãn phần cứng tuyệt đối loại trừ nhau. Máy rẻ không đồng nghĩa tổng vận hành rẻ.',
'Phần cứng phổ thông giảm mua sắm nhưng tăng công quản lý, dây và nguồn khi mở rộng.',
'Vì sao benchmark một job độc lập không dự báo tốt mô phỏng trao đổi dày đặc?',
'Xử lý rất nhiều job resize ảnh độc lập, tối ưu tổng job/ngày phù hợp nhất với mục tiêu nào?',
'HTC|Chỉ HA|Chỉ tăng xung một CPU|Chỉ giảm dung lượng ảnh nguồn về 0',
'Đúng: thông lượng job là trọng tâm.|HA nói khả năng phục vụ khi lỗi, không chính là thông lượng.|Không tận dụng nhiều job độc lập.|Không phải mục tiêu tính toán hợp lệ.',terms='HPC|HTC|Beowulf')
lesson('F2.5','PVM, MPI, communicator và rank',(39,49),None,'Lập trình nhiều process cần tên nhóm giao tiếp và cách xác định mỗi process.',
'Parallel Virtual Machine (PVM) và Message Passing Interface (MPI) cung cấp cơ chế truyền thông cho chương trình song song. MPI_Init khởi tạo môi trường; communicator xác định nhóm và ngữ cảnh giao tiếp; MPI_Comm_size lấy số process, MPI_Comm_rank lấy chỉ số của process trong nhóm. MPI_Finalize kết thúc. Rank không phải ID máy vật lý; một máy có thể chạy nhiều process.',
'Đánh số thành viên trong một đội để phân công, số áo không đồng nghĩa địa chỉ tòa nhà.',
'Ví dụ tự xây dựng: size=4, rank=0..3. Mỗi rank xử lý phần dữ liệu tương ứng rồi gửi kết quả. Các lệnh EC2/Ubuntu 11.04 trong slide là ví dụ cũ để đọc luồng triển khai, không được đóng gói như môi trường thực hành hiện hành.',
'Đừng sao chép prototype hàm giản lược trên slide thành C không kiểm tra con trỏ output. MPI_Comm_size và MPI_Comm_rank dùng địa chỉ biến nhận kết quả trong mã C thực tế.',
'Phải cài môi trường MPI riêng nếu muốn chạy mã thật; ứng dụng này cung cấp đọc hiểu và mô phỏng offline, không cài MPI vào Windows.',
'Có 8 process trên 2 máy thì communicator size có thể là 8 không?',
'MPI_Comm_rank trả về gì theo communicator?',
'Chỉ số process gọi trong nhóm|Số rack vật lý|Tần số CPU|Tổng số byte mọi file',
'Đúng: định danh tương đối trong communicator.|Sai: không là topology vật lý.|Sai: không đo CPU.|Sai: không thống kê lưu trữ.',terms='MPI|PVM|rank|communicator')
lesson('F2.6','Send/Recv, collective và Barrier',(50,62),None,'Thông điệp cần khớp đúng người gửi, người nhận, tag và kiểu dữ liệu; collective cần cả nhóm phối hợp.',
'MPI_Send/MPI_Recv là giao tiếp điểm–điểm với tham số endpoint, số phần tử và kiểu dữ liệu. Bcast gửi cùng dữ liệu từ root; Scatter chia các phần; Gather thu về root; Allgather thu và chia cho toàn nhóm. Barrier chờ các process trong communicator cùng đến điểm đó. Collective phải được gọi theo quy tắc tương thích của nhóm; không chỉ root gọi là đủ.',
'Phát cùng một tờ hướng dẫn khác chia mỗi người một phần tập hồ sơ. Chuông “đợi cả đội đến” không tự cộng kết quả.',
'Ví dụ tự xây dựng: chỉ rank 0 gọi Barrier, các rank khác không bao giờ gọi: rank 0 có thể đợi mãi. Hai process đều blocking receive trước khi có ai send cũng có nguy cơ chờ nhau.',
'Blocking send không mặc định có nghĩa người nhận đã xử lý nghiệp vụ xong. Buffer, count và datatype cần khớp; count tính phần tử, không luôn byte.',
'Collective thuận tiện nhưng tạo điểm phối hợp; không dùng Barrier vô điều kiện để sửa mọi race.',
'Chọn Bcast hay Scatter nếu mỗi worker cần một đoạn khác nhau của mảng?',
'Root muốn gửi mỗi process một phần khác nhau của mảng. Chọn collective nào?',
'Scatter|Bcast|Barrier|Finalize',
'Đúng: phân phần mảng cho nhiều process.|Sai: gửi cùng dữ liệu.|Sai: chỉ đồng bộ điểm đến.|Sai: kết thúc môi trường.',terms='MPI Scatter|MPI Bcast|MPI Gather|MPI Barrier')
lesson('F2.7','Wtime, Reduce và ví dụ Monte Carlo',(63,68),None,'Đo đúng thời gian và tổng hợp đúng kết quả là điều kiện đánh giá chương trình song song.',
'MPI_Wtime lấy thời gian dạng số giây theo đồng hồ phù hợp cho khoảng đo cục bộ. MPI_Reduce kết hợp giá trị từ các process bằng phép như SUM rồi đưa kết quả về root. Mẫu Monte Carlo trong slide chia số điểm, tính tổng cục bộ rồi reduce; cần xét phần dư khi npts không chia hết và tránh các luồng ngẫu nhiên trùng nhau.',
'Mỗi nhóm đếm phần của mình rồi nộp số; người tổng kết cộng số, không cần gửi từng điểm nếu chỉ cần tổng.',
'Ví dụ tự xây dựng: số điểm trong hình tròn từng rank là 780, 790, 785, 795 với 1.000 mẫu/rank. Tổng 3.150/4.000 cho π≈3,15. Đây là kết quả mẫu, không chứng minh mọi lần chạy đều cùng giá trị.',
'Reduce khác Gather: Reduce áp phép kết hợp còn Gather thu từng phần. Tính thời gian chỉ ở một rank cần hiểu đoạn đo có bao gồm chờ các rank chậm hơn hay chưa.',
'Kết quả ngẫu nhiên có sai số; benchmark cần lặp và báo phương pháp, không so một lần chạy duy nhất.',
'Với 10 mẫu và 3 rank, bạn phân phần dư thế nào để không bỏ một mẫu?',
'Tổng điểm trong tròn 3.150 trên 4.000 điểm đều trong vuông. Ước π theo ví dụ là gì?',
'3,15|0,7875|12,6|4.000',
'Đúng: 4×3150/4000.|Sai: mới là tỷ lệ diện tích.|Sai: nhân 4 hai lần.|Sai: đó là số mẫu.',level='Vận dụng',terms='MPI Reduce|MPI Wtime')
lesson('F2.8','Gearman và mô hình client–job server–worker',(69,72),None,'Job độc lập có thể phân phối qua một bộ môi giới thay vì mọi client tự chọn worker.',
'Client gửi job cho job server, worker đăng ký loại hàm có thể xử lý và nhận job phù hợp. Gearman trong slide chỉ phân phối công việc; dữ liệu ảnh được truy cập qua file system chia sẻ. Job mang đường dẫn không có nghĩa nội dung file đã được chuyển tới worker. Các nhận xét về không mã hóa/xác thực là phạm vi cấu hình/tài liệu lịch sử, không xác nhận phiên bản hiện nay.',
'Quầy điều phối giao phiếu việc; worker còn cần lấy được hồ sơ mà phiếu chỉ tới.',
'Ví dụ tự xây dựng: client gửi /srv/media/a.jpg nhưng worker không mount thư mục đó. Job được nhận mà xử lý vẫn lỗi. Cần thống nhất đường dẫn, quyền và quy tắc đặt tên đầu ra.',
'Queue không thay shared storage. Nhận job không chứng minh xử lý thành công và lưu đầu ra bền vững.',
'Cần kiểm soát retry, idempotency, dữ liệu dùng chung và đường truyền; ví dụ không phải bộ triển khai production.',
'Nếu job bị giao lại, thao tác resize ghi đè file nên được thiết kế thế nào?',
'Job chỉ chứa đường dẫn ảnh. Worker cần điều kiện gì để xử lý?',
'Truy cập được dữ liệu tại đường dẫn hoặc cơ chế lấy dữ liệu tương ứng|Chỉ cần biết tên job server|Không cần file ảnh|Tự có file vì nhận được chuỗi đường dẫn',
'Đúng: định danh không phải nội dung.|Chưa đủ dữ liệu.|Sai: cần đầu vào.|Sai: truyền chuỗi không truyền file.',terms='Gearman|worker')

chapter('f3','Thực hành đọc kiến trúc FaaS','Function_as_a_Service(2).pdf',None,'Một nền tảng FaaS tự host có các lớp nào?|Hàm nhận sự kiện và lưu dữ liệu ra sao?', 'Vẽ luồng OpenFaaS và OpenWhisk theo tài liệu|Theo vết pipeline Minio và trigger/action/rule|Nhận diện cấu hình lịch sử cần cập nhật khi triển khai',['6.3','14.2'], 'Mô-đun bổ trợ FaaS dựa tài liệu 2019, không tự thay thế giáo trình chính hay cài nền tảng FaaS.')
lesson('F3.1','Container, Docker và nguyên tắc FaaS',(1,17),None,'Cần phân biệt container là cơ chế đóng gói còn FaaS là mô hình vận hành và kích hoạt.',
'Docker client gửi yêu cầu tới daemon, daemon quản lý image/container theo kiến trúc tài liệu. FaaS bổ sung môi trường gọi hàm, co giãn và quản lý thực thi sự kiện. Slide 14–17 dùng stateless và no side effects để giới thiệu; cần tách rõ: stateless không cấm gọi DB hay tạo tác dụng phụ. Mã ví dụ Minio và MongoDB của chính tài liệu có ghi dữ liệu.',
'Đóng gói dụng cụ không giống dịch vụ điều người dùng dụng cụ theo từng phiếu việc.',
'Ví dụ tự xây dựng: container chạy HTTP server thường trực chưa tự là nền tảng FaaS. Cần đường kích hoạt hàm, quản lý môi trường, theo dõi và chính sách tài nguyên.',
'Container hiệu quả hơn VM ở một số overhead không có nghĩa nhanh hơn cho mọi workload. “Docker có trên Windows” không suy ra Linux container dùng kernel Windows trực tiếp.',
'Tài liệu có kiến trúc/phụ thuộc 2019; đọc để hiểu vai trò, không chạy nguyên xi lệnh cũ với quyền cao.',
'Chỉ ra mâu thuẫn nếu vừa nói hàm không side effect vừa ghi vào DB, rồi sửa định nghĩa.',
'Hàm FaaS ghi kết quả vào DB có nhất thiết trái stateless không?',
'Không; stateless không dựa vào trạng thái cục bộ bền qua lần gọi, vẫn có thể ghi DB|Có; stateless cấm mọi I/O|Có; mọi hàm phải luôn trả cùng giá trị bất kể input|Không vì DB biến thành RAM cục bộ',
'Đúng: tách local state và side effect.|Sai: ví dụ trong tài liệu dùng DB/object.|Sai: không phải định nghĩa stateless.|Sai: DB vẫn là dịch vụ dữ liệu.',terms='function runtime')
lesson('F3.2','OpenFaaS: gateway, watchdog và metric',(18,25),None,'Gói mã hàm cần được nối vào HTTP và cơ chế quản lý tài nguyên.',
'Theo phiên bản trong slide, gateway định tuyến yêu cầu và cung cấp API quản lý; watchdog kết nối request với giao diện vào/ra của hàm; Prometheus thu thập metric; lớp container/orchestrator quản lý các bản chạy. Phân biệt dữ liệu metric với dữ liệu nghiệp vụ. Các script Swarm/ARM và lệnh curl|sh là ví dụ triển khai cũ, không được ứng dụng tự thực thi.',
'Quầy nhận phiếu chọn nơi làm; người trực tại bàn đưa input vào hàm và lấy output; đồng hồ đo báo tình hình hoạt động.',
'Ví dụ tự xây dựng: request lỗi có thể do gateway không tìm endpoint, container chưa ready hoặc mã hàm ném lỗi. Theo vết từng chặng giúp không quy mọi lỗi cho Python.',
'Có Prometheus không có nghĩa đã có chính sách autoscaling phù hợp. Runtime thực thi và collector metric có chức năng khác nhau.',
'Tự host cho quyền kiểm soát nhưng bạn chịu vận hành nền tảng. Phần này không cung cấp bộ cài OpenFaaS hiện hành.',
'Bạn sẽ quan sát metric và log nào khi gateway trả lỗi nhưng container đang chạy?',
'Trong kiến trúc OpenFaaS của slide, Prometheus có vai trò gì?',
'Thu thập metric để quan sát|Là kho object thay Minio|Là mã xử lý ảnh của người dùng|Là kernel riêng mỗi hàm',
'Đúng: chức năng monitoring.|Sai: lưu trữ object là vai trò khác.|Sai: business logic thuộc function.|Sai: không phải kernel.',terms='OpenFaaS|watchdog|Prometheus')
lesson('F3.3','Pipeline Minio: download, xử lý và lưu ảnh',(26,43),None,'Tách hai hàm cần thống nhất nơi lưu, sự kiện và định danh dữ liệu.',
'Ví dụ dùng Minio với bucket incoming và processed. Hàm loadimages nhận danh sách URL, tải và đưa ảnh vào kho; processimages lấy ảnh, biến đổi rồi đưa kết quả vào bucket đích. YAML mô tả hàm, image, handler và biến môi trường. Build tạo image; deploy đăng ký/chạy theo nền tảng; invoke mới kích hoạt công việc.',
'Quầy tiếp nhận nhập hàng vào kho thô; xưởng lấy hàng theo nhãn rồi trả kho thành phẩm.',
'Ví dụ diễn giải mã: (1) parse JSON urls; (2) tạo ID file; (3) tải file tạm; (4) ghi incoming; (5) truyền ID/thông báo; (6) hàm xử lý đọc đúng object; (7) lưu processed. Khi tái triển khai cần thay khóa trong ví dụ bằng cấu hình bí mật phù hợp và xác minh API theo phiên bản.',
'Có hai bucket không tự tạo trigger giữa chúng. Tệp tạm /tmp không nên là nơi lưu kết quả duy nhất. Các access key in trên slide là ví dụ, không là khóa cần dùng.',
'URL bên ngoài, kích thước file, timeout và retry cần được kiểm soát trong triển khai thật; ví dụ học không bao phủ mọi tình huống lỗi.',
'Nếu upload incoming thành công rồi thông báo xử lý thất bại, làm sao tìm các object chưa được xử lý?',
'Vai trò của hai bucket incoming và processed là gì?',
'Tách đầu vào và kết quả để pipeline theo dõi và lấy đúng dữ liệu|Tự chạy mã Python chỉ nhờ tên bucket|Thay thế mọi cơ chế trigger|Giữ kernel hai hàm độc lập',
'Đúng: phân loại dữ liệu theo giai đoạn.|Sai: tên bucket không thực thi hàm.|Sai: cần đường kích hoạt rõ.|Sai: không liên quan kernel.',level='Vận dụng',terms='Minio|bucket')
lesson('F3.4','OpenWhisk: controller, Kafka, invoker và trạng thái',(44,51),None,'Nền tảng cần tiếp nhận yêu cầu, kiểm tra, xếp luồng công việc và chạy hàm.',
'Theo kiến trúc trong tài liệu: Nginx đứng trước controller; controller xử lý yêu cầu và điều phối; Kafka làm lớp truyền thông/thông điệp; invoker thực thi action; CouchDB lưu thông tin phục vụ nền tảng. Vai trò metadata nền tảng khác dữ liệu hàng tồn kho của ứng dụng ở MongoDB. Các cách cài Docker/Vagrant/Kubernetes được trình bày theo phiên bản cũ.',
'Bàn tiếp nhận, bộ điều phối, hàng phiếu và người thực hiện là các lớp khác nhau, có thể hỏng độc lập.',
'Ví dụ tự xây dựng: action đang chờ lâu. Kiểm tra tiếp nhận, hàng đợi, invoker và giới hạn runtime trước khi chỉ tăng tài nguyên controller.',
'Kafka trong kiến trúc không tự đảm bảo logic nghiệp vụ xử lý đúng một lần. CouchDB nền tảng không tự biến thành DB nghiệp vụ ứng dụng.',
'Nhiều thành phần tăng khả năng tổ chức nhưng cũng tăng công vận hành; không coi “production ready” trên slide là xác nhận cho cấu hình bất kỳ.',
'Vẽ đường đi yêu cầu và đánh dấu chỗ dữ liệu nền tảng khác dữ liệu ứng dụng.',
'Trong kiến trúc OpenWhisk được học, invoker chủ yếu làm gì?',
'Thực thi action/hàm|Là ảnh đầu vào trong Minio|Chỉ hiển thị UI client|Là định danh VLAN',
'Đúng: lớp chạy action.|Sai: dữ liệu khác thành phần thực thi.|Sai: không phải UI.|Sai: thuộc mạng.',terms='OpenWhisk|invoker|Kafka|CouchDB')
lesson('F3.5','Action, trigger, rule và cập nhật tồn kho',(52,62),None,'Sự kiện bán hàng và nhập kho cần được nối tới logic cập nhật dữ liệu.',
'Trigger biểu diễn sự kiện, action là logic được gọi, rule nối trigger với action theo mô hình OpenWhisk trong slide. Ví dụ updateInventory dùng MongoDB và tham số sản phẩm/tồn kho. CLI create action, create trigger và create rule tạo các đối tượng khác nhau; kích hoạt trigger mới tạo luồng gọi tương ứng. Kết luận FaaS trong slide cần đọc cùng các giới hạn stateless đã làm rõ.',
'Sự kiện là phiếu báo; rule là quy tắc phiếu nào giao ai; action là công việc xử lý.',
'Ví dụ tự xây dựng: sự kiện bán 1 món được giao lại hai lần. Nếu action cứ trừ 1 mà không kiểm tra event ID, tồn kho giảm 2. Cần thiết kế cập nhật nguyên tử và chống trùng phù hợp, không mặc định FaaS tự làm.',
'Đăng ký rule không có nghĩa đã xảy ra sự kiện. Stateless không ngăn lỗi race khi nhiều hàm cùng cập nhật một sản phẩm.',
'Chuỗi cũ minh họa logic nhưng thông số deploy, cách đóng gói thư viện và sản phẩm công cộng cần xác minh khi dùng thật.',
'Khi hai action cùng đọc tồn=10 rồi cùng ghi 9, giao thức cập nhật nào cần cải thiện?',
'Trigger và action được nối với nhau bằng đối tượng nào trong ví dụ OpenWhisk?',
'Rule|VLAN|NameNode|Docker base image',
'Đúng: rule gắn sự kiện với action.|Sai: mạng lớp 2.|Sai: metadata HDFS.|Sai: lớp đóng gói không nối trigger.',terms='trigger|action|rule')

chapter('f4','Chuyên đề: Quantum Cloud Computing','NT533-L10 Introduction to Quantum Cloud Computing(1).pdf',None,'Qubit khác bit ra sao?|Cloud cung cấp truy cập QPU theo cách nào?|Lợi thế lượng tử có những điều kiện gì?', 'Tính xác suất đo qubit đơn từ biên độ|Phân biệt chồng chập, rối và giao thoa|Vẽ pipeline lai CPU–QPU và phân tích giới hạn NISQ',['2.4','F1.5'], 'Chuyên đề riêng trong NT533, không ghép vào chương 18 chỉ vì file được gửi cuối.')
lesson('F4.1','Mèo Schrödinger và 1.1 Bit vs Qubit',(1,5),None,'Một bit cổ điển có giá trị xác định trong phép đọc; trạng thái lượng tử cần mô hình biên độ và phép đo.',
'Qubit thuần có thể viết |ψ⟩=α|0⟩+β|1⟩ với α,β phức và |α|²+|β|²=1. Đo theo cơ sở tính toán cho 0 hoặc 1 với các xác suất tương ứng. Hình cầu Bloch minh họa qubit đơn thuần. Mèo Schrödinger là thí nghiệm tư duy về phép đo, không phải mô tả một con mèo được dùng làm phần cứng máy tính.',
'Phải phân biệt mô hình trạng thái trước đo với một kết quả đọc. Ví von tung đồng xu chỉ giúp hình dung xác suất, không thể hiện pha và giao thoa lượng tử.',
'Ví dụ tự xây dựng: α=√3/2, β=1/2 có P(0)=3/4, P(1)=1/4. Một lần đo không đọc cả α và β; cần nhiều lần chuẩn bị/đo để ước phân bố.',
'Qubit không đơn giản là một bit bí mật mà ta chưa biết. Pha tương đối có thể ảnh hưởng phép biến đổi và xác suất ở cơ sở đo khác.',
'Ứng dụng chỉ mô phỏng xác suất qubit đơn, không truy cập QPU và không mô phỏng toàn cơ học lượng tử.',
'Vì sao một lần đo không cho bạn toàn bộ biên độ trạng thái?',
'α=√3/2 và β=1/2. Xác suất đo được 1 theo cơ sở tính toán là gì?',
'1/4|1/2|3/4|1',
'Đúng: bình phương môđun β = (1/2)².|Sai: biên độ khác xác suất.|Sai: đó là P(0).|Sai: không phải trạng thái chắc chắn 1.',level='Vận dụng',terms='qubit|amplitude|measurement')
lesson('F4.2','1.2–1.3 Chồng chập, rối và giao thoa',(6,7),None,'Cần hiểu vì sao biểu diễn nhiều biên độ không đồng nghĩa đọc được vô số kết quả cùng lúc.',
'Chồng chập (superposition) là tổ hợp tuyến tính của các trạng thái cơ sở. Rối lượng tử (entanglement) là tính chất trạng thái nhiều phần không thể viết thành tích các trạng thái riêng tương ứng. Giao thoa (interference) làm biên độ tăng/giảm qua phép biến đổi; thuật toán thiết kế để tăng xác suất kết quả cần. n qubit có 2ⁿ biên độ trong mô hình trạng thái tổng quát nhưng một lần đo cho một chuỗi n bit.',
'“Nhiều trạng thái cùng lúc” là cách nói rút gọn về biểu diễn, không phải một màn hình liệt kê mọi đáp án sau một lần chạy.',
'Ví dụ tự xây dựng: trạng thái Bell (|00⟩+|11⟩)/√2 khi đo cơ sở tính toán cho 00 hoặc 11, mỗi loại xác suất 1/2. Tương quan không tạo kênh gửi thông tin điều khiển tức thời bằng chỉ một phép đo.',
'Không phải mọi chồng chập nhiều qubit đều rối. Có 2ⁿ biên độ không tự chứng minh tăng tốc hàm mũ cho mọi bài toán.',
'Cần thuật toán, cách nạp dữ liệu và phép đo phù hợp; lợi thế phải được phân tích trên bài toán cụ thể.',
'Nếu được một chuỗi bit từ mỗi lần đo, bạn thu thông tin về phân bố bằng cách nào?',
'Điều gì sai khi nói n qubit cho 2ⁿ trạng thái cơ sở?',
'Suy ra một phép đo đọc được tất cả 2ⁿ kết quả riêng biệt|Cần 2ⁿ biên độ để mô tả trạng thái tổng quát|Phép đo cơ sở tính toán cho chuỗi n bit|Thuật toán phải khai thác giao thoa có mục tiêu',
'Đúng: đó là suy luận sai cần tránh.|Đúng về số biên độ biểu diễn.|Đúng về kiểu đầu ra đo.|Đúng về yêu cầu thuật toán.',terms='superposition|entanglement|interference')
lesson('F4.3','1.4–1.5 Nhiễu và NISQ',(8,9),None,'Qubit khó giữ trạng thái, cổng và phép đo có lỗi nên mạch sâu không tùy ý tin cậy.',
'Noisy Intermediate-Scale Quantum (NISQ) mô tả giai đoạn thiết bị lượng tử cỡ trung gian còn nhiễu. Decoherence làm mất đặc tính trạng thái theo thời gian; sai số cổng và readout ảnh hưởng đầu ra. Các công nghệ phần cứng có yêu cầu vận hành khác nhau; không phải mọi QPU đều dùng cùng nhiệt độ hay thiết bị.',
'Thực hiện nhiều bước trên một hệ dễ nhiễu làm kết quả lệch dần; tăng số phần tử mà không kiểm soát lỗi chưa đủ.',
'Ví dụ tự xây dựng: một mạch dài có tỷ lệ đầu ra mục tiêu thấp hơn mô phỏng lý tưởng. Cần xem noise model, số shots và độ sâu, không chỉ số qubit quảng cáo.',
'Qubit vật lý khác qubit logic đã sửa lỗi. Nhiều qubit hơn không tự bảo đảm tốt hơn trên một thuật toán.',
'NISQ giới hạn các mạch có thể chạy hữu ích; error mitigation không đồng nghĩa sửa lỗi hoàn toàn.',
'Nêu ba thông tin ngoài số qubit cần biết để đánh giá backend.',
'Vì sao chỉ so số qubit vật lý chưa đủ đánh giá khả năng chạy một thuật toán?',
'Còn sai số, coherence, kết nối và độ sâu mạch cần xét|Vì mọi qubit vật lý đều không bao giờ đo được|Vì số qubit luôn bằng số CPU core|Vì cloud tự loại bỏ mọi noise',
'Đúng: chất lượng và cấu trúc quan trọng.|Sai: vẫn đo được có lỗi.|Sai: khác mô hình.|Sai: truy cập cloud không xóa nhiễu.',terms='NISQ|decoherence|physical qubit|logical qubit')
lesson('F4.4','2, 2.1 và 2.2 Lịch sử, ứng dụng và bối cảnh',(10,14),None,'Cần tách kết quả nghiên cứu, khả năng thiết bị và dự báo thị trường.',
'Slide liệt kê hướng QML, tối ưu, tìm kiếm, mô phỏng phân tử/vật liệu; mốc lịch sử nối lý thuyết với thuật toán và sửa lỗi. Biểu đồ thị trường toàn cầu và danh mục trong nước là hình chụp theo nguồn của bài giảng, không bằng chứng mọi ứng dụng đã có lợi thế thực tế. Cụm “cracks small RSA key” chỉ nói trường hợp nhỏ trong slide, không suy mọi khóa RSA thực tế đã bị phá.',
'Nguyên mẫu chứng minh một kỹ thuật khác với một dịch vụ đã hiệu quả ở quy mô sử dụng thực tế.',
'Ví dụ tự xây dựng: đề xuất QAOA cho lịch làm việc phải so cùng ràng buộc với bộ giải cổ điển, tính cả chi phí mã hóa dữ liệu, chờ QPU và đọc kết quả.',
'Grover có tăng tốc truy vấn theo mô hình nhất định, không tự giảm mọi chi phí hệ thống. Đường dự báo không phải kết quả đo tương lai đã xảy ra.',
'Chuyên đề giữ mốc theo tài liệu, không khẳng định roadmap hay thị phần hiện tại. Chi tiết ảnh thị trường không được dùng làm câu hỏi thuộc số liệu.',
'Bạn yêu cầu những bằng chứng nào trước phát biểu “lợi thế lượng tử” cho một bài toán?',
'Một ví dụ phân tích số RSA rất nhỏ có đủ chứng minh mọi khóa RSA đang dùng đều bị phá không?',
'Không; phải xét quy mô, phương pháp và tài nguyên thực tế|Có; chỉ cần cùng tên RSA|Có; mọi QPU có tài nguyên vô hạn|Có; biểu đồ thị trường tăng là bằng chứng mật mã',
'Đúng: không khái quát vượt phạm vi.|Sai: kích thước và điều kiện quyết định.|Sai: QPU hữu hạn và nhiễu.|Sai: dự báo doanh thu không chứng minh thuật toán.',terms='QML|QAOA|quantum advantage')
lesson('F4.5','3, 3.1 và 3.2 Quantum Cloud và roadmap',(15,17),None,'Thiết bị đắt và khó vận hành thúc đẩy truy cập QPU qua dịch vụ từ xa.',
'Quantum Cloud Computing (QCC) cung cấp truy cập tài nguyên lượng tử qua hạ tầng dịch vụ. Quantum as a Service (QaaS/QCaaS) cho phép client mô tả job/mạch, chọn backend, gửi yêu cầu rồi lấy kết quả đo. Backend có thể là simulator hoặc QPU thật; phải phân biệt. Bảng vendor và roadmap IBM trong slide có mốc riêng, không là trạng thái sản phẩm đã xác nhận hiện nay.',
'Thuê lượt dùng thiết bị chuyên dụng thay vì tự xây phòng thí nghiệm. Việc gửi qua cloud không làm thiết bị hết nhiễu.',
'Ví dụ tự xây dựng: CPU chuẩn bị tham số → gửi mạch → chờ hàng đợi → QPU chạy nhiều shots → lấy counts → CPU cập nhật tham số → lặp. WAN và hàng đợi có thể chi phối vòng lặp lai.',
'Quantum cloud không phải quantum Internet và không mặc định truyền qubit qua trình duyệt. Simulator chạy trên CPU không là bằng chứng đã dùng QPU thật.',
'Cần tài khoản/kết nối nếu dùng dịch vụ ngoài; ứng dụng học này chỉ có mô phỏng offline và không gửi dữ liệu tới vendor.',
'Bạn ghi metadata nào để lần sau biết đã chạy simulator hay QPU và có tái lập phép thử được không?',
'Một job quantum cloud trả counts sau nhiều shots. Bước nào thường do CPU cổ điển làm trong vòng lai?',
'Chuẩn bị/cập nhật tham số và xử lý kết quả đo|Đọc đồng thời mọi biên độ từ một shot|Loại bỏ mọi lỗi vật lý chỉ bằng HTTP|Biến simulator thành QPU thật',
'Đúng: vai trò classical orchestration.|Sai: phép đo không cho toàn bộ biên độ.|Sai: protocol không xóa noise.|Sai: backend khác nhau.',terms='QCC|QaaS|QPU|shot')
lesson('F4.6','4. Các vấn đề nghiên cứu và ranh giới khái niệm',(18,21),None,'QCC kết hợp scheduling, tài nguyên đắt, lập trình lai, bảo mật và độ đúng kết quả.',
'Tài liệu nêu các hướng distributed/parallel quantum computing, quản lý tài nguyên, lập trình, bảo mật, QML/QMLOps và quantum serverless. Quantum communication, QKD (Quantum Key Distribution) và QML là các hướng khác nhau, không hoán đổi tên. Câu hỏi nghiên cứu phải xác định bài toán, giả định, metric và baseline cổ điển.',
'“Quantum” chỉ một họ kỹ thuật; không thể dùng kết quả ở một nhánh để tự kết luận mọi nhánh khác đã giải quyết.',
'Ví dụ tự xây dựng: lập lịch job QPU tối ưu thời gian chờ phải giữ ràng buộc backend, số shots và ưu tiên. Báo cả thời gian đầu cuối lẫn thời gian QPU để tránh che chi phí orchestration.',
'Quantum serverless không có nghĩa QPU vô hạn hoặc miễn cold start/hàng đợi. QKD không tự là thuật toán tăng tốc mô phỏng phân tử.',
'Mô-đun là nhập môn từ slide; chưa có tài liệu bài tập/đề mẫu để suy cấu trúc thi chính thức của giảng viên.',
'Đặt một câu hỏi nghiên cứu có metric và baseline cho quản lý tài nguyên QCC.',
'Đánh giá hệ lập lịch QPU nên bao gồm gì?',
'Thời gian đầu cuối, thời gian chờ và ràng buộc job trên baseline rõ|Chỉ logo vendor|Chỉ số dòng mã frontend|Cam kết mọi job đều có lợi thế lượng tử',
'Đúng: metric gắn mục tiêu và điều kiện.|Không là metric hiệu năng.|Không đo chất lượng lập lịch.|Không có căn cứ để cam kết.',level='Vận dụng',terms='QKD|QMLOps')

chapter('f5','NT533: lộ trình và đồ án','NT533-L0 Introduction Project Instruction 2026(2).pdf',None,'Môn học yêu cầu sản phẩm và bằng chứng gì?|Làm sao thiết kế thí nghiệm đồ án công bằng?', 'Đọc đúng các thành phần đánh giá ghi trong tài liệu|Thiết kế đồ án có baseline, metric và dữ liệu minh chứng',['1.1'], 'Tài liệu tổ chức môn học được giữ riêng, không xem là một chương lý thuyết cloud.')
lesson('F5.1','Mục tiêu khóa học, lịch và đánh giá',(1,8),None,'Cần phân biệt phạm vi học lý thuyết với tổ chức môn và lựa chọn đề tài.',
'Tài liệu nêu các mảng distributed/parallel computing, cluster, cloud, virtualization/container, middleware/big data và microservices, sau đó nghiên cứu/đồ án. Trang 8 ghi Labs 25%, Attendance and Project 25%, Final Exam 50%. Đây là nội dung của bản PDF 2026 được cung cấp, không xác nhận thay đổi sau tài liệu. File không quy định một đề cuối kỳ 40+3; cấu trúc đó là yêu cầu của người học cho ứng dụng.',
'Bản kế hoạch môn cho biết hoạt động và cách đánh giá, không tự cung cấp đầy đủ kiến thức từng tuần.',
'Ví dụ tự xây dựng: dùng lộ trình ứng dụng ôn VM/container trước khi so chi phí VM–container–serverless ở đồ án. Các đề mock của app phục vụ tự kiểm tra, không được gắn nhãn đề thật.',
'Tỷ trọng attendance/project không phải hai mục mỗi mục 25%. Danh sách đề tài là gợi ý; trang 7 yêu cầu trao đổi giảng viên trước đăng ký.',
'Nếu thông báo giảng viên mới khác PDF, cần cập nhật nguồn và giữ mốc phiên bản.',
'Tại sao không thể suy đề cuối kỳ thật có 40 câu trắc nghiệm từ file này?',
'Tài liệu ghi 25% Labs, 25% Attendance and Project, 50% Final Exam. Điều nào đúng?',
'Attendance and Project cùng nằm trong một thành phần 25%|Attendance 25% và Project thêm 25% riêng|Labs chiếm 50%|File đã chứng minh đề thi thật gồm 40+3',
'Đúng: đọc đúng nhãn thành phần.|Sai: làm tổng vượt 100%.|Sai: Labs là 25%.|Sai: cấu trúc mock do người học yêu cầu.',terms='course assessment')
lesson('F5.2','Đề tài, báo cáo, demo và thí nghiệm',(6,11),None,'Đồ án cần chứng minh kết quả bằng phương pháp và dữ liệu, không chỉ chạy một lần để chụp ảnh.',
'Gợi ý đề tài gồm microservices autoscaling, serverless pipeline, cấp phát động, cân bằng tải, cloud đa node, so sánh VM/container/serverless, edge IoT và hybrid backup. Trang 9 yêu cầu technical report, slides, demo logs/video/scenarios/results và numerical data; cấu trúc có tác giả, giới thiệu, mô tả, related work, phân tích mã/demo và nguồn. Trang 10 ghi 14 nhóm, 4 thành viên/nhóm trong bối cảnh lớp.',
'Một demo cho thấy “chạy được”; số liệu và quy trình cho thấy “vì sao kết luận đáng tin”.',
'Ví dụ tự xây dựng: so VM/container dùng cùng logic, dữ liệu, tài nguyên và tải. Đo startup riêng, latency p50/p95, throughput, CPU/RAM và lỗi; lặp nhiều lần, giữ log và cấu hình. Nếu khác tài nguyên thì ghi rõ thay vì quy mọi khác biệt cho mô hình.',
'Một biểu đồ đẹp không thay dữ liệu gốc. Tự chọn đề tài không bỏ bước thống nhất với giảng viên như tài liệu yêu cầu.',
'Ứng dụng hỗ trợ học và lập luận; không tự thay báo cáo, thực nghiệm hoặc quy định lớp cập nhật.',
'Bạn cần lưu những gì để người khác tái lập biểu đồ so sánh?',
'Để so VM và container công bằng, nên làm gì?',
'Kiểm soát workload/tài nguyên, tách startup khỏi steady-state và lặp phép đo|Dùng hai chương trình khác nhau rồi quy khác biệt cho container|Chỉ đo một lần nhanh nhất|Chỉ chụp giao diện không lưu dữ liệu',
'Đúng: giảm yếu tố nhiễu và tăng khả năng tái lập.|Sai: thay nhiều biến cùng lúc.|Sai: thiên lệch lựa chọn.|Sai: không đủ bằng chứng định lượng.',level='Vận dụng',terms='baseline|reproducibility')

# Các thuật ngữ dùng định nghĩa riêng; ví dụ và điểm dễ nhầm dẫn về bài nguồn.
TERMS='''
Điện toán đám mây;cloud computing;;Cung cấp tài nguyên hoặc ứng dụng tính toán dưới dạng dịch vụ qua mạng.;1.1
Người thuê;tenant;;Khách hàng hoặc đơn vị logic được cấp tài nguyên/quyền trong hạ tầng dịch vụ.;1.1
Bức tường công suất;power wall;;Giới hạn thực tế do điện và nhiệt khi tiếp tục tăng hiệu năng bộ xử lý theo cách truyền thống.;1.2
Đa lõi;multicore;;Một bộ xử lý có nhiều lõi thực thi, cần phần mềm phù hợp để khai thác song song.;1.2
Cụm máy tính;cluster;;Nhóm nút độc lập nối qua mạng để cùng cung cấp dịch vụ hoặc xử lý công việc.;1.3
Tủ thiết bị;rack;;Kết cấu chuẩn hóa dùng lắp thiết bị như server và switch.;1.3
Nhiều người thuê;multi-tenancy;;Nhiều tenant chia sẻ hạ tầng với cơ chế phân bổ và cách ly.;1.4
Chi phí vốn;Capital Expenditure;CAPEX;Chi phí đầu tư tài sản phục vụ hoạt động dài hạn trong mô hình phân tích.;1.4
Chi phí vận hành;Operating Expenditure;OPEX;Chi phí duy trì hoạt động như điện, nhân lực và thuê dịch vụ theo mô hình.;1.4
Cân bằng tải;load balancer;;Thành phần phân phối yêu cầu tới các endpoint theo chính sách và trạng thái.;1.5
Ứng dụng phân tán;distributed application;;Ứng dụng có các thành phần hoạt động trên nhiều nút và phối hợp qua truyền thông.;1.5
Tính co giãn;elasticity;;Điều chỉnh tăng và giảm tài nguyên theo thay đổi nhu cầu.;2.1
Khả năng mở rộng;scalability;;Khả năng tận dụng thêm tài nguyên để xử lý khối lượng công việc lớn hơn.;2.1
Máy ảo;Virtual Machine;VM;Máy tính logic có trạng thái CPU, RAM và thiết bị được lớp ảo hóa cung cấp.;2.2
Trình giám sát máy ảo;hypervisor;;Lớp quản lý và cách ly tài nguyên cho các máy ảo.;2.2
Hạ tầng như dịch vụ;Infrastructure as a Service;IaaS;Mô hình cung cấp compute, mạng và lưu trữ trong khi khách thường quản lý guest OS và ứng dụng.;2.3
Nền tảng như dịch vụ;Platform as a Service;PaaS;Mô hình cung cấp môi trường phát triển/chạy ứng dụng cùng các lớp nền được quản lý.;2.4
Khóa chặt nhà cung cấp;vendor lock-in;;Mức phụ thuộc khiến chuyển nhà cung cấp tốn kém do API, dữ liệu, quy trình hoặc dịch vụ liên quan.;3.2
Phần mềm như dịch vụ;Software as a Service;SaaS;Ứng dụng hoàn chỉnh do nhà cung cấp vận hành cho người dùng truy cập.;2.5
Desktop như dịch vụ;Desktop as a Service;DaaS;Cung cấp môi trường desktop từ xa theo nghĩa được dùng trong sách.;2.5
Đám mây riêng;private cloud;;Hạ tầng cloud dành cho một tổ chức, không chỉ là một VM có IP riêng.;3.1
Đám mây công cộng;public cloud;;Dịch vụ cloud cung cấp cho nhiều khách hàng, không đồng nghĩa dữ liệu công khai.;3.1
Đám mây lai;hybrid cloud;;Kiến trúc kết hợp private và public cloud cho các phần công việc có quan hệ.;3.3
Đa đám mây;multi-cloud;;Sử dụng dịch vụ của nhiều nhà cung cấp cloud.;3.3
Pod hạ tầng;infrastructure pod;;Đơn vị vật lý nhóm rack cùng năng lực mạng, điện và làm mát.;4.1
Lối nóng;hot aisle;;Lối tập trung phía thải khí nóng của các hàng thiết bị trong mô hình hot/cold aisle.;4.2
Lối lạnh;cold aisle;;Lối cấp khí lạnh đến phía hút khí của thiết bị.;4.2
Lưu lượng nội bộ;east-west;;Lưu lượng giữa các thành phần bên trong trung tâm dữ liệu.;4.3
Lưu lượng vào ra;north-south;;Lưu lượng đi vào hoặc ra ngoài trung tâm dữ liệu.;4.3
Switch đầu rack;Top-of-Rack;ToR;Switch nối các máy trong rack tới mạng phía trên.;4.3
Gộp liên kết;link aggregation;;Ghép nhiều liên kết thành nhóm logic để tăng năng lực tổng hoặc dự phòng.;4.3
Mạng leaf-spine;leaf-spine;;Topology nối leaf tới các spine để tạo nhiều đường giữa các leaf.;4.4
Lưu trữ từ xa;remote storage;;Truy cập giao diện lưu trữ qua mạng thay vì chỉ thiết bị cục bộ.;8.2
Giả lập;emulation;;Tái hiện hoạt động một kiến trúc hoặc thiết bị bằng phần mềm/hệ thống khác.;5.1
Mã trung gian;bytecode;;Biểu diễn lệnh cho môi trường thực thi ngôn ngữ thay vì trực tiếp tập lệnh CPU đích.;5.1
Bộ quản lý bộ nhớ;Memory Management Unit;MMU;Phần cứng dịch địa chỉ và hỗ trợ bảo vệ truy cập bộ nhớ.;5.2
Mức đặc quyền;privilege level;;Mức quyền thực thi quyết định các thao tác nhạy cảm được phép.;5.2
Ảo hóa bán phần;paravirtualization;;Guest được điều chỉnh để phối hợp hypervisor qua giao diện như hypercall.;5.3
Ảo hóa toàn phần;full virtualization;;Cung cấp môi trường máy ảo nhằm chạy guest không sửa với cách ly và hiệu quả.;5.3
Lời gọi hypervisor;hypercall;;Yêu cầu guest gửi đến hypervisor để thực hiện thao tác quản lý/đặc quyền.;5.3
Vào ra ảo;virtual I/O;;Giao diện thiết bị guest nhìn thấy, được lớp ảo hóa nối tới backend thực.;5.4
Đĩa ảo;virtual disk;;Không gian block logic được ánh xạ tới file, volume hoặc tài nguyên vật lý.;5.4
Di chuyển sống;live migration;;Chuyển VM đang hoạt động với mục tiêu giảm khoảng dừng bằng chuyển trạng thái có tổ chức.;5.5
Trang bẩn;dirty page;;Trang RAM đã được ghi thay đổi kể từ mốc theo dõi hoặc sao chép.;5.5
Hypervisor hosted;hosted hypervisor;;Mô hình chạy máy ảo dựa trên host OS và các dịch vụ của host.;5.6
Container;container;;Môi trường tiến trình được cách ly và quản lý tài nguyên, thường chia sẻ kernel host.;6.2
Không gian tên;namespace;;Cơ chế cung cấp góc nhìn riêng cho một nhóm tài nguyên hệ điều hành.;6.2
Nhóm kiểm soát;control group;cgroup;Cơ chế Linux quản lý/hạch toán và giới hạn sử dụng tài nguyên theo nhóm tiến trình.;6.2
Nhân hệ điều hành;kernel;;Thành phần lõi quản lý tiến trình, bộ nhớ, thiết bị và quyền truy cập.;6.2
Công thức image;Dockerfile;;Tệp chỉ dẫn các bước build image và metadata chạy mặc định.;6.3
Ảnh container;container image;image;Gói các lớp file và metadata dùng tạo phiên container.;6.3
Kho phân phối image;registry;;Dịch vụ lưu và phân phối container image.;6.3
Bộ thực thi container;container runtime;;Lớp thiết lập và quản lý môi trường để tiến trình container chạy.;6.4
Linux Containers;Linux Containers;LXC;Bộ công cụ container dựa cơ chế cách ly OS, trong slide hướng môi trường hệ thống.;6.4
Mạng nền;underlay;;Mạng cung cấp kết nối vận chuyển vật lý/IP cho lớp mạng phủ.;7.1
Mạng phủ;overlay;;Mạng logic xây trên mạng nền, thường dùng đóng gói và ánh xạ endpoint.;7.1
Mạng ảo;virtual network;;Góc nhìn kết nối logic tách một phần khỏi vị trí và cấu tạo mạng vật lý.;7.1
LAN ảo;Virtual Local Area Network;VLAN;Phân đoạn lớp 2 bằng cấu hình cổng và thẻ định danh VLAN.;7.2
Switch ảo;virtual switch;;Chức năng chuyển mạch trong host nối giao diện ảo và uplink.;7.2
LAN mở rộng ảo;Virtual eXtensible LAN;VXLAN;Đóng gói khung Ethernet trong UDP/IP để vận chuyển mạng logic trên IP underlay.;7.3
Định danh VXLAN;VXLAN Network Identifier;VNI;Trường 24 bit xác định mạng logic trong VXLAN.;7.3
Đầu cuối VXLAN;VXLAN Tunnel Endpoint;VTEP;Điểm thêm/bỏ đóng gói VXLAN và nối workload với tunnel.;7.3
Dịch địa chỉ mạng;Network Address Translation;NAT;Thay địa chỉ và có thể cổng để ánh xạ kết nối giữa các phạm vi mạng.;7.4
Địa chỉ riêng;private IP;;Địa chỉ có phạm vi định tuyến riêng, có thể được dùng lặp trong các mạng độc lập.;7.4
Mạng điều khiển bằng phần mềm;Software Defined Networking;SDN;Cách tổ chức tách logic điều khiển khỏi chức năng chuyển tiếp và dùng giao diện lập trình.;7.5
Giao thức OpenFlow;OpenFlow;;Giao diện điều khiển bảng luồng trong một cách tiếp cận SDN.;7.5
Lưu trữ khối;block storage;;Giao diện đọc/ghi các khối theo địa chỉ logic.;8.1
Hệ thống file;file system;;Lớp quản lý tên, metadata và ánh xạ nội dung file tới không gian lưu trữ.;8.1
Kibibyte;kibibyte;KiB;Đơn vị bằng 2¹⁰ = 1.024 byte.;8.1
Hạ tầng siêu hội tụ;Hyper-Converged Infrastructure;HCI;Mô hình gộp và quản lý compute/storage theo cụm trong phần sách bổ trợ.;8.2
Lưu trữ gắn mạng;Network Attached Storage;NAS;Cung cấp dịch vụ file qua mạng.;8.3
Mạng lưu trữ;Storage Area Network;SAN;Mạng cung cấp truy cập lưu trữ, thường ở giao diện block trong bài.;8.3
Lưu trữ đối tượng;object storage;;Quản lý nội dung và metadata theo khóa/định danh đối tượng qua API.;8.4
Tự động hóa;automation;;Thực thi tác vụ/quy trình bằng phần mềm thay thao tác lặp thủ công.;9.1
Tính lũy đẳng;idempotency;;Thực hiện lặp cùng yêu cầu không gây thêm tác dụng vượt kết quả đã định nghĩa sau lần đầu.;9.2
AI cho vận hành;Artificial Intelligence for IT Operations;AIOps;Áp dụng kỹ thuật dữ liệu/AI hỗ trợ quan sát, phân tích hoặc hành động vận hành.;9.3
Giám sát;monitoring;;Thu thập và đánh giá tín hiệu trạng thái/hiệu năng của hệ thống.;9.3
Hạ tầng dưới dạng mã;Infrastructure as Code;IaC;Quản lý mô tả hạ tầng bằng tệp có thể lưu phiên bản và xử lý bằng công cụ.;9.4
Khai báo;declarative;;Mô tả trạng thái mong muốn thay vì chỉ dẫn hết thứ tự thao tác.;9.4
Mệnh lệnh;imperative;;Mô tả các bước/thao tác phải thực hiện.;9.4
Đẩy cấu hình;push;;Bộ điều khiển chủ động gửi/áp cấu hình tới thiết bị.;9.5
Kéo cấu hình;pull;;Thiết bị/agent chủ động lấy cấu hình từ nguồn quản lý.;9.5
Điều phối;orchestration;;Phối hợp nhiều tác vụ tự động và quan hệ trong vòng đời dịch vụ.;10.1
Bộ lập lịch;scheduler;;Thành phần chọn vị trí chạy theo tài nguyên và ràng buộc.;10.2
Tự co giãn;autoscaling;;Cơ chế tự điều chỉnh năng lực/số bản sao theo metric và chính sách.;10.2
Triển khai dần;rollout;;Quá trình đưa phiên bản/cấu hình mới vào hệ thống có kiểm soát.;10.3
Quay lại phiên bản;rollback;;Đưa mã/cấu hình về trạng thái trước phù hợp, không mặc định hoàn tác mọi dữ liệu.;10.3
Khám phá dịch vụ;service discovery;;Cơ chế tìm endpoint dịch vụ khi vị trí/bản sao thay đổi.;10.3
Sẵn sàng phục vụ;readiness;;Trạng thái endpoint có thể tiếp nhận và xử lý công việc theo kiểm tra được định nghĩa.;10.3
Pod Kubernetes;Kubernetes Pod;Pod;Đơn vị chạy gồm các container liên quan chia sẻ một số tài nguyên như mạng Pod.;10.4
Container khởi tạo;init container;;Container thực hiện chuẩn bị trước app container theo mô hình thông thường của tài liệu.;10.4
Mẫu đối tượng;template;;Mô tả dùng tạo các đối tượng/Pod mới với cấu hình xác định.;10.4
Mặt phẳng điều khiển;control plane;;Các thành phần API, trạng thái, lập lịch và điều khiển của cluster.;10.5
Agent node;kubelet;;Thành phần node phối hợp trạng thái Pod với runtime và báo trạng thái.;10.5
Thiết kế cho cloud;cloud-native;;Phần mềm được thiết kế để tận dụng cách triển khai và vận hành của môi trường cloud.;11.1
Song song dữ liệu;data parallelism;;Áp một loại xử lý lên các phần dữ liệu có thể phân chia.;11.1
Mô hình MapReduce;MapReduce;;Mô hình map phát cặp khóa–giá trị, group cùng khóa rồi reduce.;11.2
Gom và chuyển theo khóa;shuffle;;Giai đoạn phân phối/gom kết quả map để các giá trị cùng khóa được xử lý cùng nhau.;11.2
Bộ xử lý tổng hợp;reducer;;Tác vụ xử lý một hoặc nhiều nhóm khóa sau shuffle.;11.2
Lệch tải dữ liệu;data skew;;Phân bố dữ liệu/chi phí không đều gây một số tác vụ trở thành nút thắt.;11.3
Tính cục bộ dữ liệu;data locality;;Đặt tính toán gần bản sao dữ liệu để giảm chi phí truyền.;11.3
Phân vùng bằng hash;hash partition;;Ánh xạ khóa tới partition qua hàm hash theo quy tắc xác định.;11.3
Nền tảng Hadoop;Apache Hadoop;Hadoop;Hệ sinh thái lưu trữ và xử lý phân tán trong mô hình dữ liệu lớn.;11.4
Hệ thống file Hadoop;Hadoop Distributed File System;HDFS;Lưu file thành các block trên DataNode cùng metadata được quản lý.;11.4
Node metadata;NameNode;;Thành phần quản lý tên, metadata và vị trí block HDFS.;11.4
Node dữ liệu;DataNode;;Thành phần lưu và phục vụ các block HDFS.;11.4
Vi dịch vụ;microservices;;Kiến trúc tách chức năng thành các dịch vụ có giao diện và khả năng triển khai độc lập.;12.1
Ứng dụng nguyên khối;monolith;;Một đơn vị triển khai chứa nhiều chức năng có thể được chia module bên trong.;12.1
Lỗi dây chuyền;cascading failure;;Lỗi/chậm một thành phần dẫn tới cạn tài nguyên hoặc lỗi ở các thành phần phụ thuộc.;12.2
Độ hạt;granularity;;Mức lớn nhỏ của đơn vị công việc/dịch vụ, ảnh hưởng phối hợp và độc lập.;12.2
Đồng bộ;synchronous;;Luồng xử lý chờ kết quả theo mô hình điều khiển giao tiếp.;12.3
Bất đồng bộ;asynchronous;;Tách việc gửi công việc với thời điểm nhận hoặc xử lý kết quả.;12.3
Hàng đợi thông điệp;message queue;;Lớp nhận, giữ và phân phối thông điệp theo các cam kết giao nhận cụ thể.;12.3
Tuần tự hóa dữ liệu;serialization;;Biến dữ liệu thành biểu diễn truyền/lưu theo định dạng đã thống nhất.;12.4
Lược đồ dữ liệu;schema;;Mô tả cấu trúc, kiểu và quy tắc của dữ liệu/hợp đồng.;12.4
Lưới dịch vụ;service mesh;;Lớp quản lý giao tiếp giữa dịch vụ qua proxy và chính sách điều khiển.;12.5
Đại diện trung gian;proxy;;Thành phần nhận/chuyển yêu cầu thay một endpoint, có thể thực thi chính sách.;12.5
Bộ điều khiển;controller;;Thành phần so trạng thái quan sát với mục tiêu rồi thực hiện hành động hội tụ.;13.1
Vòng điều khiển;control loop;;Chu trình quan sát, so sánh và điều chỉnh lặp lại.;13.1
Trạng thái mong muốn;desired state;;Mô tả kết quả/điều kiện hệ thống cần đạt và duy trì.;13.1
Trễ và phụ thuộc lịch sử;hysteresis;;Khái niệm đáp ứng phụ thuộc lịch sử, trong slide còn được dùng rộng để nói hiệu ứng phản ứng trễ.;13.2
Cửa sổ ổn định;stabilization window;;Khoảng quan sát/chính sách làm mượt thay đổi để giảm quyết định co giãn dao động.;13.2
Đối soát trạng thái;reconciliation;;Đọc trạng thái hiện tại và thực hiện bước đưa về mục tiêu, có thể cần lặp lại.;13.3
Định nghĩa tài nguyên tùy chỉnh;Custom Resource Definition;CRD;Mở rộng kiểu đối tượng API Kubernetes, không tự chứa toàn bộ hành vi vận hành.;13.3
Mẫu operator;operator;;Kết hợp tài nguyên tùy chỉnh và controller để đóng gói tri thức vận hành.;13.3
Máy khách–máy phục vụ;client-server;;Mô hình client yêu cầu dịch vụ theo giao thức và server cung cấp/đáp ứng.;14.1
Hàm như dịch vụ;Function as a Service;FaaS;Nền tảng kích hoạt và quản lý thực thi hàm theo sự kiện.;14.2
Không giữ trạng thái cục bộ bền;stateless;;Không phụ thuộc trạng thái nội bộ của một instance để duy trì ngữ cảnh bền giữa các lần gọi.;14.2
Hướng sự kiện;event-driven;;Kích hoạt xử lý theo sự kiện được phát sinh và chuyển tới thành phần phù hợp.;14.2
Khởi tạo lạnh;cold start;;Phần chậm do chuẩn bị môi trường trước khi có thể xử lý yêu cầu.;14.3
Thu về không bản sao;scale-to-zero;;Giảm số instance compute về 0 khi nhàn rỗi ở nền tảng hỗ trợ.;14.3
Văn hóa DevOps;Development and Operations;DevOps;Cách tổ chức phối hợp phát triển, kiểm thử và vận hành với trách nhiệm chung.;15.1
Tích hợp liên tục;Continuous Integration;CI;Tích hợp thay đổi thường xuyên cùng build/test tự động.;15.2
Sẵn sàng phát hành liên tục;Continuous Delivery;CD;Giữ thay đổi đủ điều kiện để có thể triển khai, có thể còn bước quyết định phát hành.;15.2
Triển khai tự động liên tục;Continuous Deployment;;Đưa thay đổi đạt điều kiện lên môi trường đích tự động theo quy trình.;15.2
Triển khai thăm dò;canary;;Đưa phiên bản mới tới phần nhỏ lưu lượng rồi quan sát trước khi mở rộng.;15.3
Hai môi trường chuyển vai;blue-green;;Chuẩn bị hai môi trường và chuyển lưu lượng giữa môi trường cũ/mới có kiểm soát.;15.3
Môi trường thử tách biệt;sandbox;;Môi trường thử nghiệm cách biệt production theo thiết kế.;15.3
Kỹ thuật độ tin cậy;Site Reliability Engineering;SRE;Áp dụng kỹ thuật phần mềm vào vận hành và độ tin cậy hệ thống.;15.4
Mục tiêu mức dịch vụ;Service Level Objective;SLO;Mục tiêu đo được cho mức dịch vụ trên metric và khoảng thời gian xác định.;15.4
Ngân sách lỗi;error budget;;Phần không đạt mục tiêu được chấp nhận theo định nghĩa SLO trong khoảng đo.;15.4
Độ trễ;latency;;Thời gian từ một mốc gửi/yêu cầu đến mốc nhận/hoàn tất đã xác định.;16.1
Băng thông;bandwidth;;Năng lực truyền dữ liệu trên đơn vị thời gian, không đồng nghĩa độ trễ.;16.1
Điện toán biên;edge computing;;Đặt tính toán/lưu trữ gần nguồn hoặc nơi sử dụng dữ liệu.;16.2
Điện toán sương mù;fog computing;;Mô hình phân cấp các tầng xử lý trung gian giữa thiết bị và cloud.;16.2
Bộ nhớ đệm;cache;;Giữ bản dữ liệu để phục vụ lại nhanh hơn theo quy tắc độ mới và loại bỏ.;16.2
IoT công nghiệp;Industrial Internet of Things;IIoT;Ứng dụng kết nối cảm biến/thiết bị và xử lý dữ liệu trong bối cảnh công nghiệp.;16.3
Vùng phi quân sự mạng;Demilitarized Zone;DMZ;Vùng mạng dành cho dịch vụ tiếp xúc bên ngoài với kiểm soát giữa các vùng.;17.1
Bề mặt tấn công;attack surface;;Tập điểm và đường tương tác có thể bị khai thác để tác động hệ thống.;17.1
Mã hóa;encryption;;Biến nội dung thành biểu diễn được bảo vệ bằng cơ chế mật mã và quản lý khóa.;17.2
Bảo mật tầng truyền tải;Transport Layer Security;TLS;Giao thức bảo vệ kết nối giữa các điểm kết thúc theo cấu hình xác thực/mật mã.;17.2
Mã hóa đầu cuối;end-to-end encryption;;Bảo vệ nội dung giữa hai đầu cuối đã xác định, cần nêu rõ ai giữ khóa và nơi giải mã.;17.2
Xác thực;authentication;;Kiểm tra danh tính theo thông tin xác thực được chấp nhận.;17.3
Phân quyền;authorization;;Quyết định chủ thể có được thực hiện hành động trên tài nguyên hay không.;17.3
Đăng nhập một lần;Single Sign-On;SSO;Cơ chế dùng một lần/quy trình đăng nhập để truy cập nhiều dịch vụ theo quyền.;17.3
Không tin mặc định;zero trust;;Không cấp tin cậy chỉ vì vị trí mạng, cần xác minh và cấp quyền theo ngữ cảnh.;17.3
Quản lý danh tính và truy cập;Identity and Access Management;IAM;Hệ thống quản lý chủ thể, thông tin định danh và chính sách quyền truy cập.;17.3
Mạng riêng ảo;Virtual Private Network;VPN;Kết nối mạng logic qua mạng trung gian, thường dùng tunnel được bảo vệ theo giao thức.;17.4
Đường hầm SSH;SSH tunnel;;Chuyển tiếp các kết nối/cổng được chọn qua một phiên SSH.;17.4
Độ phức tạp phân tán;distributed complexity;;Khó khăn từ đồng thời, lỗi, độ trễ và nhiều trạng thái/tương tác trên các nút.;18.1
Mô hình;model;;Biểu diễn có chọn lọc của hệ thống để suy luận trong phạm vi giả định.;18.2
Nguyên mẫu;prototype;;Phiên bản thực nghiệm để kiểm tra giả định công nghệ/kiến trúc.;18.2
Bế tắc;deadlock;;Tập tác vụ bị chặn do các phụ thuộc chờ khiến không tác vụ nào tiến triển.;18.3
Tính an toàn;safety;;Tính chất ngăn điều xấu đã định nghĩa xảy ra.;18.3
Tính tiến triển;liveness;;Tính chất yêu cầu cuối cùng có tiến triển dưới các giả định đã nêu.;18.3
Đặc tả logic thời gian;Temporal Logic of Actions;TLA+;Ngôn ngữ đặc tả trạng thái và hành vi theo thời gian để suy luận hệ thống.;18.3
Quyền tự chủ số;digital autonomy;;Khả năng kiểm soát sử dụng và di chuyển dữ liệu/công cụ trong phạm vi phân tích của bài.;F1.1
Máy khách nhẹ;thin client;;Client thực hiện ít nhiệm vụ xử lý/lưu trữ hơn, dựa nhiều vào server.;F1.2
Máy khách đầy đủ;fat client;;Client đảm nhận nhiều nhiệm vụ tính toán và giao diện theo phân loại bài.;F1.2
Kilowatt giờ;kilowatt-hour;kWh;Đơn vị năng lượng bằng công suất 1 kW duy trì trong 1 giờ.;F1.3
Định luật Moore;Moore law;;Quy luật quan sát lịch sử về mật độ/số transistor, không bảo đảm tốc độ mọi ứng dụng.;F1.3
Nút thắt Von Neumann;Von Neumann bottleneck;;Giới hạn hiệu năng do đường truyền và truy cập giữa xử lý và bộ nhớ.;F1.3
Định luật Amdahl;Amdahl law;;Mô hình tăng tốc bài toán cố định bị giới hạn bởi phần tuần tự và overhead.;F1.4
Hệ số tăng tốc;speedup;;Tỷ lệ thời gian tham chiếu chia thời gian thực thi với cấu hình đang xét.;F1.4
Định luật Gustafson;Gustafson law;;Mô hình scaled speedup khi tăng kích thước phần song song theo tài nguyên.;F1.5
Phương pháp Monte Carlo;Monte Carlo;;Ước lượng bằng các mẫu ngẫu nhiên theo mô hình xác suất.;F1.5
Bộ nhớ chia sẻ;shared memory;;Mô hình nhiều bộ xử lý truy cập không gian địa chỉ dùng chung với cơ chế đồng bộ.;F1.6
Bộ nhớ phân tán;distributed memory;;Mỗi nút có bộ nhớ riêng và trao đổi qua truyền thông.;F1.6
Đa xử lý đối xứng;Symmetric Multiprocessing;SMP;Mô hình các CPU có vai trò tương đương trong tổ chức hệ thống theo bài.;F1.6
Gibibyte;gibibyte;GiB;Đơn vị bằng 2³⁰ = 1.073.741.824 byte.;F1.6
Cụm workstation;Cluster of Workstations;COW;Dùng workstation làm nút, có thể chỉ khả dụng ở thời gian nhàn rỗi.;F2.1
Mạng workstation;Network of Workstations;NOW;Mô hình khai thác nhóm workstation nối mạng theo ngữ cảnh bài.;F2.1
Cụm không đồng nhất;heterogeneous cluster;;Cluster có khác biệt về năng lực hoặc cấu hình giữa các node.;F2.1
Độ sẵn sàng cao;High Availability;HA;Mục tiêu duy trì dịch vụ hoạt động và giảm thời gian gián đoạn.;F2.2
Thời gian hoạt động trung bình;Mean Time Between Failures;MTBF;Đại lượng thời gian hoạt động trung bình giữa lỗi theo quy ước mô hình trong bài.;F2.2
Thời gian sửa trung bình;Mean Time To Repair;MTTR;Thời gian trung bình khôi phục sau lỗi theo mô hình.;F2.2
Chia não;split brain;;Các phía đồng thời tự coi mình có quyền hoạt động/ghi độc quyền do mất phối hợp.;F2.2
Chuyển vai khi lỗi;failover;;Chuyển nhiệm vụ dịch vụ sang thành phần khác khi phát hiện lỗi theo chính sách.;F2.2
Nhân bản block phân tán;Distributed Replicated Block Device;DRBD;Cơ chế nhân bản thiết bị block giữa các nút theo cấu hình.;F2.3
Không chia sẻ lưu trữ;shared nothing;;Mô hình các node dùng tài nguyên lưu trữ riêng và phối hợp/nhân bản khi cần.;F2.3
Đĩa chia sẻ;shared disk;;Mô hình nhiều node truy cập hạ tầng lưu trữ chung với cơ chế phối hợp.;F2.3
Tính toán hiệu năng cao;High Performance Computing;HPC;Mục tiêu giải công việc tính toán lớn hiệu quả, thường cần phối hợp chặt.;F2.4
Tính toán thông lượng cao;High Throughput Computing;HTC;Mục tiêu hoàn thành nhiều job trong thời gian dài.;F2.4
Cụm Beowulf;Beowulf;;Cluster tính toán chuyên dụng từ phần cứng phổ thông/phần mềm tự do theo ngữ cảnh tài liệu.;F2.4
Giao diện truyền thông điệp;Message Passing Interface;MPI;Chuẩn giao diện cho truyền thông giữa các process trong chương trình song song.;F2.5
Máy ảo song song;Parallel Virtual Machine;PVM;Bộ công cụ truyền thông để ghép các máy thành môi trường tính toán song song.;F2.5
Chỉ số process;rank;;Định danh tương đối của process trong communicator MPI.;F2.5
Nhóm và ngữ cảnh giao tiếp;communicator;;Đối tượng xác định tập process và ngữ cảnh truyền thông MPI.;F2.5
Chia mảng;MPI_Scatter;MPI Scatter;Collective phân các phần dữ liệu từ root tới process trong nhóm.;F2.6
Phát cùng dữ liệu;MPI_Bcast;MPI Bcast;Collective gửi cùng dữ liệu từ root tới các process trong nhóm.;F2.6
Thu dữ liệu;MPI_Gather;MPI Gather;Collective tập hợp các phần dữ liệu từ nhóm về root.;F2.6
Hàng rào đồng bộ;MPI_Barrier;MPI Barrier;Điểm chờ tới khi các process trong communicator đều đến theo quy tắc collective.;F2.6
Tổng hợp dữ liệu;MPI_Reduce;MPI Reduce;Collective áp phép kết hợp lên dữ liệu nhóm và đưa kết quả tới root.;F2.7
Đồng hồ MPI;MPI_Wtime;MPI Wtime;Hàm lấy mốc thời gian để đo khoảng thực thi trên process.;F2.7
Bộ phân phối job;Gearman;;Framework theo client, job server và worker như mô hình trong slide.;F2.8
Tiến trình làm việc;worker;;Thành phần nhận và xử lý công việc được phân phối.;F2.8
Runtime hàm;function runtime;;Môi trường nhận sự kiện, gọi mã hàm và quản lý phần thực thi theo nền tảng.;F3.1
Nền tảng OpenFaaS;OpenFaaS;;Nền tảng hàm dựa container với gateway và các thành phần vận hành theo tài liệu.;F3.2
Cầu nối hàm;watchdog;;Thành phần nối giao diện yêu cầu với vào/ra hàm theo phiên bản OpenFaaS trong slide.;F3.2
Hệ thu metric;Prometheus;;Hệ thống thu thập số liệu phục vụ giám sát trong kiến trúc minh họa.;F3.2
Kho Minio;Minio;;Dịch vụ object storage được dùng làm kho đầu vào/kết quả pipeline ảnh.;F3.3
Thùng đối tượng;bucket;;Đơn vị nhóm object trong mô hình kho đối tượng.;F3.3
Nền tảng OpenWhisk;Apache OpenWhisk;OpenWhisk;Nền tảng thực thi action theo sự kiện với controller và invoker trong tài liệu.;F3.4
Bộ chạy action;invoker;;Thành phần thực thi action theo kiến trúc OpenWhisk được học.;F3.4
Lớp thông điệp Kafka;Apache Kafka;Kafka;Thành phần truyền thông/thông điệp trong kiến trúc OpenWhisk của slide.;F3.4
Kho metadata CouchDB;Apache CouchDB;CouchDB;Kho dữ liệu phục vụ nền tảng trong kiến trúc OpenWhisk minh họa.;F3.4
Sự kiện kích hoạt;trigger;;Đối tượng biểu diễn sự kiện dùng kích hoạt luồng action trong mô hình OpenWhisk.;F3.5
Hàm hành động;action;;Đơn vị logic/hàm được gọi bởi nền tảng OpenWhisk.;F3.5
Quy tắc nối;rule;;Đối tượng nối trigger tới action trong ví dụ OpenWhisk.;F3.5
Bit lượng tử;quantum bit;qubit;Đơn vị trạng thái lượng tử hai mức, biểu diễn bằng biên độ chuẩn hóa và phép đo.;F4.1
Biên độ xác suất;probability amplitude;amplitude;Hệ số phức của trạng thái cơ sở, bình phương môđun cho xác suất đo tương ứng.;F4.1
Phép đo;measurement;;Thao tác cho kết quả theo cơ sở và phân bố xác suất của trạng thái lượng tử.;F4.1
Chồng chập;superposition;;Tổ hợp tuyến tính các trạng thái cơ sở, không là khả năng đọc mọi kết quả cùng lúc.;F4.2
Rối lượng tử;entanglement;;Tính chất trạng thái tổng không phân tích được thành tích trạng thái các phần tương ứng.;F4.2
Giao thoa;interference;;Sự kết hợp biên độ làm tăng hoặc giảm xác suất đầu ra sau phép biến đổi.;F4.2
Lượng tử cỡ trung gian có nhiễu;Noisy Intermediate-Scale Quantum;NISQ;Bối cảnh thiết bị lượng tử còn nhiễu và quy mô chưa có sửa lỗi đầy đủ theo chuyên đề.;F4.3
Mất kết hợp;decoherence;;Quá trình trạng thái mất đặc tính kết hợp lượng tử do tương tác môi trường.;F4.3
Qubit vật lý;physical qubit;;Đơn vị phần cứng lượng tử thực tế chịu nhiễu.;F4.3
Qubit logic;logical qubit;;Đơn vị lượng tử được mã hóa để kiểm soát lỗi theo sơ đồ phù hợp.;F4.3
Học máy lượng tử;Quantum Machine Learning;QML;Hướng dùng phương pháp lượng tử trong các bài toán/mô hình học máy.;F4.4
Tối ưu xấp xỉ lượng tử;Quantum Approximate Optimization Algorithm;QAOA;Họ thuật toán lai biến phân cho tối ưu theo chuyên đề.;F4.4
Lợi thế lượng tử;quantum advantage;;Lợi ích đã đánh giá của cách lượng tử so baseline cổ điển cho bài toán và điều kiện cụ thể.;F4.4
Điện toán đám mây lượng tử;Quantum Cloud Computing;QCC;Cung cấp truy cập tài nguyên lượng tử qua dịch vụ từ xa và điều phối cloud.;F4.5
Lượng tử như dịch vụ;Quantum as a Service;QaaS;Mô hình truy cập tài nguyên lượng tử theo dịch vụ, còn gọi QCaaS trong slide.;F4.5
Bộ xử lý lượng tử;Quantum Processing Unit;QPU;Phần cứng thực thi phép biến đổi và đo lượng tử theo kiến trúc thiết bị.;F4.5
Lần chạy đo;shot;;Một lần thực hiện/đo mạch theo ngữ cảnh thu counts, cần nhiều shots ước lượng phân bố.;F4.5
Phân phối khóa lượng tử;Quantum Key Distribution;QKD;Hướng truyền thông lượng tử phục vụ thiết lập khóa, khác thuật toán QML.;F4.6
Vận hành học máy lượng tử;Quantum Machine Learning Operations;QMLOps;Hướng quản lý vòng đời mô hình/quy trình QML được nêu ở phần nghiên cứu.;F4.6
Thành phần đánh giá;course assessment;;Cách chia trọng số hoạt động trong tài liệu môn học, cần giữ mốc phiên bản.;F5.1
Mốc so sánh;baseline;;Phương pháp/cấu hình tham chiếu rõ ràng để đánh giá cải tiến.;F5.2
Khả năng tái lập;reproducibility;;Khả năng thực hiện lại phương pháp với dữ liệu/cấu hình đã ghi và kiểm tra kết luận.;F5.2
'''
for row in TERMS.strip().splitlines():
 name,en,abbr,definition,lid=row.split(';');li=next(x for x in L if x['id']==lid)
 term(name,en,abbr,definition,li['plain'],li['example'],li['confusion'],lid)

E=[]
def essay(id,title,lessons,prompt,hints,model,criteria):
 E.append(dict(id=id,title=title,lessons=lessons.split('|'),prompt=prompt,hints=hints.split('|'),model=model,criteria=[{'text':t,'max':int(p)} for p,t in (x.split(':',1) for x in criteria.split('|'))],refs=[r for l in L if l['id'] in lessons.split('|') for r in l['refs']]))
essay('e1','Thiết kế cho mùa đăng ký','1.5|2.1|10.2|13.2','Một cổng đăng ký có tải tăng từ 100 lên 800 yêu cầu/giây trong 1 phút. Mỗi bản sao web chịu 100 yêu cầu/giây, DB chịu 450, bản sao mới mất 90 giây để sẵn sàng. Hãy phân tích nút thắt, ước lượng lý tưởng số bản sao web và đề xuất phương án vận hành có giới hạn.','Tách năng lực web và DB.|Số bản sao desired chưa phải ready.|Hãy xét dự báo tải và thời gian khởi động.',
'Tầng web lý tưởng cần ít nhất ceil(800/100)=8 bản sao theo giả định chia đều, chưa tính dự phòng. Nhưng DB trần 450 nên chỉ tăng web không đạt 800. 90 giây khởi động lớn hơn cửa sổ tăng 60 giây, phản ứng sau khi quá tải sẽ chậm. Có thể chuẩn bị trước tải dự kiến, kiểm tra/giảm truy vấn hoặc cache khi ngữ nghĩa cho phép, kiểm soát tiếp nhận/hàng đợi. Đặt readiness, theo dõi latency/lỗi và cửa sổ ổn định; không scale liên tiếp từ metric cũ. Mọi cách tăng DB phải được đo, không cam kết chỉ thêm replica sẽ tăng mọi ghi.',
'2:Tính 8 bản sao và nêu giả định|3:Chỉ ra trần DB 450 và tác động|3:Phân tích 90 giây so với 60 giây, đề xuất khả thi|2:Nêu quan sát, readiness và giới hạn/đánh đổi')
essay('e2','VM hay container','5.3|6.1|6.2|6.3','Nhóm có ứng dụng cần kernel Windows và một pipeline Python tạo hàng nghìn tác vụ ngắn trên Linux. Đề xuất môi trường cho từng loại, giải thích ranh giới cách ly và quy trình đóng gói.','Container chia sẻ kernel nào?|Tách overhead startup và tốc độ thuật toán.|Dockerfile, image, container khác nhau.',
'Ứng dụng cần kernel Windows không thể chạy như một Linux container thuần trên Linux host; chọn VM Windows hoặc môi trường Windows/container tương thích với yêu cầu. Pipeline Python ngắn có thể dùng container để giảm boot OS riêng, sau khi kiểm tra thư viện, dữ liệu, image và độ trễ tải. VM có guest kernel dưới hypervisor; container chia sẻ kernel host với namespace và cơ chế giới hạn tài nguyên. Dockerfile được build thành image, registry phân phối rồi runtime tạo container. Ghi dữ liệu cần tồn tại ra volume/dịch vụ lưu trữ; không đặt bí mật trong image. Quyết định cuối cần benchmark cùng workload/tài nguyên.',
'3:Phân biệt yêu cầu kernel và chọn môi trường có điều kiện|3:Giải thích cách ly VM/container đúng|2:Quy trình build–image–run|2:Dữ liệu, bí mật, benchmark và giới hạn')
essay('e3','MapReduce bị lệch tải','11.2|11.3|11.4','Job đếm lỗi từ log có 90% bản ghi cùng khóa OK. Có 100 mapper, 10 reducer; một reducer chạy rất lâu. Giải thích cơ chế, vì sao thêm mapper chưa đủ và cách cải thiện vẫn giữ kết quả đúng.','Theo đường map → shuffle → reduce.|Một khóa thường được partition tới đâu?|Đếm cục bộ có thể kết hợp bằng tổng không?',
'Map phát khóa và số đếm, shuffle gom cùng khóa vào partition của reducer. Khóa OK chiếm 90% làm một reducer trở thành straggler, hash tốt vẫn không chia một khóa theo mặc định. Thêm mapper có thể phát dữ liệu nhanh hơn nhưng không giảm việc ở reducer đó. Với phép cộng kết hợp được, có thể tổng hợp cục bộ/combiner hợp lệ trước truyền, hoặc chia khóa trung gian có chủ đích rồi reduce lần hai để khôi phục tổng. Đo phân bố partition, lượng shuffle và thời gian reducer; bảo đảm mỗi record được tính đúng theo semantics và retry của framework. HDFS locality hỗ trợ đọc nhưng không tự sửa skew.',
'3:Theo vết map/shuffle/reduce chính xác|2:Giải thích skew và vì sao thêm mapper không đủ|3:Giải pháp hợp lệ và giữ tổng|2:Metric kiểm chứng cùng giới hạn locality')
essay('e4','Một sự kiện bị giao hai lần','14.2|F3.3|F3.5','Pipeline bán hàng dùng hàm serverless trừ tồn kho và lưu ảnh hóa đơn. Cùng một sự kiện có thể được giao lại. Thiết kế xử lý để tránh trừ hai lần, nêu nơi lưu trạng thái và trường hợp lỗi từng phần.','Stateless không có nghĩa không side effect.|Cần ID và ràng buộc nguyên tử.|Ghi DB và object không tự là một giao dịch.',
'Dùng event ID bền để nhận diện thao tác đã xử lý. Việc kiểm tra ID và cập nhật tồn cần được phối hợp nguyên tử phù hợp DB, nếu chỉ đọc rồi ghi rời có thể race. Trạng thái bền nằm ở DB/kho dữ liệu, không chỉ RAM hàm. Khi ghi ảnh và DB thuộc hai hệ, cần mô hình trạng thái job, retry có idempotency và đối soát/bù trừ phù hợp. Ví dụ ghi ảnh với khóa gắn event ID rồi cập nhật trạng thái hoàn tất; nếu lỗi sau ghi ảnh, lần sau nhận diện object/trạng thái và tiếp tục. Không tuyên bố “exactly once” chỉ vì dùng FaaS; quan sát các job lỗi và kiểm thử crash giữa các bước.',
'3:Phân tích tác dụng lặp và stateless|3:ID bền cùng cập nhật nguyên tử hoặc cơ chế tương đương|2:Xử lý lỗi từng phần DB/object|2:Retry, đối soát và giới hạn cam kết')
essay('e5','Canary và dữ liệu','15.2|15.3|15.4','Bạn triển khai canary 5%. Bản mới lỗi 6%, bản cũ lỗi 0,1%; bản mới cũng đã thay schema DB không tương thích bản cũ. Hãy đề xuất hành động và kế hoạch phát hành an toàn hơn.','CPU thấp có chứng minh canary tốt không?|Rollback code có rollback schema không?|Cần so nhóm và metric nào?',
'Dừng tăng canary, đánh giá ảnh hưởng và hạn chế lỗi theo playbook. Tỷ lệ lỗi tăng là tín hiệu xấu nhưng cần kiểm tra mẫu, nhóm lưu lượng và định nghĩa lỗi. Không quay mã về mù quáng vì schema đã không tương thích. Xử lý dữ liệu theo kế hoạch migration/khôi phục được chuẩn bị, cân nhắc sửa tiến hoặc rollback có kiểm chứng. Lần sau dùng thay đổi schema tương thích theo giai đoạn, test tích hợp, cùng artifact, tiêu chí dừng và rollback trước phát hành. Theo dõi latency, lỗi, tính đúng dữ liệu và error budget; canary chỉ giảm phạm vi thử, không bảo đảm vô hại.',
'2:Hành động dừng/hạn chế và đo đúng|3:Phân tích schema cùng giới hạn rollback code|3:Kế hoạch tương thích và test|2:Metric dịch vụ/error budget và giới hạn canary')
essay('e6','Bảo mật nhiều chặng','7.1|17.2|17.3|17.4','Người dùng qua VPN, HTTPS kết thúc ở reverse proxy, sau đó HTTP tới API. API chỉ kiểm tra có token và cho sửa mọi tài khoản. Xác định các ranh giới và đề xuất sửa.','Đánh dấu VPN/TLS kết thúc ở đâu.|Xác thực khác quyền trên tài nguyên.|Private IP không thay kiểm tra quyền.',
'VPN bảo vệ phạm vi tunnel tới gateway theo cấu hình, không tự bảo vệ mọi đoạn phía sau. TLS kết thúc tại proxy nên đoạn HTTP proxy–API không nằm trong phiên bảo vệ client–proxy. Cần xác định trust boundary và bảo vệ đoạn nội bộ thích hợp. API không chỉ kiểm tra sự tồn tại token: cần xác minh hợp lệ, danh tính, hạn dùng/ngữ cảnh phù hợp và quyền đối với tài khoản/hành động. Phân quyền tối thiểu, không tin IP nội bộ mặc định. Bảo vệ khóa, endpoint và log; mã hóa không sửa lỗi authorization. Cấu hình cụ thể cần dựa mô hình đe dọa và hạ tầng thực.',
'3:Vẽ/giải thích đúng điểm kết thúc VPN/TLS|3:Phân biệt xác thực và phân quyền, sửa quyền tài nguyên|2:Chính sách nội bộ/zero trust phù hợp|2:Giới hạn mã hóa, endpoint và vận hành')
essay('e7','Edge khi mất WAN','16.1|16.2|16.3|8.4','Một hệ camera liên tục sinh dữ liệu nhưng WAN có thể mất 2 giờ. Thiết kế phần chạy local/edge/cloud, cách lưu rồi gửi lại và cách đánh giá chất lượng bộ lọc.','Tác vụ nào phải phản ứng tại chỗ?|Cần bao nhiêu dữ liệu giữ lại?|Gửi lại có thể trùng hoặc sai thứ tự.',
'Đặt xử lý cần độ trễ thấp hoặc cần sống khi mất WAN ở local/edge. Cloud nhận tổng hợp hoặc dữ liệu cần phân tích dài hạn. Thiết kế buffer bền đủ cho thời gian/bitrate cùng dự phòng, chính sách khi đầy, timestamp và event ID. Khi mạng trở lại gửi có kiểm soát tránh bão tải, chống trùng và xử lý thứ tự theo nhu cầu. Bộ lọc cần đánh giá bỏ sót/báo sai, không chỉ lượng byte giảm. Nêu rủi ro privacy, cập nhật model và bảo vệ nhiều thiết bị. Không coi edge tự bảo đảm an toàn hay dữ liệu không bao giờ mất.',
'3:Phân chia chức năng theo trễ và lỗi kết nối|3:Buffer bền, dung lượng/chính sách và gửi lại|2:Metric chất lượng lọc lẫn hiệu năng|2:Đánh đổi bảo mật, vận hành và giới hạn')
essay('e8','HA không chỉ thêm máy','F2.2|F2.3|4.4','Hai node DB active/passive dùng heartbeat. Đường heartbeat đứt nhưng hai node vẫn sống và cùng truy cập storage. Phân tích nguy cơ và điều kiện để failover an toàn.','Không nghe heartbeat có chắc node chết không?|Ai được quyền ghi?|Hạ tầng chung có điểm lỗi nào?',
'Mất heartbeat không phân biệt chắc lỗi node với lỗi mạng. Hai bên có thể cùng nhận active tạo split brain, ghi xung đột và hỏng dữ liệu. Cần cơ chế quyết định quyền/quorum và fencing phù hợp để chỉ bên được phép tiếp tục ghi, cùng quy trình chuyển vai kiểm thử được. Shared storage cần phối hợp và dự phòng; hai compute không loại bỏ single point ở storage/nguồn/mạng. Cân bằng availability và tính đúng dữ liệu, nêu giả định đường điều khiển. Kiểm thử phân vùng mạng, node treo, mất storage và khôi phục đồng bộ.',
'3:Phân biệt lỗi heartbeat và lỗi node|3:Split brain và cơ chế ngăn ghi đồng thời|2:Điểm lỗi chung và quy trình phục hồi|2:Giả định, thử lỗi và đánh đổi')
essay('e9','Thí nghiệm quantum cloud','F4.1|F4.2|F4.3|F4.5','Nhóm tuyên bố “8 qubit đọc được 256 đáp án trong một lần và nhanh hơn CPU” sau khi chạy simulator. Hãy phản biện và đề xuất phép thử có ý nghĩa.','Một shot cho đầu ra gì?|Simulator khác QPU.|Speedup so tổng thời gian nào?',
'8 qubit có trạng thái tổng quát gồm 256 biên độ, nhưng một phép đo theo cơ sở tính toán cho một chuỗi 8 bit, không đọc mọi đáp án. Simulator cổ điển không chứng minh đã dùng QPU thật hoặc lợi thế lượng tử. Cần mô tả bài toán, thuật toán, cách mã hóa, số shots, noise/backend, độ đúng/sai số và baseline cổ điển cùng điều kiện. Đo tổng thời gian gồm chuẩn bị, truyền, hàng đợi, QPU và hậu xử lý; phân biệt thời gian QPU riêng. Lặp thí nghiệm, lưu cấu hình và kết quả, nêu giới hạn NISQ. Chỉ kết luận trong phạm vi phép thử, không khẳng định lợi thế phổ quát.',
'3:Sửa diễn giải 256 biên độ và phép đo|2:Phân biệt simulator/QPU|3:Thiết kế baseline, metric, chất lượng và thời gian đầu cuối|2:Tái lập, nhiễu và giới hạn kết luận')

# Liên kết tiên quyết, cùng chương và thuật ngữ ổn định theo ID.
for c in C:
 units=[l for l in L if l['chapter']==c['id']]
 for i,l in enumerate(units):
  l['related']=list(dict.fromkeys(c['prior']+[x['id'] for x in units[max(0,i-1):i+2] if x['id']!=l['id']]))
# Gắn mức nhận biết cho các câu yêu cầu nhận diện chức năng/thuật ngữ trực tiếp.
for q in Q:
 if q['lesson'] in ['1.3','2.3','2.4','3.3','4.1','5.1','5.2','5.3','6.4','7.2','8.3','9.5','10.1','10.4','10.5','11.2','11.4','12.5','13.3','15.1','15.3','F2.5','F2.6','F3.2','F3.4','F3.5']:q['level']='Nhận biết'

# Giữ trọn văn bản nguồn để tìm kiếm đối chiếu; phần giảng không phải bản dịch nguyên văn.
import fitz
D=[]; page_map=[]
for name in sorted(files):
 doc=fitz.open(files[name]);texts=[p.get_text() for p in doc]
 lesson_refs=[(l,r) for l in L for r in l['refs'] if r['file']==name]
 image_heavy=[]
 for n,t in enumerate(texts,1):
  body=re.sub(r'Prof[^\n]*|CompSci[^\n]*|Distributed Computing Systems Course','',t)
  if len(body.strip())<80:image_heavy.append(n)
  linked=[l['id'] for l,r in lesson_refs if r['start']<=n<=r['end']]
  page_map.append(dict(file=name,pdfPage=n,printedPage=str(n-19) if name==BOOK and 24<=n<=282 else '',lessons=list(dict.fromkeys(linked)),status='Đối chiếu theo cụm chủ đề' if linked else ('Bìa/mục lục/chỉ mục hoặc phần sách ngoài phạm vi trục slide' if name==BOOK else 'Chưa có liên kết bài: cần đối chiếu')))
 D.append(dict(file=name,pages=len(texts),role='Sách bổ trợ' if name==BOOK else ('Trục slide chính' if re.match(r'^\d\d-',name) else 'Tài liệu bổ sung'),imageHeavy=image_heavy,texts=texts))

DATA=dict(schemaVersion=1,version='2026.10.16.1',title='CloudLab • Học để hiểu',chapters=C,lessons=L,questions=Q,terms=G,essays=E,documents=D,coverage=page_map,examEssaySets=[['e1','e2','e3'],['e4','e5','e6'],['e7','e8','e9']],notes=[
'Số bài 1.1, F1.1… là số điều hướng do ứng dụng đặt theo cụm chủ đề, không khẳng định trùng số mục gốc. Bảng nguồn giữ tên và trang PDF để tra lại. Sách có mục lục gốc riêng trong trang nguồn.',
'Các đoạn giải thích tiếng Việt là biên soạn/diễn giải theo phạm vi nguồn dẫn; ví dụ có nhãn tự xây dựng là dữ kiện giả định. Không xem lời giải và câu hỏi do ứng dụng tạo là câu hỏi gốc của giảng viên.',
'Trang PDF đếm từ 1. Trong phần thân sách được dùng, trang in = trang PDF − 19. Bìa, mục lục La Mã và chỉ mục được mở trực tiếp trong PDF, không tự đánh số in theo công thức.',
'Trang ít chữ hoặc chỉ có ảnh được đánh dấu để mở bản gốc. Đã kiểm tra trích xuất 24 file; không khẳng định đã xác minh từng chi tiết trong tất cả ảnh/screenshot.',
'Nguồn cũ được giảng như tài liệu theo thời điểm, không dùng để khẳng định giá, roadmap, chính sách hoặc lệnh cài đặt hiện hành. Chưa có đề mẫu nên bộ đề chỉ phục vụ tự luyện.',
'Các bài được gộp theo tiêu đề/cụm slide liên tiếp và bao phủ toàn bộ trang slide qua bảng đối chiếu; không có nghĩa mọi chi tiết sách được mở rộng thành một bài riêng. Các mô hình và chủ đề chuyên sâu vẫn cần đọc trang nguồn được dẫn.'
])
(ROOT/'data/content.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'data/content.js').write_text('window.CLOUD_DATA = '+json.dumps(DATA,ensure_ascii=False)+';',encoding='utf-8')
import csv
with (ROOT/'docs/doi-chieu.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['Tên file','Trang PDF','Trang in','Bài liên quan','Trạng thái'])
 for row in page_map:w.writerow([row['file'],row['pdfPage'],row['printedPage'],', '.join(row['lessons']),row['status']])
print(json.dumps({'chapters':len(C),'lessons':len(L),'mcq':len(Q),'terms':len(G),'essays':len(E),'documents':len(D),'pages':sum(d['pages'] for d in D),'unmappedSlidePages':len([r for r in page_map if not r['lessons'] and r['file']!=BOOK])},ensure_ascii=False))
with (ROOT/'docs/doi-chieu-chuong-muc.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['Nhóm','Chương','Bài ứng dụng','Tên bài','Mục tiêu chương kiểm chứng được','Tiên quyết','File slide','Trang PDF slide','File sách','Trang PDF sách','Trang in sách','Chủ đề kết nối'])
 for l in L:
  c=next(c for c in C if c['id']==l['chapter']);sr=l['refs'][0];br=next((r for r in l['refs'] if r['kind']=='book'),{})
  w.writerow([c['id'],c['title'],l['id'],l['title'],'; '.join(c['goals']),'; '.join(c['prior']),sr['file'],f"{sr['start']}–{sr['end']}",br.get('file',''),f"{br.get('start','')}–{br.get('end','')}" if br else '',br.get('printed',''),'; '.join(l['related'])])
